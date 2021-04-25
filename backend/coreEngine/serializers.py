from rest_framework import serializers

# from .models import Initiative


# get from http://www.django-rest-framework.org/api-guide/fields/#listfield
class StringListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, obj):
        return ', '.join(obj.values_list('name', flat=True))

#
# class InitiativeSerializer(serializers.ModelSerializer):
#     labels = StringListField()
#
#     class Meta:
#         model = Initiative
#         fields = '__all__'
#         use_natural_foreign_keys = True
#         use_natural_primary_keys = True


# class SampleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sample
#         fields = '__all__'
#         use_natural_foreign_keys = True
#         use_natural_primary_keys = True
#
#     @staticmethod
#     def func(obj):
#         """
#         Usage - data.append(SampleSerializer.func(obj))
#         """
#         project_data = model_to_dict(obj)
#         return project_data
