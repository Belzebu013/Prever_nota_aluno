#imports
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import joblib

# Instancia FastApi
app = FastAPI()

# Classe com os dados do request para API
class request_body(BaseModel):
    horas_estudo : float

# Carregar modelo para realizar a predição
modelo_pontuacao = joblib.load('./modelo_regressao.pkl')

# Função para realizar a prediçã
@app.post('/predict')
def predict(data : request_body):
    input_feature = [[data.horas_estudo]]
    y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)
    return {'pontuacao_teste': y_pred.tolist()}