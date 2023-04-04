DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'momo_db',
        'USER': 'root',
        'PASSWORD': 'qwer1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

SECRET_KEY = 'django-insecure-xrz4gs@34f^omrq36gl3r#)bixnnl#=i3*v@i$h(a2^s1lsna9'
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}