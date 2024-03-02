from sklearn.svm import LinearSVC

# Características dos compostos
composto1 = [1, 1, 1]  # Ex: Álcool etílico (S)
composto2 = [0, 0, 0]  # Ex: Hexano (N)
composto3 = [1, 0, 1]  # Ex: Glicerol (S)
composto4 = [0, 1, 0]  # Ex: Metano (N)
composto5 = [1, 1, 0]  # Ex: Ácido acético (S)
composto6 = [0, 0, 1]  # Ex: Fenol (S)

dados_treino = [composto1, composto2, composto3, composto4, composto5, composto6]
rotulos_treino = ['S', 'N', 'S', 'N', 'S', 'S']

# Criar e treinar o modelo
modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

# Testar o modelo com novos compostos
teste1 = [1, 0, 0]  # Ex: Ácido butírico
teste2 = [0, 1, 1]  # Ex: 1-butanol
teste3 = [1, 0, 1]  # Ex: Etilenoglicol

dados_teste = [teste1, teste2, teste3]

# Fazer previsões com o modelo treinado
previsoes = modelo.predict(dados_teste)

mapeamento_previsoes = {'S': 'Solúvel', 'N': 'Não Solúvel'}


# Imprimir as previsões
print("Previsões do modelo para os compostos testados:", previsoes)
for i, previsao in enumerate(previsoes):
    print(f'O composto {i+1} pode ser considerado {mapeamento_previsoes[previsao]}')
