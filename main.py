from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha calculadora")

class DadosCalculo(BaseModel):
    num1: float
    num2: float
    operacao: str
    
@app.post("/calcular")
async def calcular(dados: DadosCalculo):
    n1 = dados.num1
    n2 = dados.num2
    op = dados.operacao.lower()
    resultado = 0
    
    if op == "soma": 
        resultado = n1 + n2 
    elif op == "subtracao":
        resultado = n1 - n2
    elif op == "multiplicacao":
        resultado = n1 * n2
    elif op == "divisao":
        if n2 == 0:
            return {"erro": "Não é possível dividir por zero"}
        resultado = n1 / n2
    else:
        return {"erro": "Operação inválida"}
    
    return {
        "num1": n1,
        "num2": n2,
        "operacao": op,
        "resultado": resultado
    }