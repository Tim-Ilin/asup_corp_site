from django.contrib.auth.models import User


def run():
    """
    This function create superuser after start on docker.
    Because it home project, i used hard code data.
    But for production you have to use ENVIRONMENT variables
    """
    try:
        User.objects.create_superuser('Admin', 'testtmz@gmail.com', '12345')
    except:
        pass
