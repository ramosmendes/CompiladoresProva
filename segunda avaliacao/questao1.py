# Exemplo da gramática f)
gramatica = {
    'S': ['AB', 'BCS'],
    'A': ['aA', 'C'],
    'B': ['bbB', 'b'],
    'C': ['cC', 'λ']
}

# Imprimir gramática na tela
for variavel, producoes in gramatica.items():
    producoes_formatadas = ' | '.join(producoes)
    print(f"{variavel} -> {producoes_formatadas}")


# Eliminação de produções vazias:
def verifica_lambda_na_gramatica(gramatica):
    for producoes in gramatica.values():
        if 'λ' in producoes:
            gramatica['S'].append('B')
            gramatica['S'].append('BS')
            gramatica['A'].append('a')
            gramatica['C'].remove('λ')
            gramatica['C'].append('c')
            return "\nA gramática contém produções vazias. Hora de resolver:"
    return "\nA gramática não contém produções vazias."


resultado = verifica_lambda_na_gramatica(gramatica)
print(resultado)

# Imprimir gramática na tela
for variavel, producoes in gramatica.items():
    producoes_formatadas = ' | '.join(producoes)
    print(f"{variavel} -> {producoes_formatadas}")


# Eliminação de produções unitárias:
def verifica_unitario_na_gramatica(gramatica):
    for producoes in gramatica.values():
        if 'B' in producoes or 'C' in producoes:
            gramatica['S'].remove('B')
            gramatica['S'].append('bbB')
            gramatica['S'].append('b')
            gramatica['A'].remove('C')
            gramatica['A'].append('cC')
            gramatica['A'].append('c')
            return "\nA gramática contém produções unitárias. Hora de resolver:"
    return "\nA gramática não contém produções unitárias."


resultado = verifica_unitario_na_gramatica(gramatica)
print(resultado)

# Imprimir gramática na tela
for variavel, producoes in gramatica.items():
    producoes_formatadas = ' | '.join(producoes)
    print(f"{variavel} -> {producoes_formatadas}")

print('Simplificação completa. Hora de renomearmos as variáveis: ')


def substituir_valores_gramatica(gramatica, valor_antigo, valor_novo):
    for variavel, producoes in gramatica.items():
        for i in range(len(producoes)):
            producoes[i] = producoes[i].replace(valor_antigo, valor_novo)


# Substituir 'B' por 'X'
substituir_valores_gramatica(gramatica, 'A', 'A₂')
substituir_valores_gramatica(gramatica, 'B', 'A₃')
substituir_valores_gramatica(gramatica, 'C', 'A₄')
substituir_valores_gramatica(gramatica, 'S', 'A₁')

# Renomeamos os valores da gramática, agora é necessário renomear as chaves
# Função para renomear as chaves da gramática


def renomear_chaves_gramatica(gramatica, mapeamento_chaves):
    nova_gramatica = {}
    for variavel, producoes in gramatica.items():
        nova_variavel = mapeamento_chaves.get(variavel, variavel)
        nova_gramatica[nova_variavel] = producoes
    return nova_gramatica


# Mapear as chaves
mapeamento_chaves = {
    'S': 'A₁',
    'A': 'A₂',
    'B': 'A₃',
    'C': 'A₄'
}

# Renomear as chaves da gramática
gramatica = renomear_chaves_gramatica(gramatica, mapeamento_chaves)

# Imprimir a gramática atualizada
for variavel, producoes in gramatica.items():
    producoes_formatadas = ' | '.join(producoes)
    print(f"{variavel} -> {producoes_formatadas}")

print('\nNão temos elementos recursivos então vamos garantir que comece com terminal.')
novos_valores = ['aA₂A₃', 'aA₃', 'cA₄A₃', 'cA₃',
                 'bbA₃A₄A₁', 'bA₄A₁', 'bbA₃A₁', 'bA₁', 'bbA₃', 'b']
gramatica['A₁'].clear()

for valor in novos_valores:
    gramatica['A₁'].append(valor)

# Imprime a gramática atualizada
for variavel, producoes in gramatica.items():
    producoes_formatadas = ' | '.join(producoes)
    print(f"{variavel} -> {producoes_formatadas}")

print('FINALIZADO')
