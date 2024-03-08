## Dependências

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- scikit-learn

Você pode instalar todas as dependências necessárias utilizando o seguinte comando:

```bash
pip install scikit-learn

Estrutura do Projeto
O projeto consiste em treinar um modelo de SVM para prever a solubilidade de compostos químicos baseados em 3 características distintas. Os compostos são representados por vetores de três dimensões, onde cada dimensão corresponde a uma propriedade específica.

Dados
Os dados são divididos em dois conjuntos:

Dados de Treino: Utilizados para treinar o modelo.
Dados de Teste: Utilizados para avaliar a performance do modelo.
Modelo
O modelo utilizado é o LinearSVC do scikit-learn, que representa uma versão do SVM com kernel linear.

Execução
Para executar o projeto, siga os passos abaixo:

Prepare os dados de treino e teste conforme especificado no script.
Treine o modelo utilizando os dados de treino.
Avalie o modelo utilizando os dados de teste e calcule a taxa de acerto.
