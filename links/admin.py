from django.contrib import admin
from .models import Link, Click


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user', 'original_url', 'click_count', 'created_at')
    list_filter = ('user',)
    search_fields = ('slug', 'original_url', 'user__username')
    ordering = ('-created_at',)

    def click_count(self, obj):
        return obj.clicks.count()
    click_count.short_description = 'Nombre de clics'


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ('link', 'get_user', 'clicked_at', 'country', 'device')
    list_filter = ('country', 'device', 'clicked_at')
    search_fields = ('link__slug', 'link__user__username')
    ordering = ('-clicked_at',)

    def get_user(self, obj):
        return obj.link.user
    get_user.short_description = 'Utilisateur'
