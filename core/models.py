from django.db import models
import sqlite3
import os

class Contact(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    email = models.EmailField("Почта", blank=True)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def sayHi(self):
        return print("hi everybody my name is Maxim, and this is my first day using vs code with wsl2")

class Lead(models.Model):
    name = models.CharField("ФИО клиента", max_length=50, blank=True)
    title = models.CharField("Название лида", max_length=50, default="Лид №"+str(id))
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    email = models.EmailField("Почта", blank=True)
    contact = models.ForeignKey("Contact", on_delete=models.SET_NULL, null=True)
    opportunity = models.FloatField(default=0)
    #1-RUB,2-USD,3-EURO
    opportunity_currency = models.PositiveSmallIntegerField(default=1)
    _stage_id = models.IntegerField("Стадия сделки", default=0)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.title
    
    @property
    def stage_id(self):
        return self._stage_id
    
    @stage_id.setter
    def stage_id(self,value):
        self._stage_id = value
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE core_lead SET _stage_id=:stage_id WHERE id=:id;",
        {"id": self.id, "stage_id": value})
        conn.commit()
        conn.close()