from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=35)
    patronymic_name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Department(models.Model):
    name = models.CharField(max_length=30)
    department_head = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True, blank=True)


class DepartmentMembers(models.Model):
    name = models.CharField(max_length=30)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)


class Team(models.Model):
    name = models.CharField(max_length=30)
    team_leader = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True, blank=True)


class DepartmentTeams(models.Model):
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, blank=True)
