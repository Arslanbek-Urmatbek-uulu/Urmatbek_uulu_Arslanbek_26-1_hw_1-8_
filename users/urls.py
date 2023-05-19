from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.RegisterAPIViews.as_view()),
    path('authorize/', views.AuthorizeAPIView.as_view()),
    # path('confirm/', views.confirm_api_view)
]