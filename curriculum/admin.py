from django.contrib import admin
from curriculum.models import Standard, Subject, Lesson, Comment, Reply

class LessonAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user == obj.created_by:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user == obj.created_by:
            return True
        return False

admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)
admin.site.register(Reply)