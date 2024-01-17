from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

# Create your views here.
def members(request):
    #template=loader.get_template('myform.html')
    #return HttpResponse(template.render())
    return render(request,'myform.html')

def counter(request):
    text=request.POST['text']
    return render(request,'counter.html')
