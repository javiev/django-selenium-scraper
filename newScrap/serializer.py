from rest_framework import serializers
from .models import ScrapedData


class ScrapedDataSerializer(serializers.ModelSerializer):
    """
    Serializer for the ScrapedData model.
    This serializer will include all fields of the model in the serialization.
    """

    class Meta:
        model = ScrapedData
        fields = '__all__'
