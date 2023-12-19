from django.urls import path

from . import views
from .views import signup, signin, profile, signout, edit_profile, delete_profile, create_poll, poll_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/', profile, name='profile'),
    path('', views.profile_unauthenticated, name='profile_unauthenticated'),
    path('delete_profile/', delete_profile, name='delete_profile'),
    path('create/', create_poll, name='create_poll'),
    path('poll_detail/<int:pk>/', poll_detail, name='poll_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
