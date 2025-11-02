
from django.core.exceptions import ValidationError


def validate_penulis(value):
    user_dont_post = ['admin','operator','teknisi']
    
    if value in user_dont_post:
        raise ValidationError(f'{value} mah montong ngupload')

def validate_tag(value):
    if len(value) <4 :
        raise ValidationError('karakterna kuranng ti 5 bambangnnnnn')