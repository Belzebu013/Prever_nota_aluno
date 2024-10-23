# API Modelo de Regressão - Previsão de Pontuação

Esta API utiliza um modelo de regressão para prever a pontuação de um teste com base no número de horas de estudo fornecidas. A API foi construída com FastAPI e utiliza Uvicorn como servidor.

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter o seguinte instalado:

- **Python 3.7+**
- **pip** (gerenciador de pacotes do Python)
- O modelo treinado `modelo_regressao.pkl` na raiz do projeto

## Instalação

1. **Clone o repositório**:
   
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   
## Executando a API

Para rodar o servidor da API com Uvicorn, execute o seguinte comando:

    uvicorn api_modelo_regressao:app --reload

## Acessando a API

Após executar o comando, o servidor estará rodando localmente. Acesse a documentação interativa da API no seguinte endereço:

      http://127.0.0.1:8000/docs

## Exemplo de Requisição

Aqui está um exemplo de como fazer uma requisição `POST` para a API:

    curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"horas_estudo": 5.0}'

### Resposta esperada:

    {
      "pontuacao_teste": 82
    }

