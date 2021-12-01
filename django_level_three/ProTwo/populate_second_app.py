import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')


import django
django.setup()

## FAKE POPULATE DATA


from faker import Faker
import random
fakegen = Faker()
from second_app.models import User

def populate(N=5):
    
    for entry in range(N):
    
        fake_first_name = fakegen.first_name
        fake_last_name = fakegen.last_name
        fake_email = fakegen.email()

        #NEW ENTRY

        user = User.objects.get_or_create(first_name = fake_first_name,
                                          last_name = fake_last_name,
                                          user_mail= fake_email)[0]


if __name__ == "__main__":

    print('populating script')
    populate(20)
    print("population complete")