from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "html/homepage.html")

def contact(request):
    return render(request, "html/therapiest-contact.html")
    