from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1, name="home1"),
    path('notes', views.notes, name="notes"),
    path('delete_note/<int:pk>', views.delete_note, name="delete_note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes-detail"),

    path('homework', views.homework, name="homework"),
    path('update_homework/<int:pk>', views.update_homework, name="update_homework"),
    path('delete_homework/<int:pk>', views.delete_homework, name="delete_homework"),

    path('youtube', views.youtube, name="youtube"),

    path('todo', views.todo, name="todo"),

    path('update_todo/<int:pk>', views.update_todo, name="update_todo"),

    path('delete_todo/<int:pk>', views.delete_todo, name="delete_todo"),

    path('books', views.books, name="books"),

    path('dictionary', views.dictionary, name="dictionary"),

    path('wiki', views.wiki, name="wiki"),

    path('conversion', views.conversion, name="conversion"),

    path('courses', views.courses, name='courses'),
    path('analysis', views.analysis, name='analysis'),
    path('subscribedCourses', views.subscribedCourses, name='subscribed-courses'),
    path('subscribeCourses/<int:pk>', views.subscribeCourses, name='subscribe-courses')
]
