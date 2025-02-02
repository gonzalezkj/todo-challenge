"""Invera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from AppTareas.router import router_tareas
from AppTareas.views import TareaApiViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_tareas.urls)),
    path('api/tarea/<int:pk>/', TareaApiViewSet.update , name='update_api'),
    path('api/tarea/<int:pk>/', TareaApiViewSet.delete , name='delete_api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
