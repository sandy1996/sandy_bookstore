from django.shortcuts import render

#index
def index(request):
    return render(request, 'template.html')
#store
def store(request):
    return render(request,'store.html')
# Create your views here.
