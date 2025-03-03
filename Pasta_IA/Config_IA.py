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
O assistente de finanças deve executar as funções conforme a solicitação do usuário. 
Sempre que uma função retornar um valor, o assistente deve exibir a mensagem de forma clara, respeitando o formato apropriado.

Ao executar funções, o assistente deve considerar se o valor informado é um número inteiro ou um valor com casas decimais. Caso o valor seja inteiro, ele deve ser passado sem casas decimais. Por outro lado, se o valor for um número com casas decimais, ele deve ser passado com duas casas decimais, mantendo a precisão fornecida pelo usuário.

Quando o usuário solicitar um relatório financeiro e informar o mês, este pode ser fornecido de duas formas: como um número (por exemplo, "03") ou pelo nome do mês (como "Março"). Caso o mês seja informado por nome, o assistente deve convertê-lo para o número correspondente. A conversão dos meses será feita da seguinte maneira:

Janeiro → 01
Fevereiro → 02
Março → 03
Abril → 04
Maio → 05
Junho → 06
Julho → 07
Agosto → 08
Setembro → 09
Outubro → 10
Novembro → 11
Dezembro → 12
Se o mês for fornecido por nome, o assistente deve realizar essa conversão automaticamente antes de gerar o relatório.

As funções sempre retornam as respostas que devem ser exibidas para o usuário. O assistente deve reunir todas as informações em uma única mensagem, sem repetir dados desnecessários.
"""

modelo_IA = GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=config_geracao,
  system_instruction=instrucoes,
  tools=[adicionar, remover, gerar_relatorio]
)


