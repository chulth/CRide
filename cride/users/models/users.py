'''models users.'''

# import models
'''This model heredity of abstracuser in django/templates/models '''
# utilities
from cride.utils.models import CRideModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator




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
    phone_regex = RegexValidator(
        regex= r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the  format: +99999999999. up to 15 digitis allowed.'
    )
    phone_number = models.CharField(validators =[phone_regex], max_length=17, blank=True)

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

    def __str__(self):
        '''Return username.'''
        return  self.username

    def get_short_name(self):
        '''Return username.'''
        return self.username
