from django.db import models


class Register(models.Model):
    
    username = models.CharField(
        max_length=100,
        primary_key=True
        )
    email = models.EmailField(
        max_length=100
        )
    password = models.CharField(
        max_length=15
        )
    otp = models.CharField(
        max_length=6,
          blank=True,
            null=True
        )
    class Meta:
        db_table = "register"
class LOTP(models.Model):

    otpL = models.CharField(
        max_length=4,
        blank=True,
        null=True
        )
    id = models.BigAutoField(
        primary_key=True
    )
    class Meta:
        db_table="LOTP"


