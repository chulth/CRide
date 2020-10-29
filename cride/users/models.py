'''models users.'''

# import models
'''This model heredity of abstracuser in django/templates/models '''
from django.db import models
from django.contrib.auth.models import AbstractUser

# utilities
from cride.utils.models import CRideModel

class User(CRideModel,AbstractUser):
    '''User model.
    Extend from django´s Abstrac User, change the user field
    to email nas add some extra fields.
    '''
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user is with that email already exists.'
        }
    )
    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'lastname']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easy distinguish users and performance queries'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text=(
            'Set to true when the user havevirified it s mail address'
        )
    )
