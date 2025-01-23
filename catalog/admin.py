from django.contrib import admin

from .models import (
    Employee, Department, DepartmentMembers, Team, DepartmentTeams)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'patronymic_name', 'salary']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'department_head']


@admin.register(DepartmentMembers)
class DepartmentMembersAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee', 'department']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'team_leader']


@admin.register(DepartmentTeams)
class DepartmentTeamsAdmin(admin.ModelAdmin):
    list_display = ['department', 'team']
