from django.db import models

class VacationModel(models.Model):
    service = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, null=True)
    job = models.CharField(max_length=1000, default="None")
    location = models.CharField(max_length=100)
    min_salary = models.PositiveIntegerField(null=True)
    max_salary = models.PositiveIntegerField(null=True)
    currency = models.CharField(max_length=5, null=True)
    min_experience = models.PositiveIntegerField(null=True)
    max_experience = models.PositiveIntegerField(null=True)
    work_time = models.CharField(max_length=100)