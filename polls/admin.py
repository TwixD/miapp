from django.contrib import admin
from polls.models import Choice, Poll
# Register your models here.

class ChoiceInline(admin.TabularInline):#Can swap by StackedInline
	model = Choice
	extra = 4

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['question']}),
	('Date information',{'fields': ['pub_date'],'classes' : ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question','pub_date','was_published_recently') #add multiple columns
	list_filter = ['pub_date'] #add lateral filter
	search_fields = ['question'] #add textfield of search
	#date_hierarchy = 'pub_date'



admin.site.register(Poll, PollAdmin)

