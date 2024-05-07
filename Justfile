set dotenv-load
set positional-arguments

# Django commands

serve:
  python -m uvicorn healthlink.asgi:application --reload

testall:
  python manage.py test

@test file:
  python manage.py test tests.test_$1

migration:
  python manage.py makemigrations

@migrations app:
  python manage.py makemigrations $1

migrate:
  python manage.py migrate --run-syncdb

admin:
  python manage.py createsuperuser

shell:
  python manage.py shell --no-startup

# django-extensions commands

erd:
  python manage.py graph_models -a -g -I DoctorProfile,PatientProfile,Appointment,MedicalRecord,MedicineShop -o erd.png

reset:
  python manage.py reset_db --noinput patient 

# MKDocs commands

docs:
  mkdocs serve

# Backend setup

bsetup:
  /home/ubuntu/.local/bin/poetry install && /home/ubuntu/.local/bin/poetry shell

# Frontend setup

fsetup:
  cd frontend && nvm use 18 && npm install -g @angular/cli@12.2.0 && npm install && ng serve

# Aggregate commands

run: migrate testall serve

db: migration migrate

rdb: reset db

all: bsetup fsetup run