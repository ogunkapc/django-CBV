from django.urls import URLPattern, path

# importing views from views.py
from .views import TodoAppCreateView, TodoAppListView, TodoAppDetailView, TodoAppUpdateView, TodoAppDeleteView


urlpatterns = [
    path('', TodoAppCreateView.as_view(), name='home'),
    path('list/', TodoAppListView.as_view(), name='list'),
    # <pk>--primary key is identification for id field
    path('detail/<pk>/', TodoAppDetailView.as_view()),
    path('update/<pk>/', TodoAppUpdateView.as_view()),
    path('delete/<pk>/', TodoAppDeleteView.as_view()),
]
