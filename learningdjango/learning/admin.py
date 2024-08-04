from django.contrib import admin
from .models import BookType, BookCertificate, BookReview, Store

# admin.site.register(BookType)
# admin.site.register(BookType)


class BookReviewInLine(admin.TabularInline):
    model = BookReview
    extra = 2


class BookTypesAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "date_added")
    inlines = [BookReviewInLine]


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("book_types",)


class BookCertificateAdmin(admin.ModelAdmin):
    list_display = ("book", "certificate_numer")


admin.site.register(BookType, BookTypesAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(BookCertificate, BookCertificateAdmin)
