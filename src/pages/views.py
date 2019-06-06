from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'home.pug', locals())

def about(request):
    
    
    page_title = 'About'
    return render(request, 'about.pug', locals())