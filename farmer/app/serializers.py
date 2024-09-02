# farm_management_app/serializers.py
from rest_framework import serializers
from .models import Crop

class CropSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Crop
        fields = '__all__'  # This will include all fields from the Crop model
