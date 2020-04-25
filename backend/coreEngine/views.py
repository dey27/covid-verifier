from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Initiative
from .serializers import InitiativeSerializer

from rest_framework.views import APIView, status
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

class HomeView(APIView):

	def get(self, request):
		querySet = Initiative.objects.all()
		# response = json.loads(serializers.serialize('json', querySet,
		# 					fields = ('', ''),
		# 					indent=2, \
		# 					use_natural_foreign_keys=True, \
		# 					use_natural_primary_keys=True))
		return JsonResponse(querySet, safe=False, status=200)

	def post(self, request):
		initiative_name = request.get.data['name']
		created_date = request.get.data['name']

		pass
