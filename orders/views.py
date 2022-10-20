from rest_framework import viewsets,status
from orders.serializers import ( ClientSerializer,TableFoodSerializer ,CategorySerializer,ProductSerializer,FoodMenuSerializer )
from rest_framework.response import Response
from rest_framework.decorators import action

class ClientModelViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class TableFoodModelViewSet(viewsets.ModelViewSet):
    serializer_class = TableFoodSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()


class CategoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class FoodMenuModelViewSet(viewsets.ModelViewSet):
    serializer_class = FoodMenuSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()
