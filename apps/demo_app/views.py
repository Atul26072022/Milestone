from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# view of demo app for HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the demo_app index.")

# view of demo app for render_template
def render_view(request):
    return render(request, 'render_template.html')

# view of demo app for redirect
def redirect_view(request):
    return redirect_view('/render_view')