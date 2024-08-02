from django.urls import path

from .apps import FoodConfig
from .views import FoodListView

app_name = FoodConfig.name

urlpatterns = [
    path('', FoodListView.as_view(), name='food-list'),
]
