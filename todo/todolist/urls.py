from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('create', views.create, name='create-page'),
    path('<int:pk>', views.todoDetailView.as_view(), name='detail-page'),
    path('<int:pk>/update', views.todoUpdateViews.as_view(), name='update-page'),
    path('<int:pk>/delete', views.todoDeleteViews.as_view(), name='delete-page'),
]
