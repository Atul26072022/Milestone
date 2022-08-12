from django.urls import path

from . import views

urlpatterns = [
    # urls of HTTPResponse
    path('', views.index, name='index'),
    # urls of render_view 
    path('render_view', views.render_view, name='render_view'),
    # urls of redirect_view
    path('redirect_view', views.render_view, name='redirect_view'),
]