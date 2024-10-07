from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='zander_site/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
