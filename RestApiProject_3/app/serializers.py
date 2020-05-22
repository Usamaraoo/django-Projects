from rest_framework import serializers

from app.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name','skills','about_you']


