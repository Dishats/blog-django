from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),  # Corrected to 'blog.urls'
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
