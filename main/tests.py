from django.test import TestCase
from django.urls import reverse
from main.models import LabTest, TestCategory
from users.models import User


class TestMain(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Olga',
            last_name='Olga',
            password='123',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )

        self.testcategory = TestCategory.objects.create(
            name='Category',
        )

        self.labtest = LabTest.objects.create(
            name='test',
            category=self.testcategory,
            description='test',
            price=1000,
            time=2,
        )

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contacts.html')

    def test_labtest_list(self):
        response = self.client.get('/labtest_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/labtest_list.html')

    def test_doctor_list(self):
        response = self.client.get('/doctor_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/doctor_list.html')

#    def test_create_labtest(self):
#        data = {
#            'name': 'test1',

#        }

#        response = self.client.post(
#            reverse('main:labtest_create'),
#            data=data,

#        )

#        self.assertEqual(response.status_code, 302)

# class TestContactForm(TestCase):
#    def test_can_send_message(self):
#        data = {
#            'name': 'Olga',
#            'phone_number': '123456',
#            'message': 'test_message',

#        }

#        response = self.client.post('contacts/', data=data)
#        self.assertContains(response,"test_message")
