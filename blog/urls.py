from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('about', views.my_about, name='about'),
    path('contact', views.contact_me, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
