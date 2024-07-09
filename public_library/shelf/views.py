from django.http import HttpResponse
from django.template import loader
from .models import Book


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def details_book(request, id):
  mybook = Book.objects.get(id=id)
  template = loader.get_template('details_book.html')
  context = {
    'mybook': mybook,
  }
  return HttpResponse(template.render(context, request))

def details_autor(request, id):
  myauthor = Book.objects.get(id=id)
  template = loader.get_template('details_author.html')
  context = {
    'myauthor': myauthor,
  }
  return HttpResponse(template.render(context, request))