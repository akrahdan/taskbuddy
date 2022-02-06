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

# REST API


1. Import django framework
   pip install djangoframework

2. Add rest framework to INSTALLED_APPS
  ```python

  INSTALLED_APPS = [
     '''''
     'rest_framework',
     'rest_framework.authtoken'
     '''''
  ]
  ```

3. Add REST_FRAMEWORK to settings:
   ```python
   REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
   }
   ```

4. create serializers for each model:
   ```python

   from rest_framework import serializers
   from .models import Task

   class TaskSerializer(serializers.ModelSerializer):
       
       class Meta:
          model = Task
          fields = [ 'description', 'title']
   ```

4. Create Rest api Views
     ```python
     from rest_framework import APIView
     from rest_framework.authentication import SessionAuthentication, TokenAuthentication
     from .serializers import TaskSerializer
     from rest_framework.permissions import IsAuthenticated
     from rest_framework.response import Response
     from rest_framework import status
     
     class TaskApiView(APIView):

        authentication_classes = [SessionAuthetication, TokenAuthentication]
        permission_classes = [IsAuthenticated]

        def get(self, request, format=None):

          tasks = Task.objects.all()
          serializer = TaskSerializer(tasks, many=True)

          return Response(serializer.data, status= status.HTTP_200_OK )

        def post(self, request, format=None):
           
           serializer = TaskSerializer(data=request.data)
           if serializer.is_valid():
              serializer.save(
                 owner = request.user
              )
              return Response(serializer.data, status=status.HTTP_200_OK)
           return Response(serializer.errors, status=status.HTTP_403)


      ```


         



