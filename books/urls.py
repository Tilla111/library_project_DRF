from django.urls import path
from .views import BookListApiView,BookDetailApiView, \
    BookDeleteApiView,BookUpdateApiView,BookCreateApiView,\
    BookListCreateApiView,BookDetailUpdateDeleteApiView

urlpatterns = [
    path('', BookListApiView.as_view(),),
    path('<int:pk>/', BookDetailApiView.as_view(),),
    path('books/create/', BookCreateApiView.as_view(),),
    path('books_list_create/', BookListCreateApiView.as_view(),),
    path('books/<int:pk>/ditail_update_delete/',BookDetailUpdateDeleteApiView.as_view(),),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view(),),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view(),),
    # path('books/', book_list_view)
]