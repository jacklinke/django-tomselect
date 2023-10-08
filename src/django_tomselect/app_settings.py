import logging

from django.conf import settings
from django.utils.module_loading import import_string

from .request import DefaultProxyRequest

logger = logging.getLogger(__name__)


DJANGO_TOMSELECT_BOOTSTRAP_VERSION = getattr(settings, "TOMSELECT_BOOTSTRAP_VERSION", 5)
if DJANGO_TOMSELECT_BOOTSTRAP_VERSION not in (4, 5):
    raise ValueError("DJANGO_TOMSELECT_BOOTSTRAP_VERSION must be either 4 or 5.")

ProxyRequest = DefaultProxyRequest
DJANGO_TOMSELECT_PROXY_REQUEST = getattr(settings, "TOMSELECT_PROXY_REQUEST", None)
if DJANGO_TOMSELECT_PROXY_REQUEST is not None and type(DJANGO_TOMSELECT_PROXY_REQUEST) == str:
    try:
        ProxyRequest = import_string(DJANGO_TOMSELECT_PROXY_REQUEST)
    except ImportError as e:
        logger.exception(
            "Could not import %s. Please check your TOMSELECT_PROXY_REQUEST setting. " + str(e),
            DJANGO_TOMSELECT_PROXY_REQUEST,
        )
elif DJANGO_TOMSELECT_PROXY_REQUEST is not None and issubclass(DJANGO_TOMSELECT_PROXY_REQUEST, DefaultProxyRequest):
    ProxyRequest = DJANGO_TOMSELECT_PROXY_REQUEST

if not issubclass(ProxyRequest, DefaultProxyRequest):
    raise TypeError(
        "DJANGO_TOMSELECT_PROXY_REQUEST must be a subclass of django_tomselect.request.DefaultProxyRequest "
        "or an importable string pointing to such a subclass."
    )


def currently_in_production_mode():
    """
    Default method to determine whether to use minified files or not by checking the DEBUG setting.
    """
    return settings.DEBUG is False


# Should be either a boolean or a callable that returns a boolean
DJANGO_TOMSELECT_MINIFIED = getattr(settings, "TOMSELECT_MINIFIED", currently_in_production_mode())