# ProjetoBB — versão sem banco de dados

## Estrutura principal
- Flask + Flask-WTF + Flask-Mail
- Formulário de inscrição validado
- Nenhum banco de dados ou ORM é usado.

## Como executar
1. Crie/ative um ambiente virtual.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. (Opcional) Configure as variáveis SMTP copiando `.env.example` para `.env`.
4. Execute:

```bash
python run.py
```

## Importante
Os dados do formulário são usados somente durante a requisição e não são salvos. A confirmação por e-mail depende de uma configuração SMTP válida. Sem essa configuração, o sistema exibirá uma mensagem de erro e não concluirá a inscrição.
