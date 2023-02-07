from django.urls import path

from src.accounts.views import ProfileRUDView,CreateProfile

app_name = 'accounts'
urlpatterns = [
    path('profile/create', CreateProfile.as_view(), name='profile'),
    path('profile/', ProfileRUDView.as_view(), name='profile')
]
