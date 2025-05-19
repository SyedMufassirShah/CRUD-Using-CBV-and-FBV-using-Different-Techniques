from django.urls import path
from . import views

urlpatterns = [
    path("", views.Greet, name="Greet-View"),
    path('create-book/', views.create_book, name="POST-Book"),
    path('<int:id>/', views.get_book, name="GET-Book-ById"),
    path('all-books/', views.get_allBooks, name="GET-AllBooks"),
    path('<int:id>/put-book/', views.put_book, name="PUT-PATCH-Book-ById"),
    path('<int:id>/delete-book/', views.delete_book, name="DELETE-Book-ById"),
    # Below are the APIs of DRF
    path('book/', views.book, name='Book-DRF'),
    # API for the class named BookView using ViewSet
    path('book-view/', views.BookView.as_view(
            {
                'get' : 'list',
                'post' : 'create',
            }
        ), name='Book-view'),
    path('book-view/<int:id>/', views.BookView.as_view(
            {
                'get' : 'retrieve',
                'put' : 'update',
                'patch' : 'update',
                'delete' : 'delete',
            }
        ), name="Book-view-ById"),
    
]





# _____________________________________________________________________

                    # Routing Via Simple Router
# _____________________________________________________________________
# from rest_framework.routers import SimpleRouter
# from . import views
# router = SimpleRouter(trailing_slash=False)

# router.register('book', views.BookView, basename='book')


# urlpatterns = router.urls
