from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth

# Create your views here.
config = {
'apiKey': "AIzaSyB_YJ_MW393T6cJaQsmil5n0pKtsAWtcNA",
    'authDomain': "where-s-the-beef.firebaseapp.com",
    'databaseURL': "https://where-s-the-beef.firebaseio.com",
    'projectId': "where-s-the-beef",
    'storageBucket': "where-s-the-beef.appspot.com",
    'messagingSenderId': "533201486090"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid credentials"
        return render(request,"signIn.html",{"msg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "home/theme2.html",{"e":email})

def signUp(request):
    return render(request,"home/signup.html")

def logout(request):
    auth.logout(request)
    return render(request, 'home/signIn.html')

def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = authe.create_user_with_email_and_password(email,passw)

        uid = user['localId']

        data = {"name":name, "status":"1"}

        database.child("users").child(uid).child("details").set(data)
    except:
        message = "Unable to create account try again"
        return render(request,"home/signup.html",{"messg":message})

    return render(request, "signIn.html")


def index(request):
    # return HttpResponse('Hello from Home!')
    #Changed from index to theme
    return render(request, 'home/theme2.html')
