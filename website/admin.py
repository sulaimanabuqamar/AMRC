from django.contrib import admin
from .models import TeamMember, ClubAbout, ClubPhoto, Book

# Admin page for TeamMember
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'club', 'branch')
    list_filter = ('role', 'club')
    search_fields = ('name',)
    ordering = ('club', 'role', 'name', 'branch')

# Inline model for displaying photos in ClubAbout's admin page (without caption)
class ClubPhotoInline(admin.TabularInline):
    model = ClubPhoto
    extra = 1  # Number of extra blank photo fields

# Admin page for ClubAbout, with ClubPhoto inline
class ClubAboutAdmin(admin.ModelAdmin):
    list_display = ('club', 'about_text')
    search_fields = ['club']
    ordering = ['club']
    inlines = [ClubPhotoInline]

# Admin page for ClubPhoto (without caption)
class ClubPhotoAdmin(admin.ModelAdmin):
    list_display = ('club', 'photo')
    search_fields = ('club__club',)
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'club')  # Display these fields in the admin list view
    search_fields = ('title',)  # Add a search box to search by book title
    list_filter = ('club',)  # Add a filter on the right to filter by club type

# Registering all models
admin.site.register(Book, BookAdmin)
admin.site.register(ClubAbout, ClubAboutAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(ClubPhoto, ClubPhotoAdmin)
