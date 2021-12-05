# Authentication
1. Add django-allauth library
   -- pip install django-allauth
2. Add AUTHENTICATION_BACKENDS to settings:
   ```python
   AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
   ]
   ```

3. Include the following sub apps in INSTALLED_APPS
    1. 'django.contrib.sites',
    2. 'allauth',
    3. 'allauth.account',
    4. 'allauth.socialaccount'
4. Add SITE_ID in setitings
   SIDE_ID = 1
5. Include the following in settings
   - ACCOUNT_AUTHENTICATION_METHOD = "username_email"
   - ACCOUNT_EMAIL_REQUIRED =True
   - ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# Email Confirmation
 - add the smtp settings below to settings
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_HOST_USER = 'youremail@gmail.com' 
   EMAIL_HOST_PASSWORD = 'yourpassword'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
 - allow less secure apps on gmail
   https://myaccount.google.com/lesssecureapps?pli=1

# Static Files
