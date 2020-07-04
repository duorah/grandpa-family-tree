import graphene
from graphene_django import DjangoObjectType

from app.models import Person, Family

class PersonType(DjangoObjectType):
    class Meta:
        model = Person

class Query(graphene.ObjectType):
    persons = graphene.List(PersonType)

    def resolve_persons(self, info):
        return Person.objects.all()

class CreatePerson(graphene.Mutation):
    
    id = graphene.Int()
    givenname = graphene.String()
    surname = graphene.String()
    gender = graphene.String()
    
    class Arguments:
        givenname = graphene.String()
        surname = graphene.String()
        gender = graphene.String()
        
    def mutate(self, info, person, givenname, surname, gender, **kwargs):
        person = Person(person_id=person_id, givenname=givenname, surname=surname, gender=gender, **kwargs)
        user.save()
        
        return CreateUser(
            id=person.id,
            person_id=person.person_id,
            givenname=person.name,
            surname=person.last_name,
            gender=person.gender
        )
    
class Mutation(graphene.ObjectType):
    create_person = CreatePerson.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)
