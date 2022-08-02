from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Tareas

class TareaSerializer(ModelSerializer):

    class Meta:
        model = Tareas
        fields = ['nombre', 'contenido', 'completada', 'created']
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'contenido': instance.contenido,
            'completada': instance.completada,
            'created': instance.created,
        }

class UpdateTareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('nombre', 'contenido', 'completada')