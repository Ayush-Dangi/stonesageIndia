from django.db import models
# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phoneNumber = models.CharField(max_length=10, verbose_name="Phone Number" )
    message = models.TextField(max_length=500, verbose_name="Message")
    date_created = models.DateTimeField(verbose_name="TimeStamp", auto_now_add="True")

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"