from django.http import JsonResponse
import logging

from utility.utils import response_dict
from .models import Posts, Votes
from taggit.models import Tag
from .serializers import PostsSerializer, VotesSerializer

from rest_framework.views import APIView


class SearchBarValuesView(APIView):
    def get(self, request):
        payload = {
            'locations': list(Posts.objects.values_list('location_city', flat=True).distinct()),
            'labels': list(Tag.objects.values_list('slug', flat=True).distinct())
            # 'labels': list(Tag.objects.all().values('id', 'name'))    # needed if search params required ids
        }
        return JsonResponse(response_dict(data=payload))


class PostsView(APIView):
    def get(self, request):
        """
        @URL - localhost:8000/apis/posts/?location_city=Delhi&labels=oxygen,food
        @request_params =
            labels = comma separated list
            location_city = single string value
        @returns
        {
            "meta": {
                "code": 200,
                "message": "",
                "data_statistics": {}
            },
            "data": {
                "posts": [
                    {
                        "post_id": 1,
                        "labels": "beds, oxygen",
                        "post_name": "test1",
                        "phone_numbers": [
                            "9425331581"
                        ],
                        "description": "abc",
                        "location_city": "delhi",
                        "location_area": null,
                        "supporting_url": null,
                        "vote_count": 7,
                        "date_updated": "2021-04-25T12:27:35.193850+05:30",
                        "vote_history": [
                            {
                                "vote": false,
                                "note": "works",
                                "date_created": "2021-04-25T12:42:48.061Z"
                            },
                            {
                                "vote": true,
                                "note": "works",
                                "date_created": "2021-04-25T12:42:34.483Z"
                            },
                        ],
                        "last_5_count": 3
                    }
                ]
            }
        }
        """
        request_params = {}

        if request.GET.get('labels', None) is not None:
            labels = [labels.strip() for labels in request.GET.get('labels').split(',')]
            request_params['labels__name__in'] = labels
        if request.GET.get('location_city', None) is not None:
            request_params['location_city__iexact'] = request.GET.get('location_city')

        if len(request_params) >= 1:
            queryset = Posts.objects.filter(**request_params).distinct()
        else:
            raise RuntimeError("Search Parameters are mandatory")

        logging.info("Retrieved {} objects".format(len(queryset)))

        payload = {
            'posts': [PostsSerializer.serialize_with_votes(obj) for obj in queryset]
            # 'posts': PostsSerializer(queryset, many=True).data # for Posts serialization only.
        }

        return JsonResponse(response_dict(data=payload))

    def post(self, request):
        """
        @URL - localhost:8000/apis/posts/
        @body -
        {
            "post_name": "test1",
            "phone_numbers": [
                "9425331581"
            ],
            "description": "abc",
            "location_city": "delhi",
            "location_area": "ncr",
            "supporting_url": null,
            "labels": ["beds","oxygen", "food"]
        }
        """
        body = request.data
        try:
            labels = body.pop('labels')
            logging.info("Received new post request")
            post_obj = Posts.objects.create(**body)  # Do not call save() method now, else it will save twice.
            post_obj.labels.add(*labels)   # this will save it too.
        except Exception as e:
            raise RuntimeError("Failed - {}".format(e))

        return JsonResponse(response_dict(msg="Successful"))


class VotesView(APIView):
    def get(self, request):
        """
        @URL - localhost:8000/apis/votes/?post_id=1
        @request_params =
            post_id
        @returns
            {
                "meta": {
                    "code": 200,
                    "message": "",
                    "data_statistics": {}
                },
                "data": {
                    "votes": [
                        {
                            "vote_id": 2,
                            "vote": false,
                            "note": "unreachable",
                            "date_created": "2021-04-25T17:26:42.639779+05:30",
                            "user_ip": null,
                            "post": 1
                        },
                    ]
                }
            }
        """
        if request.GET.get('post_id', None) is not None:
            post_id = request.GET.get('post_id', None)
            queryset = Votes.objects.filter(post=post_id).order_by('-vote_id')[:5]
        else:
            raise RuntimeError("Post is required in request params.")

        logging.info("Retrieved {} objects".format(len(queryset)))

        payload = {
            'votes': VotesSerializer(queryset, many=True).data
        }

        return JsonResponse(response_dict(data=payload))

    def post(self, request):
        """
        @URL - localhost:8000/apis/votes/
        @Body -
        {
            "vote": false,
            "note": "works",
            "post": 1
        }
        @Returns - Updated post
        """
        body = request.data
        try:
            logging.info("Received new vote request - {}".format(body))
            body['post'] = Posts.objects.get(post_id=body['post'])
            # logging.info("Updating Post - {}, {}".format(body['post'], body['post'].vote_count))

            Votes.objects.create(**body)  # Do not call save() method now, else it will save twice.
        except Exception as e:
            raise RuntimeError("Voting Failed - {}".format(e))

        payload = {
            'post': PostsSerializer(body['post'], many=False).data
        }

        return JsonResponse(response_dict(data=payload))
