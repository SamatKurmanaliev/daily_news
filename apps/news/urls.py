from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register('news', views.NewsViewSet)
router.register('status', views.StatusTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news/<int:news_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('news/<int:news_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
    path('news/<int:news_id>/<slug:slug>/', views.get_news_status),
    path('news/<int:news_id>/comments/<int:comment_id>/<slug:slug>/', views.get_comment_status),
]


