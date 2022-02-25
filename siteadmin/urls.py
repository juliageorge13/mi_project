from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome, name="siteAdmin-home"),
    path('adminUsers', views.adminUsers, name='admin-users'),
    path('adminCourses', views.adminCourses, name='admin-courses'),
    path('subscribedCourseDetails', views.subscribedCourseDetails, name="admin-subscription-details"),
    path('removeSubscriptionDetails/<int:id>', views.removeSubscriptionDetails, name="admin-remove-subscription-details")
]
