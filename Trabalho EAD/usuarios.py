def buscar_usuario_por_username(usuarios, username):
    for usuario in usuarios:
        if usuario["username"] == username:
            return usuario
    return None


def cadastrar_usuario(usuarios, nome, username, senha, nascimento):
    if buscar_usuario_por_username(usuarios, username) is not None:
        return False

    novo_usuario = {
        "nome": nome,
        "username": username,
        "senha": senha,
        "nascimento": nascimento,
    }
    usuarios.append(novo_usuario)
    return True


def editar_usuario(usuarios, username, novo_nome=None, nova_senha=None, novo_nascimento=None):
    usuario = buscar_usuario_por_username(usuarios, username)
    if usuario is None:
        return False

    if novo_nome:
        usuario["nome"] = novo_nome
    if nova_senha:
        usuario["senha"] = nova_senha
    if novo_nascimento:
        usuario["nascimento"] = novo_nascimento

    return True


def excluir_usuario(usuarios, username):
    usuario = buscar_usuario_por_username(usuarios, username)
    if usuario is None:
        return False

    usuarios.remove(usuario)
    return True


def fazer_login(usuarios, username, senha):
    usuario = buscar_usuario_por_username(usuarios, username)

    if usuario is None:
        return None

    if usuario["senha"] != senha:
        return None

    return usuario


def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return

    print("\n--- Lista de Usuários ---")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['nome']} | Username: {usuario['username']} | Nascimento: {usuario['nascimento']}")
    print("-------------------------\n")