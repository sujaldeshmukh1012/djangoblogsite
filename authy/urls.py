from django.urls import path
from authy.views import UserProfile, Signup, PasswordChange, PasswordChangeDone, EditProfile

from django.contrib.auth import views as authViews



urlpatterns = [
   	
      path('profile/edit', EditProfile, name='edit-profile'),
   	path('signup/', Signup, name='signup'),
   	path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
   	path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   	path('reset_password/',authViews.PasswordResetView.as_view(), name="reset_password"),
      path('reset_password_sent/',authViews.PasswordResetDoneView.as_view(), name = "password_reset_done"),
      path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
      path('reset_password_complete/',authViews.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

   ]
"""path('changepassword/', PasswordChange, name='change_password'),
      path('changepassword/done', PasswordChangeDone, name='change_password_done'),
      path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
      path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
      path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
      path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
"""