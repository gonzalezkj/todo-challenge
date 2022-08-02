from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Tareas
from .serializers import TareaSerializer, UpdateTareaSerializer
from django_filters import rest_framework as filters
from rest_framework.response import Response

class TareaFilter(filters.FilterSet):
    class Meta:
        model = Tareas
        fields = {
            'id': ['exact',],
            'created': ['iexact', 'lte', 'gte'],
            'contenido': ['icontains'],
        }

class TareaApiViewSet(ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()
    filterset_class = TareaFilter

    def update(self, request, pk = None):
        Tarea = self.get_object()
        tarea_serializer = UpdateTareaSerializer(Tarea, data=request.data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return Response({
                'message': 'Tarea actualizada correctamente'
            })
        return Response({
            'message': 'Hay errores en la actualización',
        })

    def delete(request, pk = None):
        Tarea = Tareas.objects.filter(id = pk).first()
        Tarea.delete()
        return Response('Eliminada')