# custom_user/views.py
from django.views.generic import UpdateView, CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, PostForm, CommentForm
from .models import Profile, Post, Comment
from django.shortcuts import get_object_or_404, render

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object = form.save()
        messages.success(self.request, "Signup successful. You can now log in.")
        return response

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/edit.html'
    success_url = reverse_lazy('profile_edit')

    def get_object(self, queryset=None):
        return self.request.user.profile

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        # Set the user field before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all_posts')

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Comment created successfully.")
        return response

class CustomHomeView(TemplateView):
    template_name = 'home.html'
    
class AllPostsView(ListView):
    model = Post
    template_name = 'all_post.html'  
    context_object_name = 'posts'



class UserProfileView(TemplateView):
    template_name = 'profile/detail.html'

    def get_context_data(self, **kwargs):
        try:
            user = get_object_or_404(get_user_model(), pk=self.kwargs['pk'])
        except KeyError:
            # Handle the case when 'pk' is not present in self.kwargs
            user = self.request.user

        return {'user': user}

class PostDetailView(DetailView): 
    model = Post
    template_name = 'post.html'
