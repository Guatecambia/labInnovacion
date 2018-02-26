from django.contrib import admin
from django import forms
import unicodedata

from .models import Municipality, Project, RateItem, Rate


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__' 
        
    def __init__(self, *args, **kwargs):
        super(ProjectAdminForm, self).__init__(*args,**kwargs)
        muni = Municipality.objects.filter(name = self.current_group)
        if not(self.is_super):
            self.initial['municipality'] = muni[0].id
            

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    
    def get_form(self, request, *args, **kwargs):
        #pass the parameter
        form = super(ProjectAdmin, self).get_form(request, *args, **kwargs)
        form.current_group = request.user.groups.values_list('name',flat=True)
        form.is_super = request.user.is_superuser
        return form
    
    def get_queryset(self, request):
        #get all projects if it is superadmin   
        qs = super(ProjectAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        #limit to the group
        group = request.user.groups.values_list('name',flat=True)
        muni = Municipality.objects.filter(name = group)
        return qs.filter(municipality=muni)
    
    def get_readonly_fields(self, request, obj = None):
        if not(request.user.is_superuser):
            return ('municipality',)+ self.readonly_fields
        return super(ProjectAdmin, self).get_readonly_fields(request, obj)
    
    def save_model(self, request, obj, form, change):
        if (not(request.user.is_superuser)):
            group = request.user.groups.values_list('name',flat=True)
            muni = Municipality.objects.filter(name = group).first()
            obj.municipality = muni
        super(ProjectAdmin, self).save_model(request, obj, form, change)
            
admin.site.register(Municipality)
admin.site.register(Project, ProjectAdmin)
admin.site.register(RateItem)
admin.site.register(Rate)
