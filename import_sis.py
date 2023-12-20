import requests
import json
from tutor_me.models import Department, Course
from django.http import JsonResponse
from django.http import HttpRequest

def getAllDepartments(request):
    # query the api and return a json file
    response = requests.get('https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearchOptions?institution=UVA01&term=1232/?format=json').json()
    # iterate through all subjects
    num_departments = 0
    for c in response['subjects']:
        subject = c['descr']
        mnemonic = c['subject']
        Department.objects.create(dept_mnemonic=mnemonic, dept_name=subject)
        num_departments+=1
        # append the subject mnemonic to list
    return JsonResponse({'message': f'Successfully loaded {num_departments} departments.'}) 

def getAllCourses(request):
    departments = Department.objects.all()
    for dept in departments:
        i = 1
        undergrad=True
        while undergrad:
            base_url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1232&subject='
            trailing_info = '&page=' + str(i)
            course_subject = dept.dept_mnemonic.upper()
            # get page of all courses in department passed in by URL
            response = requests.get(base_url + course_subject + trailing_info).json()
            course_list = []
            # get name of subject so html can display at top of course page
            course_mnemonic = response[0]['subject']
            # populate course_list with all course names and all course numbers
            for c in response:
                graduate_level = c['acad_career']
                course_info = course_mnemonic + " " + c['catalog_nbr'] + " - " + c['descr']
                if course_info not in course_list and graduate_level == 'UGRD':
                    course_list.append(course_info)
                    Course.objects.create(course_info=course_info, department=dept)
                if graduate_level != 'URGD':
                    undergrad = False
            i+=1
        print("Dept "+ dept.dept_mnemonic +" finished.")
    return JsonResponse({'message': f'Successfully loaded courses.'}) 





request = HttpRequest()
request.method = 'GET'
#response = getAllDepartments(request)
response= getAllCourses(request)
print(response)