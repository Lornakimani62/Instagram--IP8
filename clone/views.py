from django.shortcuts import render
import datetime as dt
# Create your views here.
def home(request):

    date = dt.date.today()


    return render(request,'index.html')