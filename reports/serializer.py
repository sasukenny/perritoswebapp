from rest_framework import serializers

from reports.models import Reportes




class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportes
        fields = '__all__'
        