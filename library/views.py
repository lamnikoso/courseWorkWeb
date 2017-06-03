# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import Context
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import F
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404

import json
import datetime
import sqlite3
import re

from news.models import News
from book.models import Book
from book.models import Genre
from book.models import Author
from user.models import Profile, BookTaken
from user.forms import UserForm, UserProfileForm

def news_more(request, id_news):
    News.objects.filter(id=id_news).update(viewing=F('viewing')+1)
    news = News.objects.get(id=id_news)
    user = request.user
    check = False
    for user_like in news.list_users_like.all():
        if user_like == user:
            check = True
    news.refresh_from_db()    
    context = Context({
        'news': news,
        'check': check,
    })
    return render(request, 'news.html', context)

def book_more(request, id_book):
    book = Book.objects.get(id=id_book)
    user = request.user
    check = False
    for book_favorites in user.profile.list_books_favorites.all():
        if book_favorites == book:
            check = True
    context = Context({
        'book': book,
        'check': check,
    })
    return render(request, 'book.html', context)

def news_like(request):
    id_news = request.GET.get('id', False)
    action = "add"
    user = request.user
    news = News.objects.get(pk=id_news)
    for item in news.list_users_like.all():
        if item == user:
            action = 'remove'
    if action == 'add':
        news.list_users_like.add(user)
        News.objects.filter(pk=id_news).update(like=F('like') + 1)
    elif action == 'remove':
        news.list_users_like.remove(user)
        News.objects.filter(pk=id_news).update(like=F('like') - 1)
    news.refresh_from_db()
    return HttpResponse(news.like)

def catalog_genre(request):
    genre = request.GET.get('genre', False)
    if genre == '0':
        books = Book.objects.all()
    else:
        books = Book.objects.filter(genre=genre)
    return render(request, 'catalog.html', {'books': books})

def search(request):
    return render(request, 'search.html', {})

def search_book(request):
    text = request.GET.get('text', False)
    category = request.GET.get('category', False)
    id_book = request.GET.get('id', False)
    user = request.user
    books = []
    if id_book is False:
        if category == 'title':
            books = Book.objects.filter(title=text.capitalize())
        elif category == 'author':
            authors_all = Author.objects.all()
            authors = []
            for author in authors_all:
                if re.search(text, str(author).lower()):
                    authors += Author.objects.filter(id=author.id)
            for author in authors:
                books += Book.objects.filter(author=author)
        elif category == 'genre':
            genre = Genre.objects.get(title=text.capitalize())
            books = Book.objects.filter(genre=genre)
        elif category == "list_books_taken":
            for item in user.profile.booktaken_set.all():
                books.append(item.book)
        elif category == "list_books_favorites":
            books = user.profile.list_books_favorites.all()
        elif category == 'debt':
            date_temp = datetime.date.today()
            for item in user.profile.booktaken_set.all():
                if date_temp > item.date_pass:
                    books.append(item.book)
    else:
        books = Book.objects.filter(id=id_book)
    return render(request, 'catalog.html', {'books': books})

def search_user(request):
    text = request.GET.get('text', False)
    category = request.GET.get('category', False)
    id_user = request.GET.get('id', False)
    users = []
    if id_user is False:
        users_all = User.objects.all()
        if category == 'username':
            for user in users_all:
                if re.match(text, user.username.lower()):
                    users += User.objects.filter(username=user.username)
        elif category == 'first_name':
            for user in users_all:
                if re.match(text, user.first_name.lower()):
                    users += User.objects.filter(first_name=user.first_name)
        elif category == 'last_name':
            for user in users_all:
                if re.match(text, user.last_name.lower()):
                    users += User.objects.filter(last_name=user.last_name)
        elif category == 'phone':
            profiles = Profile.objects.filter(phone=text)
            for profile in profiles:
                users += User.objects.filter(profile=profile)
        elif category == 'debt-users':
            for profile in Profile.objects.all():
                for book_taken in BookTaken.objects.filter(profile=profile):
                    if book_taken.date_pass < datetime.date.today():
                        users += User.objects.filter(profile=profile)
    else:
        users = User.objects.filter(id=id_user)
    return render(request, 'users.html', {'users': users, 'date': datetime.date.today(),})

