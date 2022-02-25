from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from dashboard.models import SubscribedCourseDetails
from siteadmin.models import Courses, Units
from django.contrib import messages


def adminHome(request):
    return render(request, 'siteAdmin/home.html')


def adminUsers(request):
    if request.POST:
        user = request.POST['user']
        try:
            user = User.objects.get(username=user)
            if user.is_active:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
            messages.success(request, 'Deactivated user access !!')
        except:
            messages.error(request, 'Error in changing status !!')
        return redirect('admin-users')
    context = {
        'users': User.objects.all()
    }
    return render(request, 'siteAdmin/users.html', context)


def adminCourses(request):
    if request.POST:
        if 'newCourseName' in request.POST:
            newCourseID = request.POST['newCourseID']
            newCourse = request.POST['newCourseName']
            newCourseDescription = request.POST['newCourseDescription']
            courseStatus = True
            newCourseStatus = request.POST['newCourseStatus']
            if newCourseStatus == 'active':
                courseStatus = True
            else:
                courseStatus = False
            newcourseDuration = request.POST['newCourseDuration']
            if newCourse.strip() != "" and newCourseID.strip() != "" and newCourseDescription != "":
                if len(Courses.objects.filter(courseID=newCourseID)) != 0:
                    messages.error(request, "Course ID already exists !!")
                else:
                    course = Courses(courseID=newCourseID, courseName=newCourse,
                                     courseDescription=newCourseDescription, createdOn=datetime.now(),
                                     status=courseStatus, courseDuration=newcourseDuration,
                                     createdBy=request.user)
                    course.save()
                    messages.success(request, "New Course Created !!")
            else:
                messages.error(request, "Please fill all the fields to create a new course !!")
        elif 'newUnitName' in request.POST:
            newUnit = request.POST['newUnitName']
            courseName = request.POST['courseName']
            unitDescription = request.POST['newUnitDescription']
            newUnitStatus = True
            unitStatus = request.POST['newUnitStatus']
            if len(Courses.objects.filter(pk=courseName)) != 0:
                course = Courses.objects.get(pk=courseName)
                if unitStatus == 'active':
                    newUnitStatus = True
                else:
                    newUnitStatus = False
                if newUnit.strip() != "" and unitDescription.strip() != "":
                    if len(Units.objects.filter(unitName=newUnit, course=course)) != 0:
                        messages.error(request, "Unit Name and Details exists !!")
                    else:
                        unit = Units(course=course, unitName=newUnit, unitDescription=unitDescription,
                                     createdOn=datetime.now(), status=newUnitStatus, createdBy=request.user)
                        unit.save()
                        messages.success(request, "Unit Created !!")
                else:
                    messages.error(request, "Please fill all the fields to create a unit for a course !!")
            else:
                messages.error(request, "unexpected user behaviour !!")
        return redirect('admin-courses')
    else:
        context = {
            'courses': Courses.objects.all(),
            'units': Units.objects.all().order_by('course')
        }
        return render(request, 'siteAdmin/course.html', context)


def subscribedCourseDetails(request):
    context = {
        'subscription': SubscribedCourseDetails.objects.all()
    }
    return render(request, 'siteAdmin/subscribedDetails.html', context)


def removeSubscriptionDetails(request, id):
    try:
        sub = SubscribedCourseDetails.objects.get(pk=id)
        sub.status = False
        sub.save()
    except:
        messages.error(request, "Cant remove the subscription at this point, please try again later !")
    return redirect('admin-subscription-details')
