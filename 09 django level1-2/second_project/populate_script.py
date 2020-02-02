import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker


fakergen = Faker()
def populate_user(num=5):

    for _ in range(num):
        name = fakergen.name().split(' ')
        lastname, firstname = ' '.join(name[:-1]), name[-1]
        email = fakergen.email()

        User.objects.get_or_create(lastname=lastname, firstname=firstname, email=email)

if __name__ == "__main__":
    
    populate_user(num=20)
    print("Populate User Complete!")