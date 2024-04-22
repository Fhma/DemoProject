from django.shortcuts import render, redirect
from .models import Book

def index(request):
    # this view return index
	return render(request, 'bookmodule/index.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList.html', {'books': books})

def book(request, bId): # read/sgiw/disply
    obj = Book.objects.get(id = bId)
    return render(request, 'bookmodule/book.html', {'book':obj})

def addBook(request):
    if request.method == 'POST':
        titleval = request.POST.get('title')
        authorval = request.POST.get('author')
        priceval = request.POST.get('price')
        editionval = request.POST.get('edition')
        obj = Book(title= titleval, author = authorval, price = priceval, edition = editionval)
        obj.save()
        return redirect('book', bId = obj.id )
    return render(request, "bookmodule/addBook.html", {})

def updateBook(request, bId):
    obj = Book.objects.get(id = bId)
    if request.method == 'POST':
        titleval = request.POST.get('title')
        authorval = request.POST.get('author')
        priceval = request.POST.get('price')
        editionval = request.POST.get('edition')
        obj.title = titleval
        obj.author=authorval
        obj.price = priceval
        obj.edition = editionval
        obj.save()
        return redirect('book', bId = obj.id )
    return render(request, "bookmodule/updateBook.html", {'obj':obj})

def filterbooks(request):
    
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        selected = request.POST.get('selectedgenre')
        
        mybooks = Book.objects.filter(title__icontains='or')
        mybooks2 = mybooks.filter(price__lte = 100).exclude(author_icontains = 'Saad')
        
        print(f"selected thing = {selected}")
        # now filter
        books = __getBooks()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)       
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html', {})

    