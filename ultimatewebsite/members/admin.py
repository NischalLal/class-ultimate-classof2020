from django.contrib import admin
from members.models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    '''
        Admin View for Member
    '''
    list_display = ('full_name', 'email', 'phone_number',)

admin.site.register(Member, MemberAdmin)
