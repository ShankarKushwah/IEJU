from django.contrib import admin
from .models import Branch, Semester, Syllabus


class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', )


class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'semester', )


admin.site.register(Branch, BranchAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Syllabus, SyllabusAdmin)
