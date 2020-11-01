from django.test import TestCase

# Create your tests here.
from .models import School, Student

from django.core.files import File


class SchoolTestCase(TestCase):
    def setUp(self):
        School.objects.create(
            name='ravi', principal='raviteja', location='hyderabad')

    def test_school_retieve(self):
        obj = School.objects.get(name='ravi')
        self.assertEquals(obj.principal, 'raviteja')

    def test_school_update(self):
        obj = School.objects.get(name='ravi')
        obj.principal = 'anything'
        obj.save()

        newObj = School.objects.get(name='ravi')
        self.assertEquals(newObj.principal, 'anything')

    # def test_employee_delete(self):
    #     count = School.objects.count()
    #     obj = School.objects.get(name = 'ravi')
    #     obj.delete()
        # 	newCount = School.objects.count()
        # 	print(count, newCount)
        # 	self.assertEqual(count-1, newCount)
