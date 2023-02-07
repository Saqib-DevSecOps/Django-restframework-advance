from django.urls import path, include, re_path


from src.accounts.views import ProfileRUDView, CreateProfile



app_name = 'accounts'
urlpatterns = [
    re_path(r'^auth/', include('exarth_rest_auth.urls')),
    # re_path(r'^auth/', include('exarth_rest_auth.registration.urls')),
    path('profile/', ProfileRUDView.as_view(), name='profile'),

]
