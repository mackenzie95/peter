from django.shortcuts import render

from .models import app

# Create your views here.
def app_list_view(request):
    app_objects = app.objects.all()
    context = {
            'app_objects': app_objects
            }
    return render(request, "app/index.html", context)

