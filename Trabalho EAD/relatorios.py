from livros import calcular_progresso 


def gerar_matriz_relatorio(livros):

    cabecalho = ["Título", "Status", "Pág. Lidas", "Pág. Totais", "Progresso"]
    matriz = [cabecalho]

    for livro in livros:
        progresso = calcular_progresso(livro["paginas_lidas"], livro["paginas_totais"])
        linha = [
            livro["titulo"],
            livro["status"],
            str(livro["paginas_lidas"]),
            str(livro["paginas_totais"]),
            f"{progresso}%",
        ]
        matriz.append(linha)

    return matriz


def imprimir_matriz_relatorio(matriz):
    if len(matriz) <= 1:
        print("Sem livros suficientes para gerar relatório.\n")
        return

    # descobre a largura máxima de cada coluna, olhando todas as linhas
    num_colunas = len(matriz[0])
    larguras = [0] * num_colunas

    for linha in matriz:
        for coluna_idx in range(num_colunas):
            tamanho = len(linha[coluna_idx])
            if tamanho > larguras[coluna_idx]:
                larguras[coluna_idx] = tamanho

    print("\n--- Relatório Geral de Livros ---")
    for linha_idx, linha in enumerate(matriz):
        texto_linha = ""
        for coluna_idx in range(num_colunas):
            texto_linha += linha[coluna_idx].ljust(larguras[coluna_idx] + 2)
        print(texto_linha)

        if linha_idx == 0:
            print("-" * sum(larguras[i] + 2 for i in range(num_colunas)))
    print()


def contar_livros_por_status(livros):
    contagem = {}
    for livro in livros:
        status = livro["status"]
        if status in contagem:
            contagem[status] += 1
        else:
            contagem[status] = 1
    return contagem