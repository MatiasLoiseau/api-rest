#Para desactivar es solo el comando "deactivate"
source env/bin/activate
python manage.py migrate
python manage.py runserver
