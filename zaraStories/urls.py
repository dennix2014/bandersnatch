from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import  views

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +[
    path('okpawawaaghonatakeaway/', admin.site.urls),
    path('accounts/password/chsnge/', views.login_after_password_change, name='account_change'),
    path('accounts/', include('allauth.urls')),
    path('', include('stories.urls')),
    path('stories/', include('stories.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
