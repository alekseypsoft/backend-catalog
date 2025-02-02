"""
URL configuration for catalog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from catalog import views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from catalog.views import EmployeeViewSet

router = DefaultRouter()
router.APIRootView.__doc__ = "Добро пожаловать, в программу каталога!"
router.APIRootView.__name__ = "BACKEND"
router.register('employees', EmployeeViewSet, basename='employees')
urlpatterns = [
    path("", views.dashboard, name="index"),
    path('admin/', admin.site.urls),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

"""router.register('departments', DepartmentViewSet, basename='departments')
router.register('department_members', DepartmentMembersViewSet, basename='department_members')
router.register('teams', TeamViewSet, basename='teams')
router.register('department_teams', DepartmentTeamsViewSet, basename='department_teams')
"""