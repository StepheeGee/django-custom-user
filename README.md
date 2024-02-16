

### Step 1: Set Up Django Project

1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Create Django Project:**
   ```bash
   django-admin startproject custom_user_project
   ```

5. **Navigate to Project Directory:**
   ```bash
   cd custom_user_project
   ```

### Step 2: Create Custom User App

6. **Create Django App "custom_user":**
   ```bash
   python manage.py startapp custom_user
   ```

7. **Inside "custom_user" App:**
   - Create `urls.py`, `views.py`, `models.py`, `tests.py`, and `apps.py`.
   - Set up the app in `custom_user/apps.py`:

     ```python
     # custom_user/apps.py
     from django.apps import AppConfig

     class CustomUserConfig(AppConfig):
         default_auto_field = 'django.db.models.BigAutoField'
         name = 'custom_user'
     ```

8. **Update `INSTALLED_APPS` in `settings.py`:**
   ```python
   # custom_user_project/settings.py
   INSTALLED_APPS = [
       # ...
       'custom_user.apps.CustomUserConfig',
       # ...
   ]
   ```

### Step 3: Create Custom User Model

9. **Define `CustomUser` Model:**
   - Update `custom_user/models.py`:

     ```python
     # custom_user/models.py
     from django.contrib.auth.models import AbstractUser
     from django.db import models

     class CustomUser(AbstractUser):
         email = models.EmailField(unique=True)
         # Add any additional fields you need
     ```

   - Set `AUTH_USER_MODEL` in `settings.py`:

     ```python
     # custom_user_project/settings.py
     AUTH_USER_MODEL = 'custom_user.CustomUser'
     ```

### Step 4: Install Additional Packages

10. **Install Required Packages:**
    ```bash
    pip install django-widget-tweaks
    ```

### Step 5: Set Up Tailwind CSS

11. **Install Tailwind CSS:**
    ```bash
    npm install tailwindcss
    ```

12. **Create Tailwind Config:**
    ```bash
    npx tailwindcss init
    ```

    Configure `tailwind.config.js` as needed.

13. **Create CSS Files:**
    - Inside the `static/src` directory, create `input.css` and `output.css`.
    ``` bash
    npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch 
```

make sure you're looking like this in your config.js file
``` /** @type {import('tailwindcss').Config} */
module.exports = {
  // ... other configurations
  content: [
    './src/**/*.html',
    './src/**/*.js',
    // Add other paths as needed
  ],
};
```

### Step 6: Create Templates Directory

14. **Create `templates` Directory:**
    - Inside the project directory, create a `templates` directory.

### Step 7: Django Admin Configuration

15. **Configure Django Admin:**
    - Update `custom_user/admin.py`:

      ```python
      # custom_user/admin.py
      from django.contrib import admin
      from .models import CustomUser

      admin.site.register(CustomUser)
      ```

### Step 8: URLs and Views

16. **Set Up URLs and Views:**
    - Update `custom_user/urls.py`:

      ```python
      # custom_user/urls.py
      from django.urls import path
      from .views import CustomLoginView, CustomLogoutView, CustomSignUpView, CustomHomeView

      urlpatterns = [
          path('login/', CustomLoginView.as_view(), name='login'),
          path('logout/', CustomLogoutView.as_view(), name='logout'),
          path('signup/', CustomSignUpView.as_view(), name='signup'),
          path('home/', CustomHomeView.as_view(), name='home'),
      ]
      ```

    - Create corresponding views in `custom_user/views.py`.

### Step 9: Django Widget Tweaks in Templates

17. **Use Django Widget Tweaks in Templates:**
    - In your templates, load widget tweaks at the beginning and use them as needed.

### Step 10: Run Migrations and Test

18. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

19. **Create Superuser for Admin Access:**
    ```bash
    python manage.py createsuperuser
    ```

20. **Run Development Server:**
    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/admin/` to access Django Admin and verify that the custom user model works.

### Step 11: Create templates (`login.html`, `logout.html`, `signup.html`, `home.html`) with corresponding forms and views:

21. **Create Templates:**
    - Inside the `templates` directory, create the following HTML templates:
      - `login.html`: Display the login form.
      - `logout.html`: Display a logout message.
      - `signup.html`: Display the signup form.
      - `home.html`: Display the home page.

22. **Update `forms.py` for Email during Signup and Tailwind CSS Styling:**
    ```python
    # custom_user/forms.py
    from django import forms
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import get_user_model

    class CustomUserCreationForm(UserCreationForm):
        email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-input'}))

        class Meta:
            model = get_user_model()
            fields = ("username", "email", "password1", "password2")
    ```

23. **Update `views.py` for Signup, Login, and Logout with Tailwind CSS Styling:**
    ```python
    # custom_user/views.py
    from django.contrib.auth.views import LoginView, LogoutView
    from django.contrib.auth.forms import AuthenticationForm
    from django.urls import reverse_lazy
    from django.views.generic import CreateView, TemplateView
    from django.contrib import messages
    from .forms import CustomUserCreationForm

    class CustomLoginView(LoginView):
        template_name = 'registration/login.html'
        authentication_form = AuthenticationForm

    class CustomLogoutView(LogoutView):
        template_name = 'registration/logout.html'

    class CustomSignUpView(CreateView):
        template_name = 'registration/signup.html'
        form_class = CustomUserCreationForm


        success_url = reverse_lazy('login')  # Redirect to login page after successful signup

        def form_valid(self, form):
            response = super().form_valid(form)
            self.object = form.save()
            messages.success(self.request, "Signup successful. You can now log in.")
            return response

    class CustomHomeView(TemplateView):
        template_name = 'home.html'
    ```

### Step 12: Update `urls.py` in the `custom_user` directory:

24. **Update `urls.py` in the `custom_user` directory:**
    ```python
    # custom_user/urls.py
    from django.urls import path
    from .views import CustomLoginView, CustomLogoutView, CustomSignUpView, CustomHomeView

    urlpatterns = [
        path('login/', CustomLoginView.as_view(), name='login'),
        path('logout/', CustomLogoutView.as_view(), name='logout'),
        path('signup/', CustomSignUpView.as_view(), name='signup'),
        path('home/', CustomHomeView.as_view(), name='home'),
    ]
    ```

25. **Include these URLs in Your Main `urls.py`:**
    ```python
    # custom_user_project/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('custom_user.urls')),
        # Add other app URLs if any
    ]
    ```



Step 8: Django Widget Tweaks in Templates
Use Django Widget Tweaks in Templates:
In your templates, load widget tweaks and use them as needed.