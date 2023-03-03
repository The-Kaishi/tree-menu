from django.urls import path

from menuapp.views import IndexPageView


app_name = 'menuapp'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index')
]