def search_news(request):
    text = request.GET.get('text', False)
    category = request.GET.get('category', False)
    id_news = request.GET.get('id', False)
    news = []
    if id_news is False:
        if category == 'title':
            news_all = News.objects.all()
            for news_item in news_all:
                if re.search(text, news_item.title.lower()):
                    news += News.objects.filter(id=news_item.id)
        elif category == 'author':
            user = User.objects.get(username=text)
            news = News.objects.filter(author=user)
    else:
        news = News.objects.filter(id=id_news)
    return render(request, 'search-news.html', {'list_news': news,})

def live_search(request):
    type_search = request.GET.get('type', False)
    text = request.GET.get('text', False)
    if type_search == 'books':
        books = []
        books_all = Book.objects.all()
        for book in books_all:
            if re.match(text, book.title.lower()):
                books += Book.objects.filter(title=book.title)
        return render(request, 'live-search.html', {'type': type_search, 'books': books,})
    elif type_search == 'users':
        users = []
        users_all = User.objects.all()
        for user in users_all:
            if re.match(text, user.username.lower()):
                users += User.objects.filter(username=user.username)
        return render(request, 'live-search.html', {'type': type_search, 'users': users,})
    elif type_search == 'news':
        news = []
        news_all = News.objects.all()
        for news_item in news_all:
            if re.search(text, news_item.title.lower()):
                news += News.objects.filter(title=news_item.title)
        return render(request, 'live-search.html', {'type': type_search, 'news': news,})
    return HttpResponse("No")
    

def home_page(request, title='Library'):
    books = Book.objects.all()
    # paginator = Paginator(books_all, 20)
    genre = Genre.objects.all()
    # page = request.GET.get('page')

    context = Context({
        'title': title,
        'user': request.user,
        'genre': genre,
        'books': books,
    })

    try:
        news = News.objects.filter(status='p')
        try:
            news_late = news[0]
        except IndexError:
            context['news'] = News.objects.get(status='p')
            return render(request, 'index.html', context)
        for news_item in news:
            if news_late.publication_date < news_item.publication_date:
                news_late = news_item
        context['news'] = news_late
    except News.DoesNotExist:
        context['news'] = None

    # try:
    #     books = paginator.page(page)
    # except PageNotAnInteger:
    #     books = paginator.page(1)
    # except EmptyPage:
    #     books = paginator.page(paginator.num_pages)
    
    # context['books'] = books

    return render(request, 'index.html', context)

def link_book(request):
    id_book = request.GET.get('id', False)
    action = "add"
    user = request.user
    response = ""
    date_taken = datetime.datetime.now()
    date_pass = date_taken + datetime.timedelta(days=20)
    book = Book.objects.get(pk=id_book)

    profile = Profile.objects.get(user=user)
    for item in BookTaken.objects.all():
        if item.book == book and item.profile == user.profile:
            book_taken = item
            action = 'remove'

    if book.get_status() == 'Есть в наличии':
        if action == 'add':
            book_taken = BookTaken(book=book, profile=profile, date_taken=date_taken, date_pass=date_pass)
            book_taken.save()
            Book.objects.filter(id=id_book).update(count=F('count')-1)
            book.refresh_from_db()
            book.save()
            response = "Вы взяли эту книгу"
        elif action == 'remove':
            book_taken.delete()
            Book.objects.filter(id=id_book).update(count=F('count')+1)
            book.refresh_from_db()
            book.save()
    elif book.get_status() == 'Нет в наличии':
        if action == 'add':
            response = 'Книга отсутствует'
        elif action == 'remove':
            book_taken.delete()
            Book.objects.filter(id=id_book).update(count=F('count')+1)
            book.refresh_from_db()
            book.save()
    return HttpResponse(response)

def like_book(request):
    id_book = request.GET.get('id', False)
    action = "add"
    user = request.user
    response = ""
    book = Book.objects.get(pk=id_book)
    profile = Profile.objects.get(user=user)
    for item in profile.list_books_favorites.all():
        if item == book:
            action = 'remove'
    if action == 'add':
        profile.list_books_favorites.add(book)
        response = "В избранном"
    elif action == 'remove':
        profile.list_books_favorites.remove(book)
    profile.refresh_from_db()
    user.refresh_from_db()
    book.refresh_from_db()
    return HttpResponse(response)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile_check, created = Profile.objects.get_or_create(user=user)
            if not created:
                profile_check.address = profile.address
                profile_check.phone = profile.phone
                profile_check.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered,})

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "Главную" страницу
        return HttpResponseRedirect("/")
    else:
        # Отображение страницы с ошибкой
        raise Http404('Введенные данные неверны')

def log_out(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")