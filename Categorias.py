from tkinter import messagebox


class No_lista:

    def __init__(lista, categoria):
        lista.categoria = categoria
        lista.proximo = None
        lista.anterior = None

        lista.sub = None
        lista.meio = None
        lista.quant = 0


class ListaDuplamenteEncadeada:

    def __init__(lista):
        lista.cabeca = None

    def adicionar_categoria(lista, categoria):
        novo_no = No_lista(categoria)

        if lista.cabeca == None:
            lista.cabeca = novo_no
            messagebox.showinfo("Sucesso!", "Categoria adicionada.")

        else:
            auxiliar = lista.cabeca

            if categoria < auxiliar.categoria:
                auxiliar.anterior = novo_no
                lista.cabeca = novo_no
                novo_no.proximo = auxiliar
                messagebox.showinfo("Sucesso!", "Categoria adicionada.")

            else:
                while auxiliar.proximo and auxiliar.categoria < categoria:
                    auxiliar = auxiliar.proximo

                if auxiliar.categoria == categoria:
                    messagebox.showinfo("Erro!", "Categoria já existe.")

                else:
                    if auxiliar.categoria > categoria:
                        novo_no.proximo = auxiliar
                        novo_no.anterior = auxiliar.anterior

                        novo_no.anterior.proximo = novo_no
                        auxiliar.anterior = novo_no

                    else:
                        novo_no.anterior = auxiliar
                        auxiliar.proximo = novo_no

                    messagebox.showinfo("Sucesso!", "Categoria adicionada.")

        # lista.imprimir_ordenado()

    def remover(lista, categoria):
        auxiliar = lista.cabeca

        if lista.cabeca == None:
            messagebox.showerror("Erro!", "Não há categorias cadastradas.")

        elif auxiliar.anterior == None and auxiliar.proximo == None and auxiliar.categoria == categoria:
            lista.cabeca = None
            messagebox.showinfo("Sucesso!", "Categoria removida.")

        else:
            while auxiliar.proximo and categoria > auxiliar.categoria:
                auxiliar = auxiliar.proximo

            if auxiliar.anterior == None and auxiliar.categoria == categoria:
                auxiliar = auxiliar.proximo
                auxiliar.anterior = None
                lista.cabeca = auxiliar
                messagebox.showinfo("Sucesso!", "Categoria removida.")

            else:
                if auxiliar.proximo == None and auxiliar.categoria == categoria:
                    auxiliar.anterior.proximo = None
                    messagebox.showinfo("Sucesso!", "Categoria removida.")

                else:
                    if auxiliar.categoria == categoria:
                        auxiliar.proximo.anterior = auxiliar.anterior
                        auxiliar.anterior.proximo = auxiliar.proximo
                        messagebox.showinfo("Sucesso!", "Categoria removida.")

                    else:
                        messagebox.showerror(
                            "Erro!", "Categoria não encontrada.")
    '''
    def liberar_disco(lista):
        no = lista.cabeca

        if lista.cabeca == None:
            messagebox.showinfo("Erro!", "Não há categorias cadastradas.")

        else:
            while no.proximo is not None:
                no = no.proximo
                no.anterior = None

            lista.cabeca = no = None
            messagebox.showinfo(
                "Sucesso!", "Todos os ítens foram removidos.")
    '''
    def imprimir_ordenado(lista):
        no = lista.cabeca
        while no is not None:
            print(no.categoria, end=' -> ')
            no = no.proximo

    def buscar(lista, categoria):
        ponteiro = lista.cabeca
        if lista.cabeca == None:
            messagebox.showerror("Erro!", "Não há Categorias cadastradas.")

        else:
            while ponteiro.proximo and categoria > ponteiro.categoria:
                ponteiro = ponteiro.proximo

            if ponteiro.categoria == categoria:
                return ponteiro
            else:
                return None
