from . import views
from django.urls import path

urlpatterns = [
  
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("contact/", views.contact, name = "contact"),
    path("courses/", views.courses, name = "courses"),
    path("services/", views.services, name = "services"),
    path("faq/", views.faq, name = "faq"),
    path("faq/<int:faq_num>/", views.faq_by_number, name = "faq_by_number"),
    path("faq_details/<str:faq_details>/", views.faq_details, name = "faq_details")
]
