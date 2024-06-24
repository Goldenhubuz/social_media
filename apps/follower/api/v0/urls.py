from django.urls import path

from .views import following_create

app_name = 'follow_api'


urlpatterns = [
    path('following-create/', following_create, name='following_create')
]