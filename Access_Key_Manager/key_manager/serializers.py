from rest_framework import serializers
from .models import Accesskey


class AccesskeySerializer(serializers.ModelSerializer):

    class Meta:
        model = Accesskey
        fields = ['key', 'status', 'date_procured', 'expiry_date']