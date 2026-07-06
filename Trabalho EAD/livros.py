def buscar_livro_por_isbn(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
    return None


def cadastrar_livro(livros, titulo, autor, editora, edicao, ano, isbn, status, paginas_totais, paginas_lidas=0):
    if buscar_livro_por_isbn(livros, isbn) is not None:
        return False

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "edicao": edicao,
        "ano": ano,
        "isbn": isbn,
        "status": status,
        "paginas_totais": paginas_totais,
        "paginas_lidas": paginas_lidas,
    }
    livros.append(novo_livro)
    return True


def editar_livro(livros, isbn, **campos_novos):
    livro = buscar_livro_por_isbn(livros, isbn)
    if livro is None:
        return False

    for chave, valor in campos_novos.items():
        if chave in livro and valor is not None:
            livro[chave] = valor

    return True


def remover_livro(livros, isbn):
    livro = buscar_livro_por_isbn(livros, isbn)
    if livro is None:
        return False

    livros.remove(livro)
    return True


def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado ainda.")
        return

    print("\n--- Lista de Livros ---")
    for i, livro in enumerate(livros, start=1):
        progresso = calcular_progresso(livro["paginas_lidas"], livro["paginas_totais"])
        print(f"{i}. {livro['titulo']} ({livro['ano']}) - {livro['autor']}")
        print(f"   Editora: {livro['editora']} | Edição: {livro['edicao']} | ISBN: {livro['isbn']}")
        print(f"   Status: {livro['status']} | Progresso: {livro['paginas_lidas']}/{livro['paginas_totais']} páginas ({progresso}%)")
    print("------------------------\n")


def calcular_progresso(paginas_lidas, paginas_totais):
    if paginas_totais == 0:
        return 0.0
    return round((paginas_lidas / paginas_totais) * 100, 1)