from django.db import models

class Contact(models.Model):
    first_name = models.CharField("Имя",max_length=30)
    last_name = models.CharField("Фамилия",max_length=30)
    phone_number = models.CharField("Номер телефона", max_length=15,blank=True)
    email = models.EmailField("Почта",blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name
