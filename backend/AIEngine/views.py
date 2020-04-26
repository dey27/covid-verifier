import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView

from utility.utils import response_dict
from .models import Article as ArticleInDB
from .serializers import ArticleSerializer

data_file = '/AIEngine/webscraper/webscraper/scrapedData/crawler.csv'


class PopulateDBView(APIView):
    def post(self, request):
        try:
            data_df = pd.read_csv(settings.BASE_DIR + data_file)
            insert_count = 0
            for index, row in data_df.iterrows():
                try:
                    article_in_db_obj = ArticleInDB(
                        title=row['title'],
                        url=row['url'],
                        article_text=row['article_text'],
                        date_crawled=row['date_crawled'],
                        date_published=row['date_published'],
                        is_processed=row['is_processed']
                    )
                    article_in_db_obj.save()
                    insert_count += 1
                except Exception as e:
                    print(e)
                    pass
            return JsonResponse(
                response_dict(msg='Populated DB with {} new scraped data points'.format(insert_count),
                              code=200))
        except Exception as e:
            return JsonResponse(response_dict(msg=str(e), code=500))


class ArticleView(APIView):
    def get(self, request):
        try:
            if request.GET.get('id', None) is None:
                query_set = ArticleInDB.objects.all()
                data = ArticleSerializer(query_set, many=True).data
            else:
                query_set = ArticleInDB.objects.get(article_id=request.GET.get('id'))
                data = ArticleSerializer(query_set, many=False).data
            return JsonResponse(response_dict(data=data, code=200))
        except Exception as e:
            return JsonResponse(response_dict(msg=str(e), code=500))

# def put(self, request):
# 	if request.GET.get('id', None) == None:
# 		return JsonResponse(response_dict(msg="Invalid API Call, 'id' missing.", code=500))
# 	try:
# 		article_obj = ArticleInDB.get(article_id=request.GET.get('id'))
