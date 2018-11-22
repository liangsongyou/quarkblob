from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project import settings
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/<slug:slug>/', views.tag,name='tag'),
    path('blog/', include('blog.urls')),
    path('search/',include('search.urls')),
    # accounts
    path('accounts/register/', views.Register.as_view(),name='register'),
    path('accounts/change/<int:pk>/',views.UserChange.as_view(), name='user_change'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/',include('django.contrib.auth.urls')),

    path('', include('base.urls')),
] + static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)
