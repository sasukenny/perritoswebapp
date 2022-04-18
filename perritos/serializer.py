from rest_framework import serializers
from .models import Perrito


class PerritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perrito
        fields = '__all__'
        
       

def PerritosSerializerParse(data):
    return {
        name : data.get('name'),
        picture : data.get('picture'),
        birth : data.get('birth'),
        gender : data.get('gender'),
        race : data.get('race'),
        owner : int(data.get('owner')),
    }
    