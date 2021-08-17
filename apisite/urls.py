"""apisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from rest_framework.authtoken import views as authtokenviews
from Employee import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# create a router to handle viewsets
router = routers.DefaultRouter()
router.register(r'employees/', views.EmployeeViewSet)
#router.register(r'employees/<int:pk>/', views.EmployeeDetail.as_view())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('employee/create', views.EmployeeCreate.as_view()),
    path('employee/update/<int:pk>',views.EmployeeUpdate.as_view()),
    path('employee/delete/<int:pk>', views.EmployeeDelete.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # timelimit #
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #
]
