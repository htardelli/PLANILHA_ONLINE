from fastapi import FastAPI, Form
from google.oauth2 import service_account
from googleapiclient.discovery import build
from typing import Optional

app = FastAPI()

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1n0hyyd2OlF5SOVKBwAK_bIckBCW-pKzp-f9kZpunQXM'
RANGE_NAME = 'Alertas!A1'  # Nome exato da aba

@app.post("/alerta_viagem")
def alerta_viagem(
    programa: str = Form(...),
    origem: str = Form(...),
    destino: str = Form(...),
    data_ida: str = Form(...),
    milhas_ida: str = Form(...),
    data_volta: str = Form(...),
    milhas_volta: str = Form(...),
    taxa_emb_ida: Optional[str] = Form(None),
    taxa_emb_volta: Optional[str] = Form(None),
    observacoes: Optional[str] = Form(''),
    alerta: Optional[str] = Form(''),
    link_emissao: Optional[str] = Form(''),
    texto_completo: Optional[str] = Form('')
):
    # Garante que os campos opcionais não fiquem como None
    taxa_emb_ida = taxa_emb_ida or ''
    taxa_emb_volta = taxa_emb_volta or ''
    observacoes = observacoes or ''
    alerta = alerta or ''
    link_emissao = link_emissao or ''
    texto_completo = texto_completo or ''

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    values = [[programa, origem, destino, data_ida, milhas_ida, data_volta, milhas_volta,
               taxa_emb_ida, taxa_emb_volta, observacoes, alerta, link_emissao, texto_completo]]
    body = {'values': values}
    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
    return {"status": "sucesso", "dados": values}
