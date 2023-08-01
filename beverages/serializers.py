from rest_framework import routers, serializers, viewsets
from .models import Beverages
 
class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverages
        fields = ["id", "name", "description"]