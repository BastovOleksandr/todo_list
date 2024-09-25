from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView,
)
from tasks.models import Task, Tag
from tasks.forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskForm()
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:list-task")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:list-task")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:list-task")


class ToggleTaskView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return reverse_lazy("tasks:list-task")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TagForm()
        return context


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:list-tag")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"
    success_url = reverse_lazy("tasks:list-tag")


# Delete tag
class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/confirm_delete.html"
    success_url = reverse_lazy("tasks:list-tag")
