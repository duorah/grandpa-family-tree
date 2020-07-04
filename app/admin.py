from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here.
from .models import Person, Family
from .resources import PersonResource, FamilyResource

admin.site.site_header = "Family Tree"

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    resource_class = PersonResource
    list_display = ('id', 'person_id', 'surname', 'givenname', 'nickname', 'gender', '_children')

@admin.register(Family)
class FamilyAdmin(ImportExportModelAdmin):
    resource_class = FamilyResource
    list_display = ('id', 'family', 'husband', 'wife', '_children', 'marriagedate')

