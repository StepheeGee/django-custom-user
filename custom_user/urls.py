# custom_user/urls.py
from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignUpView, ProfileEditView, PostCreateView, CommentCreateView, CustomHomeView, UserProfileView, AllPostsView, PostDetailView

urlpatterns = [
    path('registration/login/', CustomLoginView.as_view(), name='login'),
    path('registration/logout/', CustomLogoutView.as_view(), name='logout'),
    path('registration/signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),  # Add a trailing slash
    path('comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('home/', CustomHomeView.as_view(), name='home'),
    path('all_posts/', AllPostsView.as_view(), name='all_posts'),
    path('user/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'), 
]
