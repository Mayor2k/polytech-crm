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

class CrmEntity(models.Model):
    name = models.CharField("ФИО клиента", max_length=50, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    email = models.EmailField("Почта", blank=True)
    contact = models.ForeignKey("Contact", on_delete=models.SET_NULL, null=True)
    opportunity = models.FloatField(default=0)
    description = models.TextField("Описание", blank=True)

class Lead(CrmEntity):
    _title = models.CharField("Название лида", max_length=50, default="Лид №%s"%(str(id)))
    _stage_id = models.IntegerField("Стадия сделки", default=1)
    
    def __str__(self):
        return self._title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        self._title = value
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE core_lead SET _title=:title WHERE crmentity_ptr_id=:id;",
        {"id": self.id, "title": value})
        conn.commit()
        conn.close()
    
    @property
    def stage_id(self):
        return self._stage_id
    
    @stage_id.setter
    def stage_id(self,value):
        self._stage_id = value
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE core_lead SET _stage_id=:stage_id WHERE crmentity_ptr_id=:id;",
        {"id": self.id, "stage_id": value})
        conn.commit()
        conn.close()

    def getStageId(self):
        return StageId.objects.filter(id=self._stage_id)[0]

class StageContainer(models.Model):
    entity = models.CharField("Сущность контейнера", max_length=20, blank=False, default="deal")
    title = models.CharField("Название контейнера стадий", max_length=50, blank=False)

    def __str__(self):
        return self.title

    def getAllElements(self):
        container = StageContainer.objects.get(id=self.id) 
        return StageId.objects.filter(container=container)

class StageId(models.Model):
    container = models.ForeignKey(StageContainer, on_delete=models.SET_NULL, null=True)
    name = models.CharField("Название стадии", max_length=30, blank=False, default="ti")
    color = models.CharField("Цвет", max_length=6, default="#ffffff")

    def getAllElements(self):
        if self.container=="lead":
            return Lead.objects.filter(_stage_id=self.id)
        elif self.container=="deal":
            return Lead.objects.filter(_stage_id=self.id)
