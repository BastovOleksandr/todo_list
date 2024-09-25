from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="list-task"),
    path("tasks/add/", TaskCreateView.as_view(), name="add-task"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(),
         name="update-task"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="delete-task"),
    path("tasks/<int:pk>/toggle/", ToggleTaskView.as_view(),
         name="toggle-task"),
    path("tags/", TagListView.as_view(), name="list-tag"),
    path("tags/add/", TagCreateView.as_view(), name="add-tag"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="update-tag"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="delete-tag"),
]
