from django.db import models

# Create your models here.
# Предполагается, что всего работает три мастера
# И у каждого мастера очередь записи к нему представлена таблицой
# from datetime import datetime
from django.utils import timezone


class FirstMaster(models.Model):
    surname = models.CharField("Фамилия", max_length=30, default="")
    name = models.CharField("Имя", max_length=30, default="")
    patronymic = models.CharField("Отчество", max_length=30, default="")
    auto_mark = models.CharField("Марка автомобиля", max_length=30, default="")
    register_date = models.DateTimeField("Время и дата записи", default=timezone.now)

    def __str__(self):
        return "Запись к 1 мастеру"

    class Meta:
        verbose_name="Запись к 1 мастеру"
        verbose_name_plural = "Записи к 1 мастеру"

class SecondMaster(models.Model):
    surname = models.CharField("Фамилия", max_length=30, default="")
    name = models.CharField("Имя", max_length=30, default="")
    patronymic = models.CharField("Отчество", max_length=30, default="")
    auto_mark = models.CharField("Марка автомобиля", max_length=30, default="")
    register_date = models.DateTimeField("Время и дата записи", default=timezone.now)

    def __str__(self):
        return "Запись к 2 мастеру"

    class Meta:
        verbose_name="Запись к 2 мастеру"
        verbose_name_plural = "Записи к 2 мастеру"


class ThirdMaster(models.Model):
    surname = models.CharField("Фамилия", max_length=30, default="")
    name = models.CharField("Имя", max_length=30, default="")
    patronymic = models.CharField("Отчество", max_length=30, default="")
    auto_mark = models.CharField("Марка автомобиля", max_length=30, default="")
    register_date = models.DateTimeField("Время и дата записи", default=timezone.now)

    def __str__(self):
        return "Запись к 3 мастеру"

    class Meta:
        verbose_name = "Запись к 3 мастеру"
        verbose_name_plural = "Записи к 3 мастеру"


