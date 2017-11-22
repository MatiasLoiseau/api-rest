#Para desactivar es solo el comando "deactivate"
source env/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
