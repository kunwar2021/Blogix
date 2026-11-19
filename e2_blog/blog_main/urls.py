from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as BlogsView
from document.views import editor, delete_document

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('', include('blogs.urls')), 
    path('api/dashboards/', include('dashboards.api.urls')),
    path('blogs/search/', BlogsView.search, name='search'),
    path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboards.urls')),

    path('document/', editor, name='editor'),
    path('document/delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('help/', views.help_center, name='help_center'),
    path('contact/', views.contact_us, name='contact'),
    path('terms/', views.terms_of_service, name='terms_of_service'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
