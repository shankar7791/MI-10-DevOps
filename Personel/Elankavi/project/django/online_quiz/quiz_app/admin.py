from quiz_app.models import git, linux, python
from django.contrib import admin

# Register your models here.

admin.site.register(python)

admin.site.register(linux)

admin.site.register(git)

admin.site.site_header="Admin - Online Quiz"
