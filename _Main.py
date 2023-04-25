from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

from Opcoes import *
from Categorias import *

# <Funções Main> ######################################################################


class Main:

    def __init__(lista):
        pass

    def adicionar_categoria(lista):

        if entry_categoria.get() == '':
            messagebox.showinfo("Erro!", "Campo 'Categoria' está vazio")

        else:
            lista_categ.adicionar_categoria(entry_categoria.get())

    def adicionar_item_na_categoria(lista):

        if entrada_categoria.get() == '' or entrada_item.get() == '' or entrada_preco.get() == '':
            messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos.")

        else:
            posicao_atual = lista_categ.buscar(entrada_categoria.get())

            if (posicao_atual):
                posicao_atual.sub, posicao_atual.meio, posicao_atual.quant = lista_itens(
                    posicao_atual.sub, posicao_atual.meio, posicao_atual.quant).adicionar_item(entrada_item.get(), entrada_preco.get())

            else:
                messagebox.showerror(
                    "Erro!", f"{entrada_categoria.get()} não foi encontrado.")

    def limpar_categoria(lista):

        if entry_categoria.get() == '':
            messagebox.showerror(
                "Erro!", "Coloque a categoria no campo categoria.")

        else:
            if lista_categ.cabeca.sub is not None:

                resposta = messagebox.askyesno(
                    "Aviso!", "Essa função apagará todos os ítens do catálogo escolhido.\nDeseja continuar mesmo assim?")

                if resposta == True:
                    posicao_atual = lista_categ.buscar(entrada_categoria.get())

                    if (posicao_atual):
                        posicao_atual.sub, posicao_atual.meio, posicao_atual.quant = lista_itens(
                            posicao_atual.sub, posicao_atual.meio, posicao_atual.quant).liberar_memoria()

                        messagebox.showinfo(
                            "Sucesso!", "Foram removidos os ítens da Categoria.")

                    else:
                        messagebox.showinfo(
                            "Erro!", "Categoria não encontrada")
            else:
                messagebox.showerror(
                    "Erro!", "Não há ítens cadastrados nessa categoria.")

    def limpar_tudo(lista):

        if lista_categ.cabeca is not None:
            resposta = messagebox.askyesno(
                "Aviso!", "Essa ação apagará todos os processos cadastrados.\nVocê tem certeza que deseja continuar?")

            if lista_categ.cabeca is not None:
                if resposta == True:
                    no = lista_categ.cabeca
                    while no is not None:

                        if no.sub is not None:
                            lista_itens(no.sub, no.meio,
                                        no.quant).liberar_memoria()

                        if no.proximo is not None:
                            no.anterior = None

                        no = no.proximo

                    lista_categ.cabeca = no = None
                    messagebox.showinfo(
                        "Sucesso!", "Todos os ítens foram removidos.")
        else:
            messagebox.showerror("Erro!", "Nenhum cadastro foi encontrado.")

    def remover_item_da_categoria(lista):

        if entry_categoria.get() == '' or entry_item.get() == '':
            messagebox.showerror(
                "Erro!", "Os campos categoria e item precisam estar preenchidos.")

        posicao_atual = lista_categ.buscar(entry_categoria.get())

        if (posicao_atual):

            posicao_atual.sub, posicao_atual.meio, posicao_atual.quant = lista_itens(
                posicao_atual.sub, posicao_atual.meio, posicao_atual.quant).remover(entrada_item.get())

    def remover_categoria(lista):
        if entry_categoria.get() == '':
            messagebox.showerror(
                "Erro!", "Digite a categoria que deseja remover no campo categoria.")

        else:
            posicao_atual = lista_categ.buscar(entry_categoria.get())

            if (posicao_atual):

                if (posicao_atual.sub is not None):
                    resposta = messagebox.askyesno(
                        "Confirmação!", "Existem ítens cadastrados nessa categoria.\nDeseja continuar mesmo assim?")

                    if resposta == True:

                        lista_itens(posicao_atual.sub, posicao_atual.meio,
                                    posicao_atual.quant).liberar_memoria()
                        lista_categ.remover(entrada_categoria.get())

                else:
                    lista_categ.remover(entrada_categoria.get())

            else:
                messagebox.showinfo(
                    "Erro!", f"{entry_categoria.get()} não foi encontrado.")

    def abrir_cardapio(lista):

        janela_cardapio = tk.Toplevel(root)
        janela_cardapio.geometry('666x780')
        janela_cardapio.resizable(False, False)
        janela_cardapio.title('Cardápio')

        imagem = ImageTk.PhotoImage(Image.open("Icon/background_cardapio.png"))
        canvas = tk.Canvas(janela_cardapio, width=imagem.width(),
                           height=imagem.height(), background="#242424", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=imagem, anchor="nw")

        # Cria o frame que contém as labels
        frame = tk.Frame(canvas, background='#242424', highlightthickness=0)

        no = lista_categ.cabeca
        if no is not None:
            while no is not None:
                label = tk.Label(frame, text=f'{no.categoria}', background='#242424', font=(
                    "Times New Roman", 20), foreground="#FFCD4E")
                label.pack(side="top", anchor="w", padx=10, pady=5)

                no_sublista = no.sub
                while no_sublista is not None:
                    label = tk.Label(frame, text=f'         {no_sublista.item}.........................R$: {no_sublista.preco}', background='#242424', font=(
                        "Times New Roman", 14), foreground="white")
                    label.pack(side="top", anchor="w", padx=10, pady=5)

                    no_sublista = no_sublista.proximo

                no = no.proximo

        # Cria a scrollbar e a associa ao canvas
        scrollbar = tk.Scrollbar(
            canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # Associa o frame ao canvas
        canvas.create_window((100, 340), window=frame, anchor='nw')
        frame.update_idletasks()

        # Configura a scrollbar para afetar o canvas e vice-versa
        canvas.config(yscrollcommand=scrollbar.set)
        frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        janela_cardapio.grab_set()
        janela_cardapio.focus_set()
        janela_cardapio.wait_window()
######################################################################################


lista_categ = ListaDuplamenteEncadeada()
lista_itens = SublistaDuplamenteEncadeada
main = Main()


# <TkInter> #########################################################################


root = tk.Tk()


# <Background e Tamanho> #############################################################
canvas = tk.Canvas(root, width=1024, height=768)
canvas.pack()

root.geometry("716x770")
root.resizable(False, False)
root.title('Painel De Controle')

image = Image.open("Icon/background.png")
photo = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor="nw", image=photo)
####################################################################################


