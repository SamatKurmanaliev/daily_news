
from django.db import models
from django.db.models import Count
from apps.accounts.models import Author


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news')

    def _str_(self):
        return f'{self.title} - {self.author.user.username}'

    def get_status(self):
        status = NewsStatus.objects.filter(news=self).values('status__name').annotate(count=Count('status'))
        result = {}
        for i in status:
            result[i['status__name']] = i['count']
        return result


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')

    def _str_(self):
        return f'{self.text[:20]} - {self.author.user.username}'

    def get_status(self):
        statues = CommentStatus.objects.filter(news=self).values('status__name').annotate(count=Count('status'))
        result = {}
        for i in statues:
            result[i['status__name']] = i['count']
        return result


class Status(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name


class NewsStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='news_statues')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news_statues')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_statues')

    class Meta:
        unique_together = ['author',  'news']


class CommentStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='news_statuses')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='news_statuses')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='news_statuses')

    class Meta:
        unique_together = ['author', 'comment'] 



