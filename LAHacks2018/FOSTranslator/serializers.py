from rest_framework import serializers
from FOSTranslator.models import Idiom

class FOSTranslatorSerializer(serializers.Serializer):
    idiom = serializers.CharField(max_length = 400)
    definition = serializers.CharField(max_length = 1000)

    def create(self, validated_data):
        """
        Create and return a new `Idiom` instance, given the validated data.
        """
        return Idiom.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Idiom` instance, given the validated data.
        """
        instance.idiom = validated_data.get('idiom', instance.idiom)
        instance.definition = validated_data.get('definiton', instance.definiton)
        instance.save()
        return instance