frame_width = 500
frame_height = 500

cor_do_fundo = '#FCBF02'


# <Frames> #####################################################################
frame_2 = tk.Frame(canvas, width=100, height=100, background=cor_do_fundo)

frame_3 = tk.Frame(canvas, width=100, height=100, background=cor_do_fundo)
frame_4 = tk.Frame(canvas, width=50, height=50, background=cor_do_fundo)

frame_5 = tk.Frame(canvas, width=50, height=50, background=cor_do_fundo)
frame_6 = tk.Frame(canvas, width=50, height=50, background=cor_do_fundo)

frame_8 = tk.Frame(canvas, height=50, background='white')
frame_9 = tk.Frame(canvas, height=50, background='white')
frame_10 = tk.Frame(canvas, height=50, background='white')
######################################################################

# <Canvas> #####################################################################
canvas.create_window(110, 250, anchor="nw", window=frame_2, height=300)
canvas.create_window(370, 250, anchor="nw", window=frame_3, height=300)
canvas.create_window(245, 580, anchor="nw", window=frame_4)
canvas.create_window(370, 460, anchor="nw", window=frame_5)
canvas.create_window(110, 460, anchor="nw", window=frame_6)
canvas.create_window(110, 210, anchor="nw", window=frame_8)
canvas.create_window(370, 210, anchor="nw", window=frame_9)
canvas.create_window(500, 210, anchor="nw", window=frame_10)
#################################################################################


