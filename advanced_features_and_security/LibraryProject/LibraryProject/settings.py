"""
Django settings for LibraryProject project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------------
# SECURITY SETTINGS
# -----------------------------------------------------------------------------------
SECRET_KEY = 'django-insecure-g@lfgkm9l!$(&py&s$=_ucg!2+tp=xtfn=noo#105x-nupvbx='

# Keep DEBUG=False in production
DEBUG = False

# Add your domain or IP when deploying
ALLOWED_HOSTS = ["yourdomain.com", "localhost", "127.0.0.1"]

# -----------------------------------------------------------------------------------
# AUTH USER MODEL
# -----------------------------------------------------------------------------------
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# -----------------------------------------------------------------------------------
# APPLICATIONS
# -----------------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'csp',  # For Content Security Policy
]

# -----------------------------------------------------------------------------------
# MIDDLEWARE (note the comma after CSPMiddleware)
# -----------------------------------------------------------------------------------
MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',  # CSP should run early
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Redirect after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# -----------------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------------------------
# STATIC FILES
# -----------------------------------------------------------------------------------
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------------
# SECURITY HEADERS & COOKIE SETTINGS
# -----------------------------------------------------------------------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # CSRF token needs to be readable by JavaScript for some frameworks

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Redirect HTTP to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30  # 30 days initially
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# -----------------------------------------------------------------------------------
# CONTENT SECURITY POLICY
# -----------------------------------------------------------------------------------
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", "data:")
CSP_FONT_SRC = ("'self'",)
CSP_CONNECT_SRC = ("'self'",)
CSP_FRAME_ANCESTORS = ("'none'",)


# --- HTTPS & Security Settings ---

SECURE_SSL_REDIRECT = True              # Redirect HTTP → HTTPS

SECURE_HSTS_SECONDS = 31536000          # HSTS: browsers remember HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True   # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True              # Allow domain to be preloaded into browsers' HSTS list

SESSION_COOKIE_SECURE = True            # Send session cookies only over HTTPS
CSRF_COOKIE_SECURE = True               # Send CSRF cookies only over HTTPS

X_FRAME_OPTIONS = "DENY"                # Prevent clickjacking via iframes
SECURE_CONTENT_TYPE_NOSNIFF = True      # Prevent MIME type sniffing
SECURE_BROWSER_XSS_FILTER = True        # Enable browser XSS filter

# Detect HTTPS correctly when behind a proxy/load balancer (e.g., Nginx, Heroku)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
