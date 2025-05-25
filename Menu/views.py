from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MenuItem, Category
from .serializers import MenuItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer

# Create your views here.
class menuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class menuItemRetrieveView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
class menuItemUpdateView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
class menuItemDestroyView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
# _____________________________________________________________________________

            # Creating  FBVs For the Same Task  
# _____________________________________________________________________________


# @api_view(["GET", "POST"])
# def menuItems(request):
#     items = MenuItem.objects.select_related('category').all()
#     serializedItems = MenuItemSerializer(items, many = True)
#     return Response(serializedItems.data)

@api_view(["GET","POST"])
def menuItems(request):
    if request.method == 'GET':
        try:
            items = MenuItem.objects.select_related('category').all()
            serializers = MenuItemSerializer(items, many=True)
            return Response(serializers.data, status=200)
        except Exception as e:
            return Response(str(e), status=500)
    
    elif request.method == 'POST':
        try:
            serializers = MenuItemSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=201)
            return Response(serializers.errors, status=400)
        except Exception as e:
            return Response(str(e), status=500)

@api_view()
def singleMenuItem(request, id):
    item = MenuItem.objects.get(id=id)
    serializedItem = MenuItemSerializer(item)
    return Response(serializedItem.data)


# @api_view(['GET'])
# def singleMenuItem(request, id):
#     try:
#         menuItem = MenuItem.objects.get(id=id)
#         return Response(MenuItemSerializer(menuItem).data)
#     except MenuItem.DoesNotExist:
#         return Response(status=404)