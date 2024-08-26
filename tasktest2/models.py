from django.db import models
from django.utils import timezone

class Shop(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    street = models.ForeignKey('Street', on_delete=models.CASCADE)
    house = models.CharField(max_length=50)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return "%s" % self.name

    def is_open(self):
        now = timezone.localtime().time()  # Получаем текущее локальное время
        return self.opening_time <= now < self.closing_time

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


    object = models.Manager


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    object = models.Manager

class Street(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

    object = models.Manager

# Create your models here.