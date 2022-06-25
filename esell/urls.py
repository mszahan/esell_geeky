from esell.forms import ChangePasswordForm, ConfirmPasswordForm, LoginForm, ResetPasswordForm
from django.urls import path
from esell import views
from django.contrib.auth import views as auth_views


urlpatterns = [
 
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show-cart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('buy/', views.buy_now, name='buy-now'),
    path('buydone/', views.buy_done, name='buy-done'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),


    #find out why cannot I add accounts/ prior to login, it shows page not found and it's only directing to esell/login
    # path('login/', auth_views.LoginView.as_view(template_name='esell/login.html', 
    # authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='esell/changepassword.html', 
    form_class=ChangePasswordForm, success_url='/esell/donepassword/'), name='changepassword'),

    path('donepassword/', auth_views.PasswordChangeDoneView.as_view(template_name='esell/donepassword.html'),
    name=('donepassword')),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='esell/password_reset.html',
    form_class=ResetPasswordForm), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='esell/password_reset_done.html'),
    name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='esell/password_reset_confirm.html',
    form_class=ConfirmPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='esell/password_reset_complete.html'),
    name='password_reset_complete'),


    
]
