from django.urls import path
from . views import CreateUrl, ProfileView, EditProfileView, URLList, URLView, URLDeleteView

app_name = "shortener"

urlpatterns = [
    path("", CreateUrl.as_view(), name="create_url"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("edit_profile/", EditProfileView.as_view(), name="edit_profile"),
    path("url_list/", URLList.as_view(), name="url_list"),
    path("<int:pk>/url_detail/", URLView.as_view(), name="url_detail"),
    path("<int:pk>/delete_url", URLDeleteView.as_view(), name="delete_url"),
]