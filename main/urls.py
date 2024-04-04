from django.urls import path
from .views import IndexView, AddProductView, ProductView,\
    LogoutUserView, SingUpUserView, SignInUserView, UserProfileView,\
    UserEditProfileView, SettingsView, SettingsSecurityView, CategoryView


urlpatterns = [
    path('', IndexView, name='index'),
    path('add/', AddProductView, name='add-product'),
    path('product/', ProductView, name='product'),
    path('category/', CategoryView, name='category'),
    path('signup/', SingUpUserView, name='signup'),
    path('signin/', SignInUserView, name='signin'),
    path('logout/', LogoutUserView, name='logout'),
    path('profile/', UserProfileView, name='profile'),
    path('profile/edit/', UserEditProfileView, name='edit-profile'),
    path('settings/', SettingsView, name='settings'),
    path('settings/security', SettingsSecurityView, name='security'),
]