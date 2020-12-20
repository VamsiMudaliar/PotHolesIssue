from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('addIssue/', views.addIssue, name="addIssue"),
    path('logout/', views.logout, name="logout"),
    path('myIssues/', views.myIssues, name="myIssues"),
    path('deleteIssue/<int:issueid>', views.deleteIssue, name="deleteIssue"),
    path('updateIssue/<int:issueid>', views.updateIssue, name="updateIssue"),
]
