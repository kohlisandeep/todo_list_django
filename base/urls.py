from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate,DeleteView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'), # nex_page is sending user to login page after logout
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'), # pk is for primary key
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]

