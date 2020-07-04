from django.test import TestCase

from .models import Person

import random
import string

# Create your tests here.
class CreatePersonTestCase(TestCase):
    
    def setUp(self):
        Person.objects.create(id=201, givenname="John", surname="Smith")
    
    def test_list_persons(self):
        query = Person.objects.get(givenname="John")
        assert query.givenname == "John" and query.surname == "Smith"


class SameFirstNameTestCase(TestCase):
    
    def setUp(self):
        Person.objects.create(id=201, givenname="John", surname="Smith")
        Person.objects.create(id=202, givenname="John", surname="Doe")
        
    def test_list_persons(self):
        query = Person.objects.filter(givenname="John")
        assert len(query) == 2
        

class GenderPersonTestCase(TestCase):

    def setUp(self):
        self.givenname = ''.join(random.sample(string.ascii_lowercase, random.randint(2,10)))
        self.surname = ''.join(random.sample(string.ascii_lowercase, random.randint(2,10)))
        self.gender = random.choice("MF")
        self.id = random.randint(1000, 2000)
        Person.objects.create(id=self.id, givenname=self.givenname, surname=self.surname,
                              gender=self.gender)

    def test_person_name_gender(self):
        query = Person.objects.get(id=self.id)
        assert (query.givenname == self.givenname and query.surname == self.surname and query.gender == self.gender), \
            "%s: %s" % (query.givenname, self.givenname)
