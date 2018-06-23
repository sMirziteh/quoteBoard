from django.shortcuts import render, redirect, HttpResponse
from .models import Users, Quotes
from django.contrib import messages

# Create your views here.
def quoteHome(request):
    print("user id", request.session['user_id'])
    user = Users.objects.filter(id=request.session['user_id']).exclude().get()
    quotes = Quotes.objects.all()
    # likes = quotes.all().likes.all()
    context = {
        'quotes': quotes,
        'user' : user,
        # 'likes' : likes
    }
    return render(request, 'quote_app/index.html', context)

def showUserPage(request, poster_id):
    #find user information
    poster = Users.objects.filter(id=poster_id).exclude().get()
    posts = poster.quotes_posted.all()
    context={
        'poster': poster,
        'posts': posts
    }
    #put user info into context
    #pass to rendered user page
    return render(request, 'quote_app/showuser.html', context)

def myAccount(request, user_id):
    #populate fields with user data
    user = Users.objects.filter(id=user_id).exclude().get()
    context ={
        'user': user
    }
    return render(request, 'quote_app/edituser.html', context)

def createQuote(request):
    print("form data:", request.POST)
    user_id = request.session['user_id']
    result = Quotes.objects.makeQuote(request.POST, user_id)
    print("new created quote: ", result)
    if type(result) is list:
        for error in result:
            messages.error(request, error)
        return redirect('/quotes')
    return redirect('/quotes')

def editUser(request):
    print('edit form data: ', request.POST)
    user_id = request.session['user_id']
    result = Users.objects.editUser(request.POST, user_id)
    print("edited user data: ", result)
    if type(result) is list:
        for error in result:
            messages.error(request, error)
        return redirect('myaccount/{}'.format(user_id))
    return redirect('/quotes')
    
def deleteQuote(request, quote_id):
    Quotes.objects.deleteQuote(quote_id)
    return redirect('/quotes')

def addlike(request):
    user_id = request.session['user_id']
    print('addlike form data: ', request.POST)

    Quotes.objects.addLike(request.POST, user_id)
    return redirect('/quotes')
