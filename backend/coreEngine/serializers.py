from rest_framework import serializers

from .models import Initiative

class InitiativeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Initiative
		fields = [field.name for field in Initiative._meta.fields]