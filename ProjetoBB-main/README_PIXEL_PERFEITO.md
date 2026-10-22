# ProjetoBB — versão corrigida

## Estrutura principal

- Flask + SQLAlchemy + Flask-WTF + Flask-Mail
- Menu lateral multinível em um único arquivo JavaScript
- Home baseada nas capturas fornecidas do Concursos BB
- Formulário de inscrição preservado

## Como executar

1. Crie/ative um ambiente virtual.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute:

```bash
python run.py
```

O banco SQLite será criado em `instance/app.db` automaticamente.

## Observações

O arquivo `.env`, o banco local e o ambiente virtual não foram incluídos no pacote por conterem configuração local.


## Envio de e-mail de confirmação

O cadastro envia uma confirmação com o botão **CLIQUE AQUI PARA ACOMPANHAR SUA INSCRIÇÃO**. O botão usa um token assinado, válido por 30 dias, para mostrar apenas o status do cadastro.

1. Instale as dependências: `pip install -r requirements.txt`.
2. Copie `.env.example` para `.env` e preencha as variáveis SMTP.
3. No Gmail, ative a verificação em duas etapas e crie uma **senha de app**; use essa senha em `MAIL_PASSWORD` (não use a senha normal da conta).
4. Execute `python run.py`.

O arquivo `.env` não deve ser enviado ao Git nem compartilhado. O e-mail identifica o site como projeto acadêmico e não oficial. Se SMTP não estiver configurado, o cadastro ainda pode ser salvo, mas a mensagem não será enviada; confira o terminal/logs.
