import pandas as pd
from datetime import date, datetime
from .conexao_sheets import planilha

def adicionar(data:str = date.today().strftime("%d/%m/%Y"), tipo:str = "", valor:float = 0, metodo:str = "", info:str = "") -> str:
    linha = [data, tipo.capitalize(), round(valor, 2), metodo.capitalize(), info.capitalize()]
    planilha.append_row(linha)
    
    return f"{tipo.capitalize()} de R${valor}, pago com {metodo}, adicionado com sucesso"

#------------------------------------------------------------------------------

def formatar_valor(valor: float) -> str:
    return f"{valor:.2f}".rstrip('0').rstrip('.')

#------------------------------------------------------------------------------

def remover(data: str = "", tipo: str = "", valor: float = 0, metodo: str = "") -> str:
    elementos = [data, tipo.capitalize(), formatar_valor(valor), metodo.capitalize()]
    
    linhas = planilha.get_all_values()
    
    for i, linha in enumerate(linhas, start=1):  
        if all(str(elem) == str(linha[idx]) for idx, elem in enumerate(elementos) if elem):  
            planilha.delete_rows(i)
            return f"{tipo.capitalize()} de R${formatar_valor(valor)}, pago com {metodo}, removido com sucesso"

    return "Nenhuma transação encontrada"

#------------------------------------------------------------------------------

def filtragem_dados(mes: str = "", ano: str = "") -> list:
    mes = int(mes) if mes !=99 else 99
    
    dados = planilha.get_all_values()
    ganhos, gastos = [], []
    
    for linha in dados[1:]:
        data_str = linha[0]

        data = datetime.strptime(data_str, "%d/%m/%Y")
        if data.month == mes and data.year == int(ano) or mes == 99 and data.year == int(ano):
            if linha[1] == "Ganho":
                ganhos.append(linha)
            elif linha[1] == "Gasto":
                gastos.append(linha)
            
    return ganhos, gastos

#------------------------------------------------------------------------------

def analizar_dados(dados: list) -> list:
    if not dados:
        return []
    
    soma = 0
    porcentagem = {}
    
    map_colunas = {
        2: "Valor",
        3: "Método"
    }
    
    df = pd.DataFrame(dados)
    
    df.rename(columns=map_colunas, inplace=True)
    
    df.drop(df.columns[[0, 1, 4]], axis=1, inplace=True) 
    
    df["Valor"] = pd.to_numeric(df["Valor"], errors='coerce')  # 'coerce' converte valores inválidos para NaN
    
    soma = df["Valor"].sum()
    
    metodo_contagem = df["Método"].value_counts(normalize=True) * 100 

    porcentagem = metodo_contagem.to_dict()
    
    return [soma, porcentagem]

#------------------------------------------------------------------------------

def gerar_relatorio(mes:str = "99", ano:str = "") -> str:
    ganhos, gastos = filtragem_dados(mes, ano)

    ganhos = analizar_dados(ganhos)
    gastos = analizar_dados(gastos)
    
   # Se ambos os dados (ganhos e gastos) estiverem vazios, retornar mensagem
    if not ganhos and not gastos:
        return "Não há dados disponíveis para o período especificado."
    
    relatorio = []
    
    # Adicionando totais de ganhos, gastos e lucro, se existirem
    if ganhos:
        relatorio.append(f"Total de ganhos: R$ {ganhos[0]:.2f}")
    if gastos:
        relatorio.append(f"Total de gastos: R$ {gastos[0]:.2f}")
    
    if ganhos and gastos:
        relatorio.append(f"Lucro de R$ {ganhos[0] - gastos[0]:.2f}")
    elif ganhos:
        relatorio.append(f"Lucro de R$ {ganhos[0]:.2f}")
    else:
        relatorio.append(f"Lucro de R$ -{gastos[0]:.2f}")
    
    # Adicionando os métodos de pagamento (Ganhos) se houver dados
    if ganhos:
        relatorio.append("---------------" * 2)
        relatorio.append("Metodos de pagamento (Ganhos):")
        for metodo, porcentagem in ganhos[1].items():
            relatorio.append(f"{metodo}: {porcentagem:.2f}%")
    
    # Adicionando os métodos de pagamento (Gastos) se houver dados
    if gastos:
        relatorio.append("---------------" * 2)
        relatorio.append("Metodos de pagamento (Gastos):")
        for metodo, porcentagem in gastos[1].items():
            relatorio.append(f"{metodo}: {porcentagem:.2f}%")
    
    # Retornando o relatório completo
    return "\n".join(relatorio)
    
#------------------------------------------------------------------------------

if __name__ == "__main__":
    #print(adicionar(valor=1000, tipo="Gasto", metodo="cartão azul", info="Salário"))
    #print(remover(data = "03/03/2025" ,valor=1000.0, tipo="Ganho", metodo="pix"))
    print(gerar_relatorio(mes="03", ano="2025"))