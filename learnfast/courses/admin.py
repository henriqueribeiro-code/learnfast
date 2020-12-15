from django.contrib import admin
from .models import Courses
from django.utils.html import format_html


class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'slug','start_date', 'create_at', 'generate_pdf']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


    def generate_pdf(self, obj):
        return format_html("""
        
        <button style="
            border-style: none;
            border-radius: 5px;
            padding: 8px;
            background-color: red;
            color: white;
        " >Generate PDF</button>""")
    
    generate_pdf.short_description = 'Generate PDF'


admin.site.register(Courses, CourseAdmin)
