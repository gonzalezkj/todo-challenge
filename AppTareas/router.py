from rest_framework.routers import DefaultRouter
from .views import TareaApiViewSet

router_tareas = DefaultRouter()

router_tareas.register(prefix='tarea', basename='tarea', viewset=TareaApiViewSet)