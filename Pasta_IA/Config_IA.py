from google.generativeai import GenerativeModel
from .Funcoes_IA import *

# Cria o modelo
config_geracao = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

instrucoes = """
Você é um assitente de finanças. Seu trabalho é executar as funções de acordo com a solicitação do usuário.
Você deve exibir as mensagens retornadas pelas funções, modificando apenas quando mais de uma operação for realizada.
Coloque casas decimais apenas se o valor informado pelo usuário for um valor com casas decimais, caso contrario, coloque apenas o valor inteiro.

"""

modelo_IA = GenerativeModel(
  model_name="gemini-2.0-flash-001",
  generation_config=config_geracao,
  system_instruction=instrucoes,
  tools=[adicionar, remover]
)


