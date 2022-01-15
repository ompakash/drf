from django.urls import path
from core.views import TestAPIView,CheckListsApiView,CheckListApiView,CheckListItemCreateApiView,CheckListItemApiView

urlpatterns = [
    path('',TestAPIView.as_view()),
    path('api/checklists/',CheckListsApiView.as_view()),
    path('api/checklist/<int:pk>/',CheckListApiView.as_view()),
    path('api/checklistitem/create/',CheckListItemCreateApiView.as_view()),
    path('api/checklistitem/<int:pk>/',CheckListItemApiView.as_view()),


]
