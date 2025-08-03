from fastapi import FastAPI, Form
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = FastAPI()

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1n0hyyd2OlF5SOVKBwAK_bIckBCW-pKzp-f9kZpunQXM'  # <-- Corrija aqui!
RANGE_NAME = 'Dados!A1'  # Altere para sua aba e range

@app.post("/adicionar")
def adicionar(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...)
):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    values = [[nome, email, telefone]]
    body = {'values': values}
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
    return {"status": "sucesso", "dados": values}

