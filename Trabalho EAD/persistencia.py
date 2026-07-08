import csv
import os

ARQUIVO_USUARIOS = "usuarios.csv"
ARQUIVO_LIVROS = "livros.csv"

CAMPOS_USUARIO = ["nome", "username", "senha", "nascimento"]
CAMPOS_LIVRO = ["titulo", "autor", "editora", "edicao", "ano", "isbn", "status", "paginas_totais", "paginas_lidas"]


def salvar_usuarios(usuarios, caminho=ARQUIVO_USUARIOS):
    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_USUARIO)
        escritor.writeheader()
        for usuario in usuarios:
            escritor.writerow(usuario)


def carregar_usuarios(caminho=ARQUIVO_USUARIOS):
    usuarios = []

    if not os.path.exists(caminho):
        return usuarios

    with open(caminho, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            usuarios.append({
                "nome": linha["nome"],
                "username": linha["username"],
                "senha": linha["senha"],
                "nascimento": linha["nascimento"],
            })

    return usuarios


def salvar_livros(livros, caminho=ARQUIVO_LIVROS):
    with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_LIVRO)
        escritor.writeheader()
        for livro in livros:
            escritor.writerow(livro)


def carregar_livros(caminho=ARQUIVO_LIVROS):
    livros = []

    if not os.path.exists(caminho):
        return livros

    with open(caminho, mode="r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            livros.append({
                "titulo": linha["titulo"],
                "autor": linha["autor"],
                "editora": linha["editora"],
                "edicao": linha["edicao"],
                "ano": int(linha["ano"]),
                "isbn": linha["isbn"],
                "status": linha["status"],
                "paginas_totais": int(linha["paginas_totais"]),
                "paginas_lidas": int(linha["paginas_lidas"]),
            })

    return livros
