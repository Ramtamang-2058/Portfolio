from django.contrib import admin
from .models import About, MySkills, MyProject, MyResume


class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'created_date', 'edited_date')
    ordering = ('created_date',)


class MySkilsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_rate', 'created_date')
    search_fields = ('skill_name', 'skill_rate', 'created_date')
    readonly_fields = ('created_date', 'edited_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('created_date',)


class MyProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'title', 'description', 'created_date')
    search_fields = ('name', 'title', 'description', 'created_date')
    readonly_fields = ('created_date', 'edited_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('created_date',)


admin.site.register(About, AboutAdmin)
admin.site.register(MySkills, MySkilsAdmin)
admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(MyResume)