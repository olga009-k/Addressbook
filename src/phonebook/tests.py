from django.test import TestCase
from addressbook.models import Person
from addressbook.views import AddPhoneFormView, HomePageView
import addressbook.forms
from django.urls import reverse_lazy


class ModelTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            first_name="lion",
            last_name="roar",
            address="test",
            phone="6567-85",
            url="https://my-url",
        )

    def test_person(self):
        """Posts are given slugs correctly when saving"""
        person = Person.objects.get(first_name='lion')
        assert person.last_name == 'roar'


class ViewsTestCase(TestCase):


    def test_server_is_running(self):
        """
        Server responds with 200 on a default route request
        """
        response = self.client.get('http://localhost:8000')

        self.assertEqual(response.status_code, 200)

    def test_create_person_ok(self, **kwards):
        """
        Test creating a new person with correct fields
        """

        data={
                'first_name': 'test_first_name',
                'last_name': 'test_last_name',
                'address': 'test_address',
                'phone': 'test_phone',
                'url': 'https://test_url',
            }



        response = self.client.post(
            'http://localhost:8000/add/',
            data=data
        )

        self.assertEqual(response.status_code, 200)
        print(response)

        HomePageView.get_context_data["persones"]

        person = Person.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            phone=data['phone'],
            url=data['url']
        )





