from django.db import models

# Create your models here.

class Customer(AbstractUser):
    user_type_data=((1,"HOD"),(2."staff"),(3."student"))
    user_type=models.CharField(default=1,choice=user_type_data,max_lenght=10)
    
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCAD)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    
class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCAD)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
  
class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    courses_at=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    Subjects=models.CharField(max_length=255)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    Staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()

  
    
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCAD)
    gender=models.CharField(max_length=255)
    profile_pic=models.Fieldfield()
    address=models.TextField()
    session_start_year=models.fieldfield()
    session_end_year=models.TextField()
    course_id=models.ForeignKey(course,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
     
class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    Subject_id=models.ForeignKey(course,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
     
class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    Subject_id=models.ForeignKey(course,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
class LeaveReport(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.textField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
class FeedbackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
class FeedbackStafft(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    message =models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
class NotificationStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    message =models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    

@receiver(post_save.sender=CustomerUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            staffs.objects.create(admin=instance)
        if instance.user_type==3:
            student.objects.create(admin=instance)
            
@receiver(post_save.sender=CustomerUser)
def save_user_profile(sender,instance,**kwargs):
        if instance.user_type==1:
            instance.Adminhod.save()
        if instance.user_type==2:
            instance.staffs.save()
        if instance.user_type==3:
            instance.student.save()
