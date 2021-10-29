
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*o!=jjr^qum*8e+*0qg_6&p!ix7nw^c3j=j!agikn-daz&citp'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_database',
        'USER': 'root',
        'PASSWORD': '27Delta!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}