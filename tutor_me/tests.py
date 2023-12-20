from django.test import TestCase
import requests
from tutor_me.models import CustomUser, Session
from django.urls import reverse

# Create your tests here.
# class URLTests(TestCase):
#     # Testing if client can successfully retrieve the appropriate pages
#
#     def test_index_url(self):
#         response = self.client.get('/', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     # def test_direct_url(self):
#     #     response = self.client.get('/direct/')
#     #     self.assertEqual(response.status_code, 200)
#
#     def test_departments_url(self):
#         response = self.client.get('/departments/', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_courses_arth_url(self):
#         response = self.client.get('/courses/ARTH', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_courses_germ_url(self):
#         response = self.client.get('/courses/GERM', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_courses_aas_url(self):
#         response = self.client.get('/courses/AAS', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
# class APITests(TestCase):
#     # Testing if the API can successfully reach its appropiate end points and gather appropiate data
#
#     def test_api_source(self):
#         response = requests.get('https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1232/?format=json', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_api_source_CS(self):
#         response = requests.get('https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&subject=CS&page=1', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_api_source_MDST(self):
#         response = requests.get('https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&subject=MDST&page=1', timeout=10)
#         self.assertEqual(response.status_code, 200)
#
#     def test_api_source_by_instructor(self):
#         response = requests.get('https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&page=1&instructor_name=Horton', timeout=10)
#         self.assertEqual(response.status_code, 200)


# class TutorTests(TestCase):
    # def test_create_tutor(self):
        # tutor = CustomUser(1, 'tutor@TutorMe.com', True, True, False, None, 'Default Tutor', 'Typical UVA Tutor', None)
        # tutor.save()
        # self.assertEquals(tutor, CustomUser.objects.filter(email='tutor@TutorMe.com').get())

    # def test_tutor_create_session(self):
        # tutor = CustomUser(1, 'tutor@TutorMe.com', True, True, False, None, 'Default Tutor', 'Typical UVA Tutor', None)
        # tutor.save()
        # session = Session(1, 1, "ASD", "A", "15", "Rice", "13:00", "14:00", "Monday", "Available", None)
        # session.save()
        # self.assertEquals(session, Session.objects.filter(course="ASD").get())


# class StudentTests(TestCase):
    # def test_create_student(self):
        # student = CustomUser(2, 'student@TutorMe.com', True, False, True, None, 'Default Student', 'Typical UVA Student', None)
        # student.save()
        # self.assertEquals(student, CustomUser.objects.filter(email='student@TutorMe.com').get())



