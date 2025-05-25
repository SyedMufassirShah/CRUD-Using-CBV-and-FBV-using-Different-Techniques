from django.urls import path
from . import views

# urlpatterns = [
#     path('menu/', views.menuItemListCreateView.as_view(), name="MenuItem-ListCreateAPIView"),
#     path('menu/<int:id>', views.menuItemRetrieveView.as_view(), name="MenuItem-RetrieveAPIView"),
#     path('menu/<int:id>/update', views.menuItemUpdateView.as_view(), name="MenuItem-UpdateAPIView"),
#     path('menu/<int:id>/destroy', views.menuItemDestroyView.as_view(), name="MenuItem-DestroyAPIView"),
# ]

urlpatterns = [
    path('menu-items/', views.menuItems, name='MenuItems-FBVs'),
    path('menu-items/<int:id>', views.MenuItem, name='MenuItem-FBVs-ById'),
]