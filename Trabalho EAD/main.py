from usuarios import (
    cadastrar_usuario,
    editar_usuario,
    excluir_usuario,
    fazer_login,
    listar_usuarios,
)
from livros import (
    cadastrar_livro,
    editar_livro,
    remover_livro,
    listar_livros,
)
from relatorios import (
    gerar_matriz_relatorio,
    imprimir_matriz_relatorio,
    contar_livros_por_status,
)
from persistencia import (
    salvar_usuarios,
    carregar_usuarios,
    salvar_livros,
    carregar_livros,
)


def menu_inicial():
    print("=== BookTrack - Sistema de Biblioteca Pessoal ===")
    print("1. Fazer login")
    print("2. Cadastrar novo usuário")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()


def menu_principal(usuario_logado):
    print(f"\n=== Olá, {usuario_logado['nome']}! O que deseja fazer? ===")
    print("--- Usuários ---")
    print("1. Editar meu cadastro")
    print("2. Excluir minha conta")
    print("3. Listar usuários")
    print("--- Livros ---")
    print("4. Cadastrar livro")
    print("5. Editar livro")
    print("6. Remover livro")
    print("7. Listar livros")
    print("8. Relatório geral de livros")
    print("--- Sessão ---")
    print("9. Logout")
    print("0. Sair do sistema")
    return input("Escolha uma opção: ").strip()


def fluxo_cadastrar_usuario(usuarios):
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome completo: ").strip()
    username = input("Username: ").strip()
    senha = input("Senha: ").strip()
    nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    sucesso = cadastrar_usuario(usuarios, nome, username, senha, nascimento)
    if sucesso:
        salvar_usuarios(usuarios)
        print("Usuário cadastrado com sucesso!\n")
    else:
        print("Já existe um usuário com esse username. Tente outro.\n")


def fluxo_editar_usuario(usuarios, usuario_logado):
    print("\n--- Editar Cadastro (deixe em branco pra não alterar) ---")
    novo_nome = input("Novo nome: ").strip() or None
    nova_senha = input("Nova senha: ").strip() or None
    novo_nascimento = input("Nova data de nascimento: ").strip() or None

    editar_usuario(usuarios, usuario_logado["username"], novo_nome, nova_senha, novo_nascimento)

    # atualiza o dicionário que está "logado" na sessão atual também
    if novo_nome:
        usuario_logado["nome"] = novo_nome
    if nova_senha:
        usuario_logado["senha"] = nova_senha
    if novo_nascimento:
        usuario_logado["nascimento"] = novo_nascimento

    salvar_usuarios(usuarios)
    print("Dados atualizados!\n")


def fluxo_cadastrar_livro(livros):
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    editora = input("Editora: ").strip()
    edicao = input("Edição: ").strip()

    try:
        ano = int(input("Ano: ").strip())
        paginas_totais = int(input("Páginas totais: ").strip())
        paginas_lidas = int(input("Páginas já lidas (0 se ainda não começou): ").strip() or 0)
    except ValueError:
        print("Ano e páginas precisam ser números. Cadastro cancelado.\n")
        return

    isbn = input("ISBN: ").strip()
    status = input("Status (Quero ler / Lendo / Lido): ").strip()

    sucesso = cadastrar_livro(livros, titulo, autor, editora, edicao, ano, isbn, status, paginas_totais, paginas_lidas)
    if sucesso:
        salvar_livros(livros)
        print("Livro cadastrado com sucesso!\n")
    else:
        print("Já existe um livro com esse ISBN.\n")


def fluxo_editar_livro(livros):
    print("\n--- Editar Livro (deixe em branco pra não alterar) ---")
    isbn = input("ISBN do livro que deseja editar: ").strip()

    novo_status = input("Novo status: ").strip() or None
    novas_paginas_lidas = input("Novas páginas lidas: ").strip()
    novas_paginas_lidas = int(novas_paginas_lidas) if novas_paginas_lidas else None

    sucesso = editar_livro(livros, isbn, status=novo_status, paginas_lidas=novas_paginas_lidas)
    if sucesso:
        salvar_livros(livros)
        print("Livro atualizado!\n")
    else:
        print("Não foi encontrado nenhum livro com esse ISBN.\n")


def main():
    usuarios = carregar_usuarios()   # vetor de usuários, carregado do arquivo usuarios.csv
    livros = carregar_livros()       # vetor de livros, carregado do arquivo livros.csv
    usuario_logado = None

    while True:
        if usuario_logado is None:
            opcao = menu_inicial()

            if opcao == "1":
                username = input("Username: ").strip()
                senha = input("Senha: ").strip()
                usuario_logado = fazer_login(usuarios, username, senha)
                if usuario_logado is None:
                    print("Username ou senha incorretos.\n")
                else:
                    print(f"Login realizado! Bem-vindo(a), {usuario_logado['nome']}.\n")

            elif opcao == "2":
                fluxo_cadastrar_usuario(usuarios)

            elif opcao == "0":
                print("Até logo!")
                break

            else:
                print("Opção inválida.\n")

        else:
            opcao = menu_principal(usuario_logado)

            if opcao == "1":
                fluxo_editar_usuario(usuarios, usuario_logado)

            elif opcao == "2":
                excluir_usuario(usuarios, usuario_logado["username"])
                salvar_usuarios(usuarios)
                print("Conta excluída. Você será desconectado.\n")
                usuario_logado = None

            elif opcao == "3":
                listar_usuarios(usuarios)

            elif opcao == "4":
                fluxo_cadastrar_livro(livros)

            elif opcao == "5":
                fluxo_editar_livro(livros)

            elif opcao == "6":
                isbn = input("ISBN do livro que deseja remover: ").strip()
                if remover_livro(livros, isbn):
                    salvar_livros(livros)
                    print("Livro removido!\n")
                else:
                    print("Nenhum livro encontrado com esse ISBN.\n")

            elif opcao == "7":
                listar_livros(livros)

            elif opcao == "8":
                resumo = contar_livros_por_status(livros)
                print("\nResumo por status:", resumo if resumo else "sem livros cadastrados")
                matriz = gerar_matriz_relatorio(livros)
                imprimir_matriz_relatorio(matriz)

            elif opcao == "9":
                print("Logout realizado.\n")
                usuario_logado = None

            elif opcao == "0":
                print("Até logo!")
                break

            else:
                print("Opção inválida.\n")


if __name__ == "__main__":
    main()