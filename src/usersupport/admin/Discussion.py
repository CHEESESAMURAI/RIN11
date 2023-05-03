from django.contrib import admin

from ..models import UserDiscussion


class DiscussionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "user_ref", 
        "ref_col",
        "history",
        "mes_id",
    )


# Register your models here.
admin.site.register(UserDiscussion, DiscussionAdmin)
