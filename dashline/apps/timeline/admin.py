from models import TimeLine, Entry
from django.contrib import admin

class EntryInlineAdmin(admin.TabularInline):
    model = Entry

class AdminTimeLine(admin.ModelAdmin):
    inlines = [
        EntryInlineAdmin
    ]

admin.site.register(TimeLine,AdminTimeLine)
admin.site.register(Entry)
