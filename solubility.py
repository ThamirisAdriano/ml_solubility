from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Características dos compostos
# Polaridade, Tamanho da cadeia carbônica, Presença de grupo funcional hidroxila
composto1 = [1, 1, 1]  # Ex: Álcool etílico (S)
composto2 = [0, 0, 0]  # Ex: Hexano (N)
composto3 = [1, 0, 1]  # Ex: Glicerol (S)
composto4 = [0, 1, 0]  # Ex: Metano (N)
composto5 = [1, 1, 0]  # Ex: Ácido acético (S)
composto6 = [0, 0, 1]  # Ex: Fenol (S)

dados_treino = [composto1, composto2, composto3, composto4, composto5, composto6]
rotulos_treino = ['S', 'N', 'S', 'N', 'S', 'S']  # 'S' = solúvel, 'N' = não solúvel

# Criar e treinar o modelo
modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

# Testar o modelo com novos compostos
teste1 = [1, 0, 0]  # Ex: Ácido butírico (prevê se é solúvel)
teste2 = [0, 1, 1]  # Ex: 1-butanol (prevê se é solúvel)
teste3 = [1, 0, 1]  # Ex: Etilenoglicol (prevê se é solúvel)

dados_teste = [teste1, teste2, teste3]
rotulos_teste = ['S', 'S', 'S']  # Todos são previstos como solúveis

previsoes = modelo.predict(dados_teste)

# Avaliar a precisão do modelo
taxa_acerto = accuracy_score(rotulos_teste, previsoes)
print("Taxa de acerto: %.2f%%" % (taxa_acerto * 100))
