from django.urls import path

from app import views

urlpatterns = [
    path("chat/<int:pk>/", views.ChatPrivateRetrieveAPIView.as_view())
]
