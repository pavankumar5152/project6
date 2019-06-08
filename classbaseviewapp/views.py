from django.views.generic import view
from django.http import HttpResponse
from django.shortcuts import render

class GetInput(view):
    def get(self,request):
        return render(request,'getinput.html')

class PostInput(view):
     def post(self,request):
         return render(request,'postinput.html')
class add(view):
    def get(self,request):
        try:
            a=request.GET['t1']
            b=request.GET['t2']
            x=int(a)
            y=int(b)
            z=x+y
            return HttpResponse('<html><body bgcolor="cyan">sum is'+str(z)+'</html></body>')
        except(ValueError):
            return HttpResponse('Invalid input')
    def post(self,request):
        try:
            a=request.POST['t1']
            b=request.POST['t2']
            x=int(a)
            y=int(b)
            z=x+y
            return HttpResponse('<html><body bgcolor="cyan">sum is '+str(z)+'</htnl></body>')
        except(ValueError):
            return HttpResponse("Invalid Input")

