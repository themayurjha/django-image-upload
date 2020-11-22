from rest_framework import serializers
from .models import Category, Images


class ImageSerializer(serializers.ModelSerializer):


    class Meta:
        Model = Images
        fields = '__all__'

    def validate(self, attrs):
        img = attrs.get('image', None)
        cat = attrs.get('category', None)

        if img is None:
            raise serializers.ValidationError(
                'image cannot be blank'
            )

        if cat is None:
            raise serializers.ValidationError(
                'category cannot be none'
            )
    def create(self, validated_data):
        return Images.objects.create(validated_data)