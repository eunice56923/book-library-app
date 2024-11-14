from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from welcome_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/', include('welcome_app.urls')),  # Include app's URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
