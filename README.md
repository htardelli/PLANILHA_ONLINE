# PLANILHA_ONLINE

Projeto FastAPI para envio automático de dados de formulário para Google Sheets.

## Como rodar localmente

1. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
2. Baixe seu `credentials.json` no Google Cloud e coloque na raiz do projeto.
3. Execute:
    ```
    uvicorn main:app --reload
    ```
4. Acesse `http://localhost:8000/docs`

## Segurança

O arquivo `credentials.json` NÃO deve ser enviado para o GitHub.
# PLANILHA_ONLINE
