from django.urls import path
from .import views
urlpatterns = [
    path('login/',views.loginPage, name="login"), 
    path('logout/',views.logout_view, name="logout"), 
    path('register/',views.registerUser, name="register"),
    path('account/',views.userAccount, name="account"),
    path('edit_account/', views.editAccount, name='edit_account'),
    path('create_skill/',views.createSkill, name="create_skill"),
    path('update_skill/<str:pk>/',views.updateSkill, name="update_skill"),
    path('delete_skill/<str:pk>/',views.deleteSkill, name="delete_skill"),
    path('inbox/',views.inbox, name="inbox"),
    path('view_message/<str:pk>/',views.viewMessage, name="view_message"),
    path('create_message/<str:pk>/',views.createMessage, name = "create_message"),

    


    path('',views.profiles, name="profiles"), 
    path("user_profile/<str:pk>/",views.userProfile, name="user_profile"),
]
