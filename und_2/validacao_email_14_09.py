import re

regex = r"^[A-Za-z0-9_%+-]+(\.[A-Za-z0-9_%+-]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$"

def motivo(email):
    if email.count("@") == 0:
        return "não tem o símbolo @"
    if email.count("@") > 1:
        return "tem mais de um @"
    usuario, dominio = email.split("@")
    if usuario == "":
        return "não tem nada antes do @"
    if usuario.startswith("."):
        return "o usuário começa com ponto"
    if usuario.endswith("."):
        return "tem um ponto logo antes do @"
    if ".." in email:
        return "tem dois pontos seguidos"
    if "." not in dominio:
        return "o domínio não tem .com, .br, etc"
    for parte in dominio.split("."):
        if parte.startswith("-") or parte.endswith("-"):
            return "a parte '" + parte + "' do domínio começa ou termina com hífen"
    return "o formato não bate com o padrão de e-mail"

validos = []
invalidos = []

for i in range(5):
    email = input("Digite o e-mail " + str(i + 1) + ": ").strip()
    if re.match(regex, email):
        validos.append(email)
    else:
        invalidos.append(email)

print("\n--- VÁLIDOS ---")
for email in validos:
    print(email)

print("\n--- INVÁLIDOS ---")
for email in invalidos:
    print(email, "->", motivo(email))
