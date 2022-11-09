from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import requests
import json
# from .documents import CarDocument
from .models import Comments
# Create your views here.


def home(request):
    return HttpResponse('THis is home page!!!')

# Generating demo comments 
def geenerate_data(request):
    url = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    print('==================> ', payload[0])
    for data in payload:
        print("Generated data : ======> ", count)
        print("Name : ======> ", data.get('name'))
        print("Email : ======> ", data.get('email'))
        print("Body : ======> ", data.get('body'))
        count = count+1
        Comments.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            body=data.get('body')
        )
    text = 'Total generated data => ' + str(count)
    return HttpResponse(text)
    # return HttpResponse('Generated data')

# def search_elastic(request):
#     qr = request.GET.get('color')
#     print('Hello ======> ', qr)
#     all_cars = CarDocument.search().query('match', description=qr)
#     print('all cars ====> ', all_cars)
#     # all_cars = Cars.objects.all()
#     for car in all_cars:
#         print('=======> single cars=> ', car.name)
#     return HttpResponse('Search in Elastic')
