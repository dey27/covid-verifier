from django.http import JsonResponse
import logging

from utility.utils import response_dict
# from .apps import CoreengineConfig
from .models import Initiative
from .serializers import InitiativeSerializer

from rest_framework.views import APIView

# logger = Logs.get_logger(CoreengineConfig.name)


# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authtoken.models import Token

# class LoginUserView(APIView):
# 	permission_classes = [IsAuthenticated]

# 	def get(self, request):
# 		userObjs = LoginUser.objects.all()
# 		response = LoginUserSerializer(userObjs, many=True).data
# 		return JsonResponse(response, safe=False, status=200)

# class RegisterUserView(APIView):
# 	permission_classes = [AllowAny]

# 	def post(self, request):
# 		try:
# 			username = request.data['username']
# 			password = request.data['password']
# 			newUser = LoginUser.objects.create_user(username=username,\
# 													password=password)
# 			token = Token.objects.create(user=newUser)

# 			returnText = "Successful! Your Username is " + str(newUser.username)
# 			return JsonResponse(utils.create_response(None, returnText), safe=False, status=200)
# 		except Exception as e:
# 			return JsonResponse(utils.create_response(None, str(e)), safe=False, status=200)

class InitiativeView(APIView):
    def get(self, request):
        try:
            if request.GET.get('id', None) is None:
                query_set = Initiative.objects.all()
                data = InitiativeSerializer(query_set, many=True).data
            else:
                query_set = Initiative.objects.get(initiative_id=request.GET.get('id'))
                data = InitiativeSerializer(query_set, many=False).data
            logger.info("Successfully Retrieved objects")
            return JsonResponse(response_dict(data=data, code=200))
        except Exception as e:
            return JsonResponse(response_dict(msg=str(e), code=500))

    def post(self, request):
        try:
            request_obj = request.data
            initiative_obj = Initiative.objects.create(initiative_name=request_obj['initiative_name'],
                                                       description=request_obj['description'],
                                                       workforce_size=request_obj['workforce_size'],
                                                       parent_entity=request_obj['parent_entity'],
                                                       location_city=request_obj['location_city'],
                                                       location_country=request_obj['location_country'],
                                                       googlemaps_url=request_obj['googlemaps_url'],
                                                       date_started=request_obj['date_started'],
                                                       year_started=request_obj['year_started'],
                                                       is_active=request_obj['is_active'])
            data = InitiativeSerializer(initiative_obj, many=False).data
            # logger.info("Created new Object with id - {}" .format(initiative_obj.initiative_id))
            return JsonResponse(response_dict(data=data, code=200))
        except Exception as e:
            return JsonResponse(response_dict(msg=str(e), code=500))
