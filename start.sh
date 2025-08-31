#!/bin/bash

# Esperar o banco de dados ficar pronto (se houver)
# while ! nc -z $DB_HOST $DB_PORT; do
#   sleep 0.1
# done

echo "Iniciando a aplicação..."

# Executar migrações (se houver)
# python manage.py migrate

# Coletar arquivos estáticos (se houver)
# python manage.py collectstatic --noinput

# Iniciar a aplicação
exec gunicorn --bind 0.0.0.0:5000 app:app --workers 2 --threads 2 --timeout 120