from django.contrib import admin

from tasks.models import Tag, Task


admin.register(Tag)
admin.register(Task)
