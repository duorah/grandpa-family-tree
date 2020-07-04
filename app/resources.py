from import_export import resources, fields, widgets
from .models import Person, Family

class PersonResource(resources.ModelResource):
    
    person = fields.Field(column_name='Person', attribute='person_id', widget=widgets.CharWidget())
    surname = fields.Field(column_name='Surname', attribute='surname', widget=widgets.CharWidget())
    given = fields.Field(column_name='Given', attribute='givenname', widget=widgets.CharWidget())
    call = fields.Field(column_name='Call', attribute='call', widget=widgets.CharWidget())
    nickname = fields.Field(column_name='Nickname', attribute='nickname', widget=widgets.CharWidget())
    prefix = fields.Field(column_name='Prefix', attribute='prefix', widget=widgets.CharWidget())
    title = fields.Field(column_name='Title', attribute='title', widget=widgets.CharWidget())
    gender = fields.Field(column_name='Gender', attribute='gender', widget=widgets.CharWidget())
    birthdate = fields.Field(column_name='Birth date', attribute='birthdate', widget=widgets.CharWidget())
    birthplace = fields.Field(column_name='Birth place', attribute='birthplace', widget=widgets.CharWidget())
    deathdate = fields.Field(column_name='Death date', attribute='deathdate', widget=widgets.CharWidget())
    deathplace = fields.Field(column_name='Death place', attribute='deathplace', widget=widgets.CharWidget())

    class Meta:
        model = Person
        skip_unchanged = True
        exclude = ('id', )
        fields = ("person_id", "surname", "givenname", "nickname", "gender")
        export_order = ["person_id", "surname", "givenname", "nickname", "gender"]
        import_id_fields = ["person_id", "surname", "givenname", "nickname", "gender"]


class FamilyResource(resources.ModelResource):
    family = fields.Field(column_name='Family', attribute='family', widget=widgets.CharWidget())
    husband = fields.Field(column_name='Husband', attribute='husband', widget=widgets.CharWidget())
    wife = fields.Field(column_name='Wife', attribute='wife', widget=widgets.CharWidget())
    marriagedate = fields.Field(column_name='Marriage Date', attribute='marriagedate', widget=widgets.CharWidget())
    children = fields.Field(column_name='Marriage Date', attribute='marriagedate', widget=widgets.CharWidget())
    
    class Meta:
        model = Family
        skip_unchanged = True
        exclude = ('id',)
        fields = ("family", "husband", "wife", "children", "marriagedate")
        export_order = ["family", "husband", "wife", "children", "marriagedate"]
        import_id_fields = ["family", "husband", "wife", "children", "marriagedate"]