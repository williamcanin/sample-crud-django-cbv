from person.models import PersonModel
from django.test import TestCase
from django.urls import reverse


class PersonTest(TestCase):

    def create_person(self, first_name='William', last_name='Canin', age='32'):
        return PersonModel(
            first_name=first_name,
            last_name=last_name,
            age=age
        )

    def test_person_creation_exists(self):
        p = self.create_person()
        self.assertTrue(isinstance(p, PersonModel))
        p.save()
        f = PersonModel.objects.filter(first_name__contains='Will')
        self.assertEqual(f[0].first_name, 'William')

    def test_person_list_view_url_accessible_by_name(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)

    def test_person_list_correct_template(self):
        response = self.client.get(reverse('person_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'person/person_list.html')
