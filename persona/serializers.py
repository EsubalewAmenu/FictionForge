from rest_framework import serializers
from .models import Persona, Query

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
