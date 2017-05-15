"""
Django settings for cibansa project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ax63jw!ryvkv2^om_-ml$x9_%-8bx@a0wvi8egu1olcd-se3bt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djangojs',
    'widget_tweaks',
    'tinymce',
    'selectable',
    'social_django',
    'django_cleanup',
    "accounts",
    "main",
    "articles",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cibansa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'cibansa.wsgi.application'


AUTH_USER_MODEL ="accounts.User"

AUTHENTICATION_BACKENDS = (
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # 'accounts.backends.EmailAuthBackend',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/accounts/login/'
SOCIAL_AUTH_LOGIN_URL = '/account/login/'
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_USER_MODEL = 'accounts.User'


SOCIAL_AUTH_PIPELINE =(
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',

    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'accounts.util.create_profile',  # <--- set the path to the function

    'accounts.util.associate_with_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SESSION_EXPIRE_AT_BROWSER_CLOSE =False


SOCIAL_AUTH_FACEBOOK_KEY = "171409442912372"
SOCIAL_AUTH_FACEBOOK_SECRET = "7a60e411060fb12d6fcde4a8eac0e256"
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email',]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}

#
# SOCIAL_AUTH_TWITTER_KEY = '5Fv32SSQ4D3A6QANTMB0OL0l1'
# SOCIAL_AUTH_TWITTER_SECRET = 'qkfUQZRCQ1HiRWbXYFehPQmBWRmrzzYz6ul3OsyrG8lLNX9Mma'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = 'pa545ucy4utd'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'pCeeuYHPy5JNKmmS'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress',"w_share"]
# Add the fields so they will be requested from linkedin.
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address','positions','summary', 'headline', 'industry','location','public-profile-url']
# Arrange to add the fields to UserSocialAuth.extra_data
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                                   ('firstName', 'first_name'),
                                   ('lastName', 'last_name'),
                                   ('emailAddress', 'email_address'),
                                   ('location','location'),
                                   ('summary','summary'),
                                   ('public-profile-url','public-profile-url')]


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '861523143860-fenmmm3lb5ggnojcmosv5ehnadvu0l9q.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WiWBJgJsGq1VCiBY0X4_2BxF'
GOOGLE_GEOCODE_API_KEY="AIzaSyAumPEW2If9WA63ERMFobZlN8Vy8ra_Nl0"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'cibansa',
#         'USER': 'CODE-WIZARD',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd1kmb939e6u07e',
        'USER': 'tpjyuqfvbkfjzk',
        'PASSWORD': 'cb68ad15c3628d657cd49af95016f9ab4f2ec13a5f52a2033b153c64096fef83',
        'HOST': 'ec2-107-20-141-145.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

#Local host setting
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# STATIC_ROOT = '/static/'
# STATIC_URL = '/static/'
#
#
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )
#
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

MEDIA_ROOT =os.path.join(BASE_DIR,"media/")
MEDIA_URL ='/media/'





TINYMCE_JS_URL = "/static/main/js/tinymce/tinymce.min.js"
TINYMCE_JS_ROOT = "/static/main/js/tinymce"
TINYMCE_EXTRA_MEDIA = {
    # 'css': {
    #     'all': [
    #         ...
    #     ],
    # },
    'js': [
        "/static/main/js/tinymce/custom-config.js",
        "/static/selectable/js/jquery.dj.selectable.js?v=1.1.0dev",
    ],

}
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'main.core.pagination.LinkHeaderPagination',
    'PAGE_SIZE': 2
}
# TINYMCE_DEFAULT_CONFIG = {
#     "plugins":"image imagetools,table, code",
#     'theme': "modern",
#     # 'toolbar': "image",
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 10,
#     'images_upload_url': 'postAcceptor.php',
#     'images_upload_base_path': '/some/basepath',
#     'images_upload_credentials': True
#     # 'image_title': True,
#     # 'automatic_uploads': True,
#     # 'images_upload_url': 'postAcceptor.php',
#     # 'file_picker_types': 'image',
#     # 'imagetools_toolbar': "rotateleft rotateright | flipv fliph | editimage imageoptions",
#     # 'file_picker_callback': "function(cb, value, meta) { var input = document.createElement('input')"
#     #                         ";input.setAttribute('type', 'file');input.setAttribute('accept', 'image/*');"
#     #                         "input.onchange = function(){var file = this.files[0];"
#     #                         "var id = 'blobid' + (new Date()).getTime();"
#     #                         "var blobCache = tinymce.activeEditor.editorUpload.blobCache;"
#     #                         "var blobInfo = blobCache.create(id, file);blobCache.add(blobInfo);"
#     #                         "cb(blobInfo.blobUri(), {title: file.name});};input.click();}"
# }