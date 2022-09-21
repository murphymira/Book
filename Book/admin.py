from django.contrib import admin


class BookAdminSite(admin.AdminSite):
    site_title = "Book Admin Site"
    site_header = "Welcome to Book Admin Interface"
    index_title = "Book Index"
