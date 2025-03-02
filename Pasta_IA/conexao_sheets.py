import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

arquivo = "carteira-452420-4d2baddfbf91.json"
escopos = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=arquivo, 
    scopes=escopos)

client = gspread.authorize(creds)

planilha = client.open(
    title="Carteira", 
    folder_id="1FgnHWPFb5VBJelouwZXwPmMfnw1_WiQr").get_worksheet(0)

def mostrar_planilha(planilha):
    df = pd.DataFrame(planilha.get_all_records())
    print(df)

if "__name__" == "__main__":
    # READ
    mostrar_planilha(planilha) 

    # CREATE
    planilha.update_cell(row=6, col=1, value="Marcos") # Adiciona por linha e coluna
    planilha.update_acell(label="B6", value="Costa") # Adiciona por referencia (A1, B2 etc...)
    mostrar_planilha(planilha)

    # UPDATE
    planilha.update_cell(row=5, col=1, value="Felipe")
    planilha.update_acell(label="B5", value="Silva")
    mostrar_planilha(planilha)

    # DELETE
    planilha.delete_rows(5)
    mostrar_planilha(planilha)