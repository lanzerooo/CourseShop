from django.contrib import admin
from . import models

# Register your models here.

admin.site.site_header = "CourseAny Admin"
admin.site.site_title = "Courses"
admin.site.index_title = "Welcome to the admin panel"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = models.Course
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at'], 'classes': ['collapse']})
    ]
    inlines = [CoursesInline]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Course, CourseAdmin)
