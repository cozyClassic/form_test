from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),  
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('apply/', include('apply.urls'), name='apply')
]
