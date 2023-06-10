def criar_lista_regras_gramatica():
    lista = ['S → AB  | CSB', 'A → aB  | C', 'B → bbB | b']
    return lista


def criar_lista_simplificado():
    lista = ['\nSimplificando:', 'Removendo variável inútil C:',
             'S → AB', 'A → aB', 'B → bbB | b']
    return lista


def criar_lista_chomsky():
    lista = ['\nTransformando em Chomsky:', 'S → AB', 'A → X₁B',
             'B → X₃B | b', 'X₁ → a', 'X₂ → b', 'X₃ → X₂X₂']
    return lista


def criar_lista_renomeado():
    lista = ['\nRenomeando as variáveis:', 'A₁ → A₂A₃', 'A₂ → A₄A₃',
             'A₃ → A₆A₃ | b', 'A₄ → a', 'A₅ → b', 'A₆ → A₅A₅']
    return lista


def criar_lista_greibach():
    lista = ['\nPassando pra Greibach:', 'A₁ → aA₃A₃', 'A₂ → aA₃',
             'A₃ → bA₅A₃ | b', 'A₄ → a', 'A₅ → b', 'A₆ → bA₅']
    return lista


# Criar lista com as regras da gramática
regras_gramatica = criar_lista_regras_gramatica()

# Criar lista com a simplificação da gramática
simplificado = criar_lista_simplificado()

# Criar lista com a transformação para a forma de Chomsky
chomsky = criar_lista_chomsky()

# Criar lista com as variáveis renomeadas
renomeado = criar_lista_renomeado()

greibach = criar_lista_greibach()

# Imprimir as regras da gramática
print('Gramática livre de contexto:')
print('\n'.join(regras_gramatica))

# Imprimir a simplificação da gramática
print('\n'.join(simplificado))

# Imprimir a transformação para a forma de Chomsky
print('\n'.join(chomsky))

# Imprimir as variáveis renomeadas
print('\n'.join(renomeado))

# Imprimir a forma de Greibach
print('\n'.join(greibach))
