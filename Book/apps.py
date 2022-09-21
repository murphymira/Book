from django.contrib.admin.apps import AdminConfig
from .admin import BookAdminSite


class BookAdminConfig(AdminConfig):
    default_site = "Book.admin.BookAdminSite"
