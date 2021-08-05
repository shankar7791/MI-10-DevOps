from student_app.models import stu_details
from django.contrib import admin

# Register your models here.
class stu_admin(admin.ModelAdmin):
    List = ['first_name','last_name','DOB','grade','gender']

admin.site.register(stu_details,stu_admin)
