from .models import Person
from strona.celery import app

@app.task
def add_person(first_name, last_name, age, bd_date):
    person = Person.objects.create(
        first_name=first_name,
        last_name=last_name,
        age=age,
        bd_date=bd_date
    )
