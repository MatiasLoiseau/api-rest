#Para desactivar es solo el comando "deactivate"
source env/bin/activate
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
