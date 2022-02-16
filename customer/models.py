from django.db import models
from django.utils import timezone


class Comment(models.Model):
    post = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text + '(' + str(self.id) + ')'


class Customer(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '(' + str(self.id) + ')'

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
