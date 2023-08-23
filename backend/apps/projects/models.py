from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Tag(models.Model):
    name = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.CharField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], blank=False
    )

    def __str__(self):
        return str(self.reviewer) + " | " + str(self.rating)

class Topic(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, blank=False)
    description = models.CharField(max_length=200)
    private = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title + " | " + str(self.creator)
