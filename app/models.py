# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class classroom(models.Model):
    class_name = models.CharField(max_length = 30)
    class_price = models.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)

class Student(models.Model):
    student_name = models.CharField(max_length = 30)
    days_attended = models.IntegerField(default = 0)
    days_absent = models.IntegerField(default = 0)
    current_credit = models.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)
    student_class = models.CharField(max_length = 30)

    def __str__(self):
        return self.student_name
    #student_class = models.ForeignKey(classroom, on_delete = models.CASCADE)




