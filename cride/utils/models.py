'''django models utilities'''

# Django
from django.db import models


class CRideModel(models.Model):
    '''
    Acts as an abstact class from which every other
    model
    '''
    created = models.DateTimeField(
        'create at',
        auto_now_add=True,
        help_text='Date time on wichh the object was create.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        '''Meta option.'''
        abstract = True
        get_lastest_by = 'created'
        ordering = ['-created','-modified']
