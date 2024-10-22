from .import views
from django.urls import path

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path('<int:note_id>/delete/', views.note_delete, name='note_delete'),
    path('register/', views.register, name='register'),

    path('api/notes/', views.note_list_api, name='note-list-api'),
    path('api/create/', views.note_create_api, name='note-create-api'),
    path('api/<int:note_id>/', views.note_detail_api, name='note-detail-api'),
    path('api/register/', views.register_user_api, name='register-api'),
]