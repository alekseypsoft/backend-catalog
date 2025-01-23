from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from catalog.models import User, Employee
from faker import Faker


class EmployeeTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.fake = Faker()
        username = 'testusera'
        password = '1234567'
        User.objects.create_user(username, "lennon@thebeatles.com", password)
        response = self.client.post(reverse('login'),
                                    data={"username": username, "password": password},
                                    format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['tokens']['access'])

    def test_can_register_and_login(self):
        username1 = 'testuser'
        password1 = '123456'
        self.client.post(reverse('register'),
                         data={"username": username1, "email": 'testuser@example.com', "password": password1},
                         format='json')
        response = self.client.post(reverse('login'),
                                    data={"username": username1, "password": password1},
                                    format='json')
        self.assertIs("access" in response.data['tokens'], True)

    def test_employee_list(self):
        url = reverse('employees-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_show_employee(self):
        employee = Employee.objects.create(first_name=self.fake.name(),
                                           last_name=self.fake.last_name(),
                                           patronymic_name=self.fake.name(),
                                           salary=50)
        url = reverse('employees-detail', args=[employee.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_employee(self):
        employee = Employee.objects.create(first_name=self.fake.name(),
                                           last_name=self.fake.last_name(),
                                           patronymic_name=self.fake.name(),
                                           salary=50)
        url = reverse('employees-detail', args=[employee.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
