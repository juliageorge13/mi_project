from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Courses(models.Model):
    courseID = models.CharField(max_length=20)
    courseName = models.CharField(max_length=250)
    courseDescription = models.TextField()
    createdOn = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)
    courseDuration = models.CharField(max_length=20)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseName.replace(' ', '_')


class Units(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    unitName = models.CharField(max_length=250)
    unitDescription = models.TextField()
    createdOn = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.__str__() + '-' + self.unitName.replace(' ', '_')


class SubTopics(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    topicName = models.CharField(max_length=250)
    topicDescription = models.TextField()
    createdOn = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit.__str__() + '-' + self.topicName.replace(' ', '_')


class SubTopicContent(models.Model):
    subtopic = models.ForeignKey(SubTopics, on_delete=models.CASCADE)
    subtopicContent = models.TextField()
    contentType = models.CharField(max_length=10)
    updatedOn = models.DateTimeField()
    createdOn = models.DateTimeField(default=datetime.now())
    status = models.BooleanField(default=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)