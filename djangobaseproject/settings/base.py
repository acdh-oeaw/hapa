import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.join(__file__, '../')))
)

SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "hapa"


ACDH_IMPRINT_URL = "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="
REDMINE_ID = 18589

# Application definition

INSTALLED_APPS = [
    'dal',
    'django.contrib.admin',
    'dal_select2',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'reversion',
    'ckeditor',
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'rest_framework',
    'mptt',
    'taggit',
    'infos',
    'leaflet',
    'charts',
    'idprovider',
    'webpage',
    'browsing',
    'vocabs',
    'gn_places',
    'bib',
    'archiv',
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
    ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'djangobaseproject.urls'

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
                'webpage.webpage_content_processors.installed_apps',
                'webpage.webpage_content_processors.is_dev_version',
                'webpage.webpage_content_processors.get_db_name',
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.my_app_name",
            ],
        },
    },
]

WSGI_APPLICATION = 'djangobaseproject.wsgi.application'

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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

ARCHE_SETTINGS = {
    'project_name': "hapa",
    'base_url': "https://id.acdh.oeaw.ac.at/hapa"
}

VOCABS_DEFAULT_PEFIX = "hapa"

VOCABS_SETTINGS = {
    'default_prefix': VOCABS_DEFAULT_PEFIX,
    'default_nsgg': "http://www.vocabs/hapa",
    'default_lang': "en"
}

Z_ID = "123"
Z_LIBRARY_TYPE = "whatever"
Z_API_KEY = "somethingelse"

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (41, 20),
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 3,
    'OVERLAYS': []
}


DEFAULT_SPECIAL_CHARS = [
    '!', '&quot;', '#', '$', '%', '&amp;', "'", '(', ')', '*', '+', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '&lt;', '=', '&gt;', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '&euro;', '&lsquo;', '&rsquo;', '&ldquo;', '&rdquo;', '&ndash;', '&mdash;', '&iexcl;', '&cent;', '&pound;', '&curren;', '&yen;', '&brvbar;', '&sect;', '&uml;', '&copy;', '&ordf;', '&laquo;', '&not;', '&reg;', '&macr;', '&deg;', '&sup2;', '&sup3;', '&acute;', '&micro;', '&para;', '&middot;', '&cedil;', '&sup1;', '&ordm;', '&raquo;', '&frac14;', '&frac12;', '&frac34;', '&iquest;', '&Agrave;', '&Aacute;', '&Acirc;', '&Atilde;', '&Auml;', '&Aring;', '&AElig;', '&Ccedil;', '&Egrave;', '&Eacute;', '&Ecirc;', '&Euml;', '&Igrave;', '&Iacute;', '&Icirc;', '&Iuml;', '&ETH;', '&Ntilde;', '&Ograve;', '&Oacute;', '&Ocirc;', '&Otilde;', '&Ouml;', '&times;', '&Oslash;', '&Ugrave;', '&Uacute;', '&Ucirc;', '&Uuml;', '&Yacute;', '&THORN;', '&szlig;', '&agrave;', '&aacute;', '&acirc;', '&atilde;', '&auml;', '&aring;', '&aelig;', '&ccedil;', '&egrave;', '&eacute;', '&ecirc;', '&euml;', '&igrave;', '&iacute;', '&icirc;', '&iuml;', '&eth;', '&ntilde;', '&ograve;', '&oacute;', '&ocirc;', '&otilde;', '&ouml;', '&divide;', '&oslash;', '&ugrave;', '&uacute;', '&ucirc;', '&uuml;', '&yacute;', '&thorn;', '&yuml;', '&OElig;', '&oelig;', '&#372;', '&#374', '&#373', '&#375;', '&sbquo;', '&#8219;', '&bdquo;', '&hellip;', '&trade;', '&#9658;', '&bull;', '&rarr;', '&rArr;', '&hArr;', '&diams;', '&asymp;'  # noqa: E501
]

CUSTOM_SPECIAL_CHARS = "ĀāĂăĄąĆćČčĐđĒēĔĕĖėĘęĚěĜĝĨĩĪīĬĭĴĵĶķĹĺŁłŃńŊŋŌōŎŏŐőŔŕŘřŚśŜŝŞşŠšŨũŪūŬŭŰűŹźŽžǪǫǮǯǴǵȀȁȄȅȈȉȌȍȐȑȔȕȨȩȮȯḀḁḌḍḔḕḖḗḪḫḰḱṀṁṂṃṄṅṆṇṌṍṐṑṒṓṘṙṚṛṢṣṬṭṶṷṸṹẽẼẹẸộỘ"  # noqa: E501

CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'office2013',
        'specialChars': [x for x in CUSTOM_SPECIAL_CHARS] + DEFAULT_SPECIAL_CHARS,
        'toolbar_YourCustomToolbarConfig': [
            {
                'name': 'document',
                'items': [
                    'Source', '-', 'Preview', 'Print', 'Templates', 'Maximize', 'ShowBlocks'
                ]
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'
                ]
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList', 'BulletedList', 'Outdent', 'Indent',
                    'Blockquote', 'CreateDiv', 'JustifyLeft', 'JustifyCenter',
                    'JustifyRight', 'JustifyBlock', 'Language'
                ]
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink', 'Anchor']},
            {
                'name': 'insert',
                'items': [
                    'Table', 'HorizontalRule', 'PageBreak']},
            {
                'name': 'styles',
                'items': [
                    'Styles', 'Format', 'Font', 'FontSize'
                ]
            },
            {
                'name': 'colors',
                'items': [
                    'TextColor', 'BGColor'
                ]
            },
            {
                'name': 'basicstyles',
                'items': [
                    'Bold', 'Italic', 'Underline', 'Strike',
                    'Subscript', 'Superscript', 'RemoveFormat', 'SpecialChar'
                ]
            },
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'font_names': 
            'Arial/Arial;'
            'Times New Roman;'
            'Verdana;',
        'font_defaultLabel': 'Arial',
        'fontSize_defaultLabel': '12px'
    }
}
