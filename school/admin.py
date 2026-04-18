from django.contrib import admin
from .models import Student, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "age", "email", "course_link")

    search_fields = ("name", "email")

    list_filter = ("course", "age")

    list_editable = ("age", "email")

    def course_link(self, obj):
        return obj.course.title
    course_link.short_description = "Course"