# <Imagens> #####################################################################
btn_AdicionarCatg_image = Image.open("Icon/adicionar_categoria.png")
btn_AdicionarCateg_photo = ImageTk.PhotoImage(btn_AdicionarCatg_image)

btn_RemoverCateg_image = Image.open("Icon/remover_categoria.png")
btn_RemoverCateg_photo = ImageTk.PhotoImage(btn_RemoverCateg_image)


btn_AdicionarItem_image = Image.open("Icon/adicionar_item.png")
btn_AdicionarItem_photo = ImageTk.PhotoImage(btn_AdicionarItem_image)

btn_RemoverItem_imagem = Image.open("Icon/remover_item.png")
btn_RemoverItem_photo = ImageTk.PhotoImage(btn_RemoverItem_imagem)


btn_limpar_categ_image = Image.open("Icon/limpar_categoria.png")
btn_limpar_categ_photo = ImageTk.PhotoImage(btn_limpar_categ_image)

btn_apagar_tudo_image = Image.open("Icon/apagar_tudo.png")
btn_apagar_tudo_photo = ImageTk.PhotoImage(btn_apagar_tudo_image)


btn_imprimir_image = Image.open("Icon/visualizar.png")
btn_imprimir_photo = ImageTk.PhotoImage(btn_imprimir_image)
########################################################################################


# <Botões e Entry> #####################################################################


btn_adicionar_categ = tk.Button(frame_2, image=btn_AdicionarCateg_photo,
                                background=cor_do_fundo, relief="flat", command=main.adicionar_categoria)
btn_adicionar_categ.pack(padx=10, pady=5)


btn_remover_categ = tk.Button(frame_2, image=btn_RemoverCateg_photo,
                              background=cor_do_fundo, relief="flat", command=main.remover_categoria)
btn_remover_categ.pack(padx=10, pady=5)


btn_adicionar_item = tk.Button(frame_3, image=btn_AdicionarItem_photo,
                               background=cor_do_fundo, relief="flat", command=main.adicionar_item_na_categoria)
btn_adicionar_item.pack(padx=10, pady=5)


btn_remover_item = tk.Button(frame_3, image=btn_RemoverItem_photo,
                             background=cor_do_fundo, relief="flat", command=main.remover_item_da_categoria)
btn_remover_item.pack(padx=10, pady=5)


entrada_categoria = tk.StringVar()
entry_categoria = tk.Entry(frame_8, font=(
    'Arial', 12), width=26, relief='flat', textvariable=entrada_categoria)
entry_categoria.pack()


entrada_item = tk.StringVar()
entry_item = tk.Entry(frame_9, font=('Arial', 12), width=11,
                      relief='flat', textvariable=entrada_item)
entry_item.pack()


entrada_preco = tk.StringVar()
entry_preco = tk.Entry(frame_10, font=('Arial', 12), width=11,
                       relief='flat', textvariable=entrada_preco)
entry_preco.pack()


btn_visualizar = tk.Button(frame_4, image=btn_imprimir_photo,
                           background=cor_do_fundo, relief="flat", command=main.abrir_cardapio)
btn_visualizar.pack(padx=10, pady=5)


btn_limpar_categ = tk.Button(frame_5, image=btn_limpar_categ_photo,
                             background=cor_do_fundo, relief="flat", command=main.limpar_categoria)
btn_limpar_categ.pack(padx=10, pady=5)


btn_apagar_tudo = tk.Button(frame_6, image=btn_apagar_tudo_photo,
                            background=cor_do_fundo, relief="flat", command=main.limpar_tudo)
btn_apagar_tudo.pack(padx=10, pady=5)
#######################################################################

root.mainloop()
#######################################################################################
