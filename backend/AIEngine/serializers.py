from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'
		use_natural_foreign_keys=True
		use_natural_primary_keys=True