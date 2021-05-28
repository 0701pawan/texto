import math
from  django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def prime(request):
   djtext=int(request.GET.get('text','default'))
   count=0
   for i in range(2,int(math.sqrt(djtext))+1):
       if djtext%i==0:
           count+=1
   if count>0:
       param={'chars':"It is not prime"}
   else:
       param = {'chars': "It is prime"}
   return render(request,'charcount.html',param)
