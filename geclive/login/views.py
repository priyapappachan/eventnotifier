from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template import RequestContext
from django.views.decorators.cache import cache_control
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.template import loader, Context
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db import models
from django.core.context_processors import csrf
from login.models import Event
from login.models import Blood
from login.models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from twilio.rest import TwilioRestClient
from django.contrib.auth import logout

def start(request):
	if request.method=='GET':
		return render_to_response('start.html',{},context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/login')



def logout_view(request):
    logout(request)
    return render_to_response('logout.html',{},context_instance=RequestContext(request))
    # Redirect to a success page.

def userlogin(request):
    if request.method=='GET':
        if request.user.is_authenticated():
            return HttpResponseRedirect('/login')
        elif 'e' in request.GET:
            return render_to_response('login.html',{'error':'1'},context_instance=RequestContext(request))
        else:
            return render_to_response('login.html',{},context_instance=RequestContext(request))
    else:
        user=authenticate(username=request.POST['uname'],password=request.POST['passwd'])
        if user is not None and user.is_active:
            login(request,user)
            #return render_to_response('welcome.html', context_instance=RequestContext(request))
	    return HttpResponseRedirect('/welcome')
        else:
            return HttpResponseRedirect('/?e=1')

@login_required
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    ret={}
    if 'message' in request.GET:
        ret={'message':request.GET['message']}
    ret['c']=user.objects.get(user=request.user)
    return render_to_response('home.html',ret,context_instance=RequestContext(request))

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
	if request.user.is_authenticated():
          return render_to_response('welcome.html', context_instance=RequestContext(request))
	else:
            return HttpResponseRedirect('/?e=1')

def myprofile(request):
	return render(request,'profile.html',{'user.username':User.username})

def events(request):
	s=Event.objects.all()      
	return render_to_response('events.html',{'eventlist': s},context_instance=RequestContext(request))


def createuser(request):
    if request.method=='GET':
       return render_to_response('createuser.html',RequestContext(request))
    else:
	name=request.POST.get('username')
	first_name=request.POST.get('first_name')
	last_name=request.POST.get('last_name')
	email=request.POST.get('email')
	password=request.POST.get('password')
	dob=request.POST.get('dob')
	department=request.POST.get('batch')
	batch=request.POST.get('dept')
	no=request.POST.get('no')
	c=User.objects.create_user(username=name, password=password,first_name=first_name,last_name=last_name,email=email)
	c.save()
	c = User.objects.get(username=name)
	w=c.get_profile()
	w.dob=dob
	w.save()
	w.department=department
	w.save()
	w.batch=batch
	w.save()
	w.reg_no=no
	w.save()
	return render_to_response('welcome.html', RequestContext(request))

def createblood(request):
    if request.method=='GET':
       return render_to_response('createblood+.html',RequestContext(request))
    else:
	name=request.POST.get('name')
	organizer=request.POST.get('organizer')
	date=request.POST.get('date')
	group=request.POST.get('group')
	contact=request.POST.get('contact')
	b=Blood(name=name,organizer=organizer,date=date,group=group,contact=contact)
	b.save()
	users=User.objects.all()
	msg1=name+"on "+date + "Blood Group needed : " + group + "  Contact: " + contact 
	for usr in users:
		c = User.objects.get(username=usr.username)
		w=c.get_profile()
		if w.blood_group == group :
			email = EmailMessage('GEC-Live'," ", to=[usr.email])
			email.send()
			
	bl=Blood.objects.all()
	return render_to_response('blood+.html', {'list': bl},RequestContext(request))

def createevent(request):
    if request.method=='GET':
       return render_to_response('createevent.html',RequestContext(request))
    else:
	l=["priya"]
	s2=set(l)
	eventname=request.POST.get('newname')
	description=request.POST.get('description')
	organizer=request.POST.get('organizer')
	event_date=request.POST.get('date')
	event_time=request.POST.get('time')
	s1=set(description.split())
	c = len(s1.intersection(s2))
	msg="Event :" + eventname + " on "+event_date+" at " +event_time
	if c==0:
		b=Event(eventname=eventname, description = description, organizer=organizer,event_date=event_date,event_time=event_time,flag="true")
		b.save()
		all_usr=User.objects.all()
		for usr in all_usr:
			email = EmailMessage('GEC-Live',msg, to=[usr.email])
			email.send()
	else:
		b=Event(eventname=eventname, description = description, organizer=organizer,event_date=event_date,event_time=event_time,flag="false")
		b.save()
	s=Event.objects.all()
	accountsid = "AC6bc03393d6c2374311ef330054b81a0e"
	auth_token = "8c1a11946dc95b93789d489ea812b0a1"
	client=TwilioRestClient(accountsid,auth_token)
	call=client.calls.create(to="+919645584428",from_="+16122947646",url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
	print call.sid
	return render_to_response('events.html', {'eventlist': s},RequestContext(request))
	
def newevent(request):
	s=Event.objects.filter()
	context = {"event":s[0].eventname}
	return render(request,'events.html',context)
	
def eventdetail(request,variable):
	s=Event.objects.get(id=variable)
	return render_to_response('eventdetail.html',{'Event': s},context_instance=RequestContext(request))

def blood(request):
	bl=Blood.objects.all()
	return render_to_response('blood+.html',{'list':bl},context_instance=RequestContext(request))		
			
	
