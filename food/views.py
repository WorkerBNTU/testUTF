from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FoodCategory
from .serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        categories = FoodCategory.objects.filter(food__is_publish=True).distinct().order_by('id')
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
