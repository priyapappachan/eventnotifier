from login.models import UserProfile,Event,Blood
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#admin.site.register(EndUser)


#class PollAdmin(admin.ModelAdmin):
 #   fields = ['question']


# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)
admin.site.register(Event)
admin.site.register(Blood)
