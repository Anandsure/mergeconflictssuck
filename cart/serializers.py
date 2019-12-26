from rest_framework import serializers
from .models import File,Cat,Sub



class carttSerializer(serializers.ModelSerializer):
  class Meta():
    model = Cart
    fields = '__all__'

class cartItemtSerializer(serializers.ModelSerializer):
  class Meta():
    model = CartItem
    fields = '__all__'

