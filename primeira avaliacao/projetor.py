import re

# Exibe uma mensagem informativa para o usuário
print("As palavras iniciadas com números, são reservadas pelo sistema.")

# Solicita que o usuário digite uma palavra e limita a entrada a no máximo 10 caracteres
entrada = input("Digite uma palavra: ")[:10]

# Expressão regular para verificar o padrão da entrada
regex = re.compile(
    r'^[^0-9][a-zA-Z0-9(){}[\]!@#$%^~;:.,><+=\-_*|&¨¬§¢£°/?ºª´`"áéíóúàèìòùâêîôûãõçÇÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕ\s]*$')

# Expressão regular para verificar caracteres inválidos na entrada
invalid_chars_regex = re.compile(r'[xyztwXYZTW]')


def verifica_expressao(entrada):
    # Lista de caracteres especiais
    special_chars = ['+', '-', '*', '/', '[', ']',
                     '{', '}', '(', ')', '!', '@', '#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    error_count = 0

    # Itera sobre cada caractere na entrada
    for i, char in enumerate(entrada):
        # Verifica se o caractere 'x', 'y', 'z', 't' ou 'w' está presente
        if char.lower() in ['x', 'y', 'z', 't', 'w']:
            # Verifica se está no início ou final da palavra
            if i == 0 or i == len(entrada) - 1:
                error_count += 1
            # Verifica se está cercado por caracteres especiais válidos
            elif entrada[i-1] in special_chars and entrada[i+1] in special_chars:
                pass
            else:
                error_count += 1

    # Verifica se houve erros na expressão
    if error_count != 0:
        print("Compilador não aceitou")
    else:
        print("Expressão numérica")


# Verifica se a entrada atende aos critérios definidos
if regex.match(entrada) and not invalid_chars_regex.search(entrada):
    # A entrada é válida
    print("Compilador aceitou.")
    print(", ".join([c for c in entrada]))  # Imprime os caracteres da entrada separados por vírgula
elif regex.match(entrada):
    # A entrada é válida, mas contém caracteres especiais que precisam ser verificados
    verifica_expressao(entrada)
else:
    # Números no início são reservados para o sistema
    print("Números no inicio são reservados para o sistema")
