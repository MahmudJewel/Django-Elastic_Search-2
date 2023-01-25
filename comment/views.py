from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import requests
import json
from .documents import CommentDocument
from .models import Comments
# Create your views here.


def home(request):
    # return HttpResponse('THis is home page!!!')
    return render(request, 'home.html')


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

# search using elastic 
def search_elastic(request):
    template_name = 'search.html'
    qr = request.GET.get('name')
    print('Hello ======> ', qr)
    all_comments = CommentDocument.search().query('match', name=qr )
    total_comments = all_comments.count()
    # print('all cars ====> ', all_cars)
    # all_cars = Cars.objects.all()
    for comment in all_comments:
        print('=======> single comments=> ', comment.name)
    context = {
        'all_comments': all_comments,
        'total_comments': total_comments,
    }
    return render(request, template_name, context)
