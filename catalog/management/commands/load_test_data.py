from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Employee, Department, DepartmentMembers, Team, DepartmentTeams
from faker import Faker


class Command(BaseCommand):
    help = "Добавление тестовых данных в базу данных"

    def handle(self, *args, **options):
        new_group, created = Group.objects.get_or_create(name='employee')
        content_type = ContentType.objects.get_for_model(Employee)
        permission1 = Permission.objects.get(content_type=content_type, codename='add_employee')
        permission2 = Permission.objects.get(content_type=content_type, codename='change_employee')
        permission3 = Permission.objects.get(content_type=content_type, codename='delete_employee')
        permission4 = Permission.objects.get(content_type=content_type, codename='view_employee')

        new_group.permissions.add(permission1)
        new_group.permissions.add(permission2)
        new_group.permissions.add(permission3)
        new_group.permissions.add(permission4)

        fake = Faker()
        employee = Employee(first_name=fake.name(),
                            last_name=fake.last_name(),
                            patronymic_name=fake.last_name(),
                            salary=50)
        employee.save()
        department = Department(
            name=fake.name(),
            department_head=employee)
        department.save()
        department_members = DepartmentMembers(
            name=fake.company(),
            employee=employee,
            department=department)
        department_members.save()
        team = Team(
            name=fake.company(),
            team_leader=employee)
        team.save()
        department_team = DepartmentTeams(team=team, department=department)
        department_team.save()



        self.stdout.write(
            self.style.SUCCESS('Данные успешно вставлены')
        )
