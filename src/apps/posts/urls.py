from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path("", subjects, name="subjects"),
    path("dashboard/", dashboard, name="dashboard"),
    path("login/", login_view, name="login"),

    path("create-subject/", create_subject, name="add_subject"),
    path("subject/<int:pk>", subject_details, name="subject_details"),
    path("edit-subject/<int:pk>", edit_subject, name="edit_subject"),
    path("delete-subject/<int:pk>", delete_subject, name="delete_subject"),
    
    path("create-topic/<int:subject_pk>", create_topic, name="add_topic"),
    path("subject/<int:subject_pk>/topic/<int:topic_pk>", retrieve_topic, name="topic_details"),
    path("edit-topic/<int:topic_id>", edit_topic, name="edit_topic"),
    path("delete-topic/<int:topic_id>", delete_topic, name="delete_topic"),

]
