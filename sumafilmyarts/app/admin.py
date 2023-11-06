from django.contrib import admin
from .models import Collaboration,Sponsorship,ContactData,Ideas,Application,BlogPost,Category,Career

import csv
from django.http import HttpResponse

# Register your models here.

class AdminCollaborationForm(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Brand_Agency','Industry','Collaboration_Type','file')
    list_filter= ['Date']


class AdminSponcershipForm(admin.ModelAdmin):
    list_display=('FirstName','Email' ,'Phone','Brand_Agency','Industry','Kind_Sponcer','Sponcer_Type','file')
    list_filter= ['Date']


class  AdminContactData(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Email' ,'Phone','Subject','Message','Date')
    list_filter = ['Date']
    actions = ['export_to_csv']
    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
             writer.writerow([getattr(obj, field) for field in fieldnames])
        return response
    export_to_csv.short_description = "Download selected as csv"


class AdminIdeasForm(admin.ModelAdmin):
    list_display=('Name','Email' ,'Phone','Subject','file')
    list_filter= ['Date']


#apply form
class AdminApplication(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email' ,'Phone','Experience','file')

#Blogpost
class Adminblog(admin.ModelAdmin):
    list_display = ('Id', 'Category','Title','Description','Image1','Body','CreatedName','Created_at','status')
    list_filter = ["CreatedName",'Created_at']
    

#Category
class Admincategory(admin.ModelAdmin):
    list_display = ('Name', 'Created')


#career
class AdminCareer(admin.ModelAdmin):
    list_display = ('id','title', 'location', 'Sluglink', 'posted_date','full_time','description','Body','Image2','experience','gender','age','workingtime','dead_line')




admin.site.register(Category,Admincategory)
admin.site.register(BlogPost, Adminblog)
admin.site.register(Collaboration,AdminCollaborationForm)
admin.site.register(Sponsorship,AdminSponcershipForm)
admin.site.register(ContactData,AdminContactData)
admin.site.register(Ideas,AdminIdeasForm)
admin.site.register(Application,AdminApplication)
admin.site.register(Career,AdminCareer)







