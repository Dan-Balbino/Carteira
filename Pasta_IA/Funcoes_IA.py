from datetime import date
from conexao_sheets import planilha

def adicionar(data:str = date.today().strftime("%d/%m/%Y"), tipo:str = "", valor:float = 0, metodo:str = "", info:str = "") -> str:
    linha = [data, tipo.capitalize(), round(valor, 2), metodo, info.capitalize()]
    planilha.append_row(linha)
    
    return f"{tipo.capitalize()} de R${valor}, pago com {metodo}, adicionado com sucesso"


def remover(data:str = "", tipo:str = "", valor:float = 0, metodo:str = "") -> str:
    elementos = [data, tipo.capitalize(), round(valor, 2), metodo]
    
    linhas = planilha.get_all_values()
    
    for i, linha in enumerate(linhas, start=1):  # Inicia a contagem a partir de 1 (1-based index)
        if all(str(elem) == str(linha[idx]) for idx, elem in enumerate(elementos) if elem):  # Compara cada elemento com a linha
            planilha.delete_rows(i)
            return f"{tipo.capitalize()} de R${valor}, pago com {metodo}, removido com sucesso"

def relatorio():
    raise NotImplementedError
   
if __name__ == "__main__":
    #print(adicionar(valor=1000, tipo="Ganho", metodo="Pix", info="Salário"))
    #print(remover(data = "02/03/2025" ,valor=1000, tipo="Ganho", metodo="Pix"))
    relatorio()