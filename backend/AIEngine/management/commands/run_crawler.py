from django.core.management.base import BaseCommand


# USAGE - python manage.py run_crawler
class Command(BaseCommand):
    help = 'Run web crawler to scrape for environment initiative News'

    def add_arguments(self, parser):
        # parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        pass

    def handle(self, *args, **kwargs):
        print(self.help)
        print('This function is currently empty. Returning to Control.')
        return

# CALLING THIS
# class ScrapeData(APIView):
# 	def get(self, request):
# 		management.call_command('run_crawler')
# 		return JsonResponse('Crawler Running', safe=False, status=status.HTTP_200_OK)
