from django.db import models


class Resume(models.Model):
    title = models.CharField(max_length=255,blank=True)
    first_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255,blank=True)
    surname = models.CharField(max_length=255,blank=True)
    born_date = models.CharField(max_length=255,blank=True)
    email = models.CharField(max_length=255,blank=True)
    skills = models.CharField(max_length=255,blank=True)
    pro_exp = models.CharField(max_length=255,blank=True)
    education = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.title}"


class Vacancy(models.Model):
    vacancy_name = models.CharField(max_length=255,blank=True)
    company_name = models.CharField(max_length=255,blank=True)
    salary = models.PositiveIntegerField(blank=True)
    required_skills = models.CharField(max_length=255,blank=True)
    responsibilities = models.CharField(max_length=255,blank=True)
    adress = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.vacancy_name}"