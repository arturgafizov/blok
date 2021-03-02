from django.urls import path

from . import views
from users.views import UserRetrieve

urlpatterns = [
    path('', UserRetrieve.as_view(), name='user-detail')
]
