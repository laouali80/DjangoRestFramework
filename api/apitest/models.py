from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

# def validate_email(value):
    
#     email = User.objects.filter(email=value)
#     if email:
#         print('exist')
#         raise ValidationError('This email is already used! Please try another one.')
#     else:
#         return value

# validators=[validate_email]

class User(models.Model):
    username = models.CharField(max_length=56)
    email = models.EmailField(unique=True)
    follower = models.IntegerField()
    following = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username.title()