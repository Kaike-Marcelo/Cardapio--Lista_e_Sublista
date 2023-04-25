from tkinter import messagebox


class No_Sub:

    def __init__(lista, item, preco):
        lista.item = item
        lista.preco = preco
        lista.proximo = None
        lista.anterior = None


class SublistaDuplamenteEncadeada:

    def __init__(lista, sub, meio, quant):
        lista.cabeca = sub
        lista.meio = meio
        lista.quant = quant

    def adicionar_item(lista, item, preco):
        novo_no = No_Sub(item, preco)
        lista.quant += 1

        if lista.cabeca == None:
            lista.cabeca = lista.meio = novo_no
            messagebox.showinfo("Sucesso!", "Ítem adicionado à categoria.")
        else:
            auxiliar = lista.cabeca
            auxiliar_meio = lista.meio

            if item < auxiliar.item:
                auxiliar.anterior = novo_no
                lista.cabeca = novo_no
                novo_no.proximo = auxiliar

                if lista.quant % 2 == 0:
                    lista.meio = lista.meio.anterior

                messagebox.showinfo("Sucesso!", "Ítem adicionado à categoria.")

            else:
                if item > lista.meio.item:
                    while auxiliar_meio.proximo and auxiliar_meio.item < item:
                        auxiliar_meio = auxiliar_meio.proximo

                    if auxiliar_meio.item != item:

                        if auxiliar_meio.item > item:
                            novo_no.proximo = auxiliar_meio
                            novo_no.anterior = auxiliar_meio.anterior

                            auxiliar_meio.anterior = novo_no
                            novo_no.anterior.proximo = novo_no

                        else:
                            novo_no.proximo = auxiliar_meio.proximo
                            novo_no.anterior = auxiliar_meio
                            auxiliar_meio.proximo = novo_no

                        if lista.quant % 2 != 0:
                            lista.meio = lista.meio.proximo

                        messagebox.showinfo(
                            "Sucesso!", "Ítem adicionado à categoria.")

                    else:
                        lista.quant -= 1
                        messagebox.showerror("Erro!", "Ítem já cadastrado.")
                        del (novo_no)

                else:
                    while auxiliar.proximo and auxiliar.item < item:
                        auxiliar = auxiliar.proximo

                    if auxiliar.item != item:

                        if auxiliar.item > item:
                            novo_no.proximo = auxiliar
                            novo_no.anterior = auxiliar.anterior

                            novo_no.anterior.proximo = novo_no
                            auxiliar.anterior = novo_no

                            if lista.quant % 2 != 0:
                                lista.meio = lista.meio.anterior

                            messagebox.showinfo(
                                "Sucesso!", "Ítem adicionado à categoria.")

                        else:
                            novo_no.anterior = auxiliar
                            auxiliar.proximo = novo_no

                            if lista.quant % 2 != 0:
                                lista.meio = lista.meio.proximo
                            messagebox.showinfo(
                                "Sucesso!", "Ítem adicionado à categoria.")
                    else:
                        lista.quant -= 1
                        messagebox.showerror("Erro!", "Ítem já cadastrado.")

        return lista.cabeca, lista.meio, lista.quant

    def remover(lista, item):

        if lista.cabeca == None:
            messagebox.showerror(
                "Erro!", "A categoria não possui ítens cadastrados.")

        else:
            lista.quant -= 1

            if lista.cabeca.proximo is None:
                lista.cabeca = lista.meio = None
                messagebox.showinfo("Sucesso!", "Ítem removido da categoria.")

            else:
                if item < lista.meio.item:
                    auxiliar = lista.cabeca

                    if auxiliar.item == item:
                        auxiliar.proximo.anterior = auxiliar.anterior
                        lista.cabeca = auxiliar.proximo

                        messagebox.showinfo(
                            "Sucesso!", "Ítem removido da categoria.")
                        del (auxiliar)

                    else:
                        while auxiliar.proximo.item is not lista.meio.item and auxiliar.proximo.item < item:
                            auxiliar = auxiliar.proximo

                        if auxiliar.item == item:
                            auxiliar.anterior.proximo = auxiliar.proximo
                            auxiliar.proximo.anterior = auxiliar.anterior

                            messagebox.showinfo(
                                "Sucesso!", "Ítem removido da categoria.")
                            del (auxiliar)

                        else:
                            lista.quant += 1
                            messagebox.showerror(
                                "Erro!", "Ítem não encontrado.")

                    if lista.quant % 2 != 0:
                        lista.meio = lista.meio.proximo

                else:
                    auxiliar_meio = lista.meio
                    while auxiliar_meio.proximo and auxiliar_meio.item < item:
                        auxiliar_meio = auxiliar_meio.proximo

                    if auxiliar_meio.item == item:

                        if auxiliar_meio.anterior is None:
                            auxiliar_meio.proximo.anterior = auxiliar_meio.anterior
                            lista.cabeca = auxiliar_meio.proximo

                            lista.meio = lista.meio.proximo
                            messagebox.showinfo(
                                "Sucesso!", "Ítem removido da categoria.")
                            del (auxiliar_meio)

                        else:
                            if auxiliar_meio.proximo == None:
                                auxiliar_meio.anterior.proximo = auxiliar_meio.proximo
                                auxiliar_meio.anterior = auxiliar_meio.proximo

                            else:
                                auxiliar_meio.anterior.proximo = auxiliar_meio.proximo
                                auxiliar_meio.proximo.anterior = auxiliar_meio.anterior

                            messagebox.showinfo(
                                "Sucesso!", "Ítem removido da categoria.")
                            del (auxiliar_meio)

                            if lista.quant % 2 == 0:
                                lista.meio = lista.meio.anterior

                    else:
                        lista.quant += 1
                        messagebox.showerror("Erro!", "Ítem não encontrado.")

        return lista.cabeca, lista.meio, lista.quant

    '''
    def imprimir_ordenado(lista):
        no = lista.cabeca
        while no is not None:
            print(f"[{no.item}] [{no.preco}]", end=' -> ')
            no = no.proximo
        print()


    def buscar(lista, item):
        no = lista.meio

        if lista.cabeca == None:
            messagebox.showerror(
                "Erro!", "Não há ítens cadastrados nessa categoria.")

        else:
            if no.item > item:
                while no and no.item > item:
                    no = no.anterior
            else:
                while no and no.item < item:
                    no = no.proximo

            if no.item == item:
                print(f"\nResultados da busca: {no.item}")

            else:
                print("Erro! Nenhum Resultado Encontrado")
    '''

    def liberar_memoria(lista):
        no = lista.cabeca

        if lista.cabeca == None:
            messagebox.showerror(
                "Erro!", "Não há ítens cadastrados nessa categoria.")

        else:
            while no.proximo is not None:
                no.proximo.anterior = no.anterior
                no = no.proximo
            del (no)
            lista.cabeca = lista.meio = no = None
            lista.quant = 0

        return lista.cabeca, lista.meio, lista.quant
