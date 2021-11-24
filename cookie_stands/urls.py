from django.urls import path
from .views import CookieStandList, CookieStandDetail

urlpatterns = [
    path("", CookieStandList.as_view(), name="Cookie_Stand_List"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="Cookie_Stand_Detail"),
]
