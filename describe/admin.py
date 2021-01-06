from django.contrib import admin

from .models import Description

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'username', 'description_text')
    search_fields = ['class_name', 'username']

admin.AdminSite.site_header = 'DescribeNet Submissions'
admin.AdminSite.index_title = 'DescribeNet Admin'
admin.AdminSite.site_title = ''
admin.site.register(Description, DescriptionAdmin)