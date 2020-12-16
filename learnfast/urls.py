from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



from django.contrib import admin
# Admin Site Config

admin.sites.AdminSite.site_header = 'LearnFast'
admin.sites.AdminSite.site_title = 'Área Administrativa'
admin.sites.AdminSite.index_title = 'LearnFast'



urlpatterns = [
    path('', include('learnfast.core.urls'), name='core'),
    path('courses/', include('learnfast.courses.urls'), name='courses'),
    path('conta/', include('learnfast.accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
