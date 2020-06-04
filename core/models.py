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
    _name = models.CharField("ФИО клиента", max_length=50, blank=True)
    _phone_number = models.CharField("Номер телефона", max_length=15, blank=True)
    _email = models.EmailField("Почта", blank=True)
    _contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    _opportunity = models.FloatField(default=0)
    _short_description = models.CharField(max_length=50, blank=True)
    _description = models.TextField("Описание", blank=True)

    def updateDatabase(self,table_name,column,value,where_column,where_value):
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE %s SET %s=:value1 WHERE %s=:value2;"
        %(table_name,column,where_column),
        {"value1": value, "value2": where_value})
        conn.commit()
        conn.close()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
        self.updateDatabase("core_crmentity","_name",value,"id",self.id)

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self,value):
        self._phone_number = value
        self.updateDatabase("core_crmentity","_phone_number",value,"id",self.id)
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,value):
        self._email = value
        self.updateDatabase("core_crmentity","_email",value,"id",self.id)

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self,value):
        self._contact = value
        self.updateDatabase("core_crmentity","_contact_id",value.id,"id",self.id)
    
    @property
    def opportunity(self):
        return self._opportunity

    @opportunity.setter
    def opportunity(self,value):
        self._opportunity = value
        self.updateDatabase("core_crmentity","_opportunity",value,"id",self.id)

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self,value):
        self._short_description = value
        self.updateDatabase("core_crmentity","_short_description",value,"id",self.id)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,value):
        self._description = value
        self.updateDatabase("core_crmentity","_description",value,"id",self.id)
    
class Lead(CrmEntity):
    _title = models.CharField("Название лида", max_length=50, default="Лид №%s"%(str(id)))
    _stage_id = models.IntegerField("Стадия лида", default=1)

    def __str__(self):
        return self._title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        self._title = value
        self.updateDatabase("core_lead","_title",value,"crmentity_ptr_id",self.id)

    @property
    def stage_id(self):
        return self._stage_id

    @stage_id.setter
    def stage_id(self,value):
        self._stage_id = value
        self.updateDatabase("core_lead","_stage_id",value,"crmentity_ptr_id",self.id)

    def getStageId(self):
        return StageId.objects.filter(id=self._stage_id)[0]

class Deal(CrmEntity):
    _title = models.CharField("Название сделки", max_length=50, default="Сделка №%s"%(str(id)))
    _stage_id = models.IntegerField("Стадия сделки", default=1)
    _lead = models.ForeignKey(Lead,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self._title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        self._title = value
        self.updateDatabase("core_deal","_title",value,"crmentity_ptr_id",self.id)

    @property
    def stage_id(self):
        return self._stage_id

    @stage_id.setter
    def stage_id(self,value):
        self._stage_id = value
        self.updateDatabase("core_deal","_stage_id",value,"crmentity_ptr_id",self.id)

    def getStageId(self):
        return StageId.objects.filter(id=self._stage_id)[0]

    @property
    def lead(self):
        return self._lead

    @lead.setter
    def lead(self,value):
        self._lead = value
        self.updateDatabase("core_deal","_lead_id",value.id,"crmentity_ptr_id",self.id)

class StageContainer(models.Model):
    _entity = models.CharField("Сущность контейнера", max_length=20, blank=False, default="deal")
    _title = models.CharField("Название контейнера стадий", max_length=50, blank=False)

    def __str__(self):
        return self.title

    def updateDatabase(self,table_name,column,value,where_column,where_value):
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE %s SET %s=:value1 WHERE %s=:value2;"
        %(table_name,column,where_column),
        {"value1": value, "value2": where_value})
        conn.commit()
        conn.close()

    def getAllElements(self):
        container = StageContainer.objects.get(id=self.id)
        return StageId.objects.filter(container=container)

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self,value):
        self._entity = value
        self.updateDatabase("core_stagecontainer","_entity",value,"id",self.id)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        self._title = value
        self.updateDatabase("core_stagecontainer","_title",value,"id",self.id)

class StageId(models.Model):
    _container = models.ForeignKey(StageContainer, on_delete=models.SET_NULL, null=True)
    _name = models.CharField("Название стадии", max_length=30, blank=False, default="ti")
    _color = models.CharField("Цвет", max_length=6, default="#ffffff")

    def updateDatabase(self,table_name,column,value,where_column,where_value):
        conn = sqlite3.connect(os.path.join('db.sqlite3'))
        cursor = conn.cursor()
        cursor.execute("UPDATE %s SET %s=:value1 WHERE %s=:value2;"
        %(table_name,column,where_column),
        {"value1": value, "value2": where_value})
        conn.commit()
        conn.close()

    @property
    def container(self):
        return self._container

    @container.setter
    def container(self,value):
        self._container = value
        self.updateDatabase("core_stageid","_container_id",value.id,"id",self.id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value
        self.updateDatabase("core_stageid","_name",value,"id",self.id)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value
        self.updateDatabase("core_stageid","_color",value,"id",self.id)

    def getAllElements(self):
        if self._container._entity=="lead":
            return Lead.objects.filter(_stage_id=self.id)
        elif self._container._entity=="deal":
            return Lead.objects.filter(_stage_id=self.id)
