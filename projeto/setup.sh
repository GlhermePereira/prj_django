#!/bin/bash

# 1. Verifica se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python não encontrado. Instale o Python antes de prosseguir."
    exit 1
fi

# 2. Cria um ambiente virtual (se ainda não existir)
if [ ! -d "venv" ]; then
    echo "Criando o ambiente virtual..."
    python3 -m venv venv
else
    echo "Ambiente virtual já existe."
fi

# 3. Ativa o ambiente virtual
echo "Ativando o ambiente virtual..."
source venv/bin/activate

# 4. Instala as dependências
if [ -f "requirements.txt" ]; then
    echo "Instalando as dependências..."
    pip install -r requirements.txt
else
    echo "Arquivo requirements.txt não encontrado!"
    exit 1
fi

# 5. Executa o projeto (ajuste o comando conforme o seu projeto)
echo "Executando o projeto..."
python manage.py  # Ajuste para o seu arquivo de entrada

# 6. Desativa o ambiente virtual após execução
deactivate
echo "Ambiente virtual desativado. Finalizado!"

