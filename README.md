📋 Pré-requisitos
Python 3.8+

MySQL/MariaDB

Node.js (para o frontend)

🔧 Backend (Python/Flask)

1. Configure o Banco de Dados
# Importe o arquivo SQL (mesmo do projeto anterior)
mysql -u seu_usuario -p < database.sql

2. Instale as Dependências
# Crie e ative um virtualenv (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale os requisitos
pip install -r requirements.txt

3. Configure as Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto:

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
SECRET_KEY=sua_chave_secreta

4. Inicie o Servidor
flask run --host=0.0.0.0 --port=5000

5. Iniciar o front-end:
cd frontend/
npm install
npm run dev