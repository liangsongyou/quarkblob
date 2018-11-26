from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from project import settings
from base import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('accounts/register/', views.Register.as_view(),name='register'),
    path('accounts/change/<int:pk>/',views.UserChange.as_view(), name='user_change'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/',include('django.contrib.auth.urls')),
    
] 

urlpatterns += i18n_patterns(
    path('', include('base.urls')),
    path('blog/',include('blog.urls')),
    path('tags/<slug:slug>/',views.tag, name='tag'),
    path('feedback/',include('feedback.urls')),
    path('search/',include('search.urls')),
    path(_('about/'), views.about, name='about'),
    prefix_default_language=False,
) + static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)