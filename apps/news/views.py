from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import IntegrityError

from .models import News, Status, Comment, NewsStatus, CommentStatus
from .permissions import IsAuthorOrIsAuthenticated, IsAdminOrReadOnly, IsAuthor
from .serializers import NewsSerializer, StatusSerializer, CommentSerializer
from apps.accounts.models import Author


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor, ]
    pagination_class = LimitOffsetPagination
    search_fields = ['title']
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])


class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]


@api_view(http_method_names=['POST', 'GET'])
def get_news_status(request, news_id, slug):
    if request.method == 'GET':
        try:
            if Author.objects.filter(user=request.user).exists():
                news = get_object_or_404(News, pk=news_id)
                author = request.user.author
                slug = get_object_or_404(Status, pk=slug)
                NewsStatus.objects.create(news=news, author=author, status=slug)
                return Response({'message': 'status added'})
            else:
                return Response({'message': "permissions error"})
        except IntegrityError:
            return Response({'message': "you already added status"})


@api_view(http_method_names=['POST', 'GET'])
def get_comment_status(request, news_id, slug, comment_id):
    if request.method == 'GET':
        try:
            if Author.objects.filter(user=request.user).exists():
                news = get_object_or_404(News,pk=news_id)
                author = request.user.author
                comment = get_object_or_404(Comment,pk=comment_id)
                slug = get_object_or_404(Status,pk=slug)
                CommentStatus.objects.create(comment=comment,author=author, status=slug)
                return Response({'message': 'status added'})
            else:
                return Response({'message': "permissions error"})
        except IntegrityError:
            return Response({'message': "you already added status"})
