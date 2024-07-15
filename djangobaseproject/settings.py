import os
from pathlib import Path

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
SECRET_KEY = os.environ.get("SECRET_KEY", "1234verysecret")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get("DEBUG", True)

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_TYP", "django.contrib.gis.db.backends.postgis"),
        "NAME": os.environ.get("DB_NAME", "hapa"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}


SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "djangobaseproject"


ACDH_IMPRINT_URL = (
    "https://shared.acdh.oeaw.ac.at/acdh-common-assets/api/imprint.php?serviceID="
)
REDMINE_ID = 18716

# Application definition

INSTALLED_APPS = [
    "dal",
    "django.contrib.admin",
    "dal_select2",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    "reversion",
    "django_ckeditor_5",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_filters",
    "django_tables2",
    "rest_framework",
    "mptt",
    "taggit",
    "infos",
    "leaflet",
    "charts",
    "idprovider",
    "webpage",
    "browsing",
    "vocabs",
    "gn_places",
    "bib",
    "archiv",
]
if DEBUG:
    INSTALLED_APPS.insert(10, "django_extensions")
    INSTALLED_APPS.insert(11, "fixture_magic")

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "reversion.middleware.RevisionMiddleware",
]

ROOT_URLCONF = "djangobaseproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "webpage.webpage_content_processors.installed_apps",
                "webpage.webpage_content_processors.is_dev_version",
                "webpage.webpage_content_processors.get_db_name",
                "webpage.webpage_content_processors.shared_url",
                "webpage.webpage_content_processors.my_app_name",
            ],
        },
    },
]

WSGI_APPLICATION = "djangobaseproject.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"


VOCABS_DEFAULT_PEFIX = os.environ.get("VOCABS_DEFAULT_PEFIX", "mmp")
VOCABS_SETTINGS = {
    "default_prefix": VOCABS_DEFAULT_PEFIX,
    "default_ns": f"http://www.vocabs/{VOCABS_DEFAULT_PEFIX}/",
    "default_lang": os.environ.get("VOCABS_DEFAULT_LANG", "en"),
}


SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
}

Z_ID = "2770745"
Z_LIBRARY_TYPE = "group"
Z_API_KEY = os.environ.get("Z_API_KEY")

LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (41, 20),
    "DEFAULT_ZOOM": 8,
    "MIN_ZOOM": 3,
    "OVERLAYS": [],
}


# default empty choice label = '-----'; if set to None it is removed as option
# https://django-filter.readthedocs.io/en/stable/ref/settings.html#filters-empty-choice-label
FILTERS_EMPTY_CHOICE_LABEL = None
CKEDITOR_UPLOAD_PATH = "uploads/"

DEFAULT_SPECIAL_CHARS = [
    "!",
    "&quot;",
    "#",
    "$",
    "%",
    "&amp;",
    "'",
    "(",
    ")",
    "*",
    "+",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "&lt;",
    "=",
    "&gt;",
    "?",
    "@",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "[",
    "]",
    "^",
    "_",
    "`",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "{",
    "|",
    "}",
    "~",
    "&euro;",
    "&lsquo;",
    "&rsquo;",
    "&ldquo;",
    "&rdquo;",
    "&ndash;",
    "&mdash;",
    "&iexcl;",
    "&cent;",
    "&pound;",
    "&curren;",
    "&yen;",
    "&brvbar;",
    "&sect;",
    "&uml;",
    "&copy;",
    "&ordf;",
    "&laquo;",
    "&not;",
    "&reg;",
    "&macr;",
    "&deg;",
    "&sup2;",
    "&sup3;",
    "&acute;",
    "&micro;",
    "&para;",
    "&middot;",
    "&cedil;",
    "&sup1;",
    "&ordm;",
    "&raquo;",
    "&frac14;",
    "&frac12;",
    "&frac34;",
    "&iquest;",
    "&Agrave;",
    "&Aacute;",
    "&Acirc;",
    "&Atilde;",
    "&Auml;",
    "&Aring;",
    "&AElig;",
    "&Ccedil;",
    "&Egrave;",
    "&Eacute;",
    "&Ecirc;",
    "&Euml;",
    "&Igrave;",
    "&Iacute;",
    "&Icirc;",
    "&Iuml;",
    "&ETH;",
    "&Ntilde;",
    "&Ograve;",
    "&Oacute;",
    "&Ocirc;",
    "&Otilde;",
    "&Ouml;",
    "&times;",
    "&Oslash;",
    "&Ugrave;",
    "&Uacute;",
    "&Ucirc;",
    "&Uuml;",
    "&Yacute;",
    "&THORN;",
    "&szlig;",
    "&agrave;",
    "&aacute;",
    "&acirc;",
    "&atilde;",
    "&auml;",
    "&aring;",
    "&aelig;",
    "&ccedil;",
    "&egrave;",
    "&eacute;",
    "&ecirc;",
    "&euml;",
    "&igrave;",
    "&iacute;",
    "&icirc;",
    "&iuml;",
    "&eth;",
    "&ntilde;",
    "&ograve;",
    "&oacute;",
    "&ocirc;",
    "&otilde;",
    "&ouml;",
    "&divide;",
    "&oslash;",
    "&ugrave;",
    "&uacute;",
    "&ucirc;",
    "&uuml;",
    "&yacute;",
    "&thorn;",
    "&yuml;",
    "&OElig;",
    "&oelig;",
    "&#372;",
    "&#374",
    "&#373",
    "&#375;",
    "&sbquo;",
    "&#8219;",
    "&bdquo;",
    "&hellip;",
    "&trade;",
    "&#9658;",
    "&bull;",
    "&rarr;",
    "&rArr;",
    "&hArr;",
    "&diams;",
    "&asymp;",  # noqa: E501
]

CUSTOM_SPECIAL_CHARS = "ĀāĂăĄąĆćČčĐđĒēĔĕĖėĘęĚěĜĝĨĩĪīĬĭĴĵĶķĹĺŁłŃńŊŋŌōŎŏŐőŔŕŘřŚśŜŝŞşŠšŨũŪūŬŭŰűŹźŽžǪǫǮǯǴǵȀȁȄȅȈȉȌȍȐȑȔȕȨȩȮȯḀḁḌḍḔḕḖḗḪḫḰḱṀṁṂṃṄṅṆṇṌṍṐṑṒṓṘṙṚṛṢṣṬṭṶṷṸṹẽẼẹẸộỘ"  # noqa: E501

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
        ],
    },
    "extends": {
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "codeBlock",
            "sourceEditing",
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
    },
    "list": {
        "properties": {
            "styles": "true",
            "startIndex": "true",
            "reversed": "true",
        }
    },
}
