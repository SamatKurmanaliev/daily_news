from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination

from .models import News, Status, Comment
from .permissions import IsAuthorOrIsAuthenticated, IsAdminOrReadOnly, IsAuthor
from .serializer import NewsSerializer, StatusSerializer, CommentSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthor, ]
    pagination_class = LimitOffsetPagination
    search_fields=['title']
    ordering_fields=['created']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrIsAuthenticated]
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(news_id=self.kwargs['news_id'])

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user.author)


class StatusTypeViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    authentication_classes = [TokenAuthentication,BasicAuthentication,SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
