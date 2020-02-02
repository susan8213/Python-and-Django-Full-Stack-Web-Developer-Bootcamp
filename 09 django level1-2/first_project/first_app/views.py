from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")

    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {"insert_me": "Now I am coming from first_app/index.html !",
        "access_records": webpages_list
        }
    return render(request, 'first_app/index.html', context=my_dict)