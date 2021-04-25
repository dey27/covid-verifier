from rest_framework import serializers
from django.forms.models import model_to_dict

from .models import Posts, Votes


# get from http://www.django-rest-framework.org/api-guide/fields/#listfield
class StringListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, obj):
        return ', '.join(obj.values_list('name', flat=True))


class PostsSerializer(serializers.ModelSerializer):
    labels = StringListField()

    class Meta:
        model = Posts
        fields = '__all__'
        use_natural_foreign_keys = True
        use_natural_primary_keys = True

    @staticmethod
    def serialize_with_votes(obj):
        """
        """
        posts_data = model_to_dict(obj)
        posts_data['labels'] = [obj.name for obj in posts_data['labels']]

        vote_qs = Votes.objects.filter(post=obj.post_id).values('vote', 'note', 'date_created').order_by('-vote_id')[:5]
        posts_data['vote_history'] = list(vote_qs)

        # every downVote should cost the post -1. # score b/w +5 to -5
        # var = 0
        vote_ints = [+1 if obj['vote'] else -1 for obj in posts_data['vote_history']]
        posts_data['last_5_count'] = sum(vote_ints)
        return posts_data


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = '__all__'
        use_natural_foreign_keys = True
        use_natural_primary_keys = True

    # @staticmethod
    # def serialize_vote_obj(obj):
    #     """
    #     """
    #     posts_data = model_to_dict(obj)
    #     posts_data['labels'] = StringListField()
    #
    #     vote_qs = Votes.objects.filter(post=obj.post_id)\
    #                   .values('vote', 'note','date_created')\
    #                   .order_by('-vote_id')[:5]
    #     posts_data['vote_history'] = [VotesSerializer.serialize_vote_obj(obj) for obj in vote_qs]
    #
    #     return posts_data