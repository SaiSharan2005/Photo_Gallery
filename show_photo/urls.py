from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

 

urlpatterns = [
    path('',views.home, name = "home"),

    path('image/<int:pk>', views.image_view, name = "image_view"),
    path('upload-image/',views.upload_photo, name = "upload-photo"),
    path('profile/<int:pk>', views.userProfile, name = "user_profile"),

    path('update-image/<int:pk>',views.update_photo, name = "update-image"),
    path('delete-image/<int:pk>',views.delete_photo, name = "delete-image"),
    path('update-comment/<int:pk>',views.update_comment, name = "update-comment"),
    path('delete-comment/<int:pk>',views.delete_comment, name = "delete-comment"),


    path('login',views.loginPage, name = "login"),
    path('logout',views.logoutUser, name = "logout"),
    path('SignUp',views.createUser, name = "signup"),





]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)