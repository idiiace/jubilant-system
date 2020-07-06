from rest_framework import serializers
from products.models import category,product




class productSerializer(serializers.ModelSerializer):

	class Meta:
		model=product
		fields="__all__"

class categorySerializer(serializers.ModelSerializer):

	class Meta:
		model=category
		fields="__all__"