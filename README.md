📋 Pré-requisitos:
Python 3.8+
MySQL

🖥️ Frontend (React)
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
Em "config.py" ajuste o objeto db_config 

4. Inicie o Servidor
python app.py

5. Iniciar o front-end:
cd frontend/
npm install
npm run dev
