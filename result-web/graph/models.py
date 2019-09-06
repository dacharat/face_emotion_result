from django.contrib.postgres.fields import ArrayField
from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    face = models.CharField(max_length=200)
    emotion_detail = ArrayField(models.TextField())

    def __str__(self):
        return self.face

def array_field_default():
    return {'a': 0}

class TestPerson(models.Model):
    face = models.CharField(max_length=200)
    face_image = ArrayField(models.TextField())
    face_encoding = ArrayField(models.TextField(), default=array_field_default)

    class Meta:
        managed = True
        db_table = 'test_person'


class Record(models.Model):
    person = models.ForeignKey(TestPerson, on_delete=models.CASCADE)
    record_name = models.CharField(max_length=200)
    emotion_detail = ArrayField(models.TextField())
    class Meta:
        managed = True
        db_table = 'record'
