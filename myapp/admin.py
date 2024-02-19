import datetime

from django.contrib import admin
from .models import Coin, Author, Article, Comment


# Register your models here.

@admin.action(description="Изменение даты рождения")
def reset_birthday(modeladmin, request, queryset):
    queryset.update(birthday=datetime.date.today())


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'birthday']
    search_fields = ['name']
    ordering = ['surname', '-birthday']
    list_filter = ['name']
    actions = [reset_birthday]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'surname'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Почта и биография',
                'fields': ['email', 'birthday', 'biography'],
            },
        ),

    ]


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article)
admin.site.register(Comment)
