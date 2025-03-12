from rest_framework import serializers
from .models import contactUs

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactUs  # Corrected syntax
        fields = '__all__'  # Corrected syntax
