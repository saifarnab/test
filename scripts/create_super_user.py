"""
python3 manage.py runscript create_super_user
"""
from django.conf import settings
from django.contrib.auth.models import User


def run():
    if settings.STAGE != "development":
        print("create_super_user can be used only on development environment")
        return

    try:
        username = "sma"
        password = "1"
        email = "sma@upaybd.com"

        user = User.objects.create_superuser(
            username=username, password=password, email=email
        )

        if user is None:
            print("Super user not created")
        else:
            print("Super user created")

    except Exception as err:
        print("Super user not created", err)
