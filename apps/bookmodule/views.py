from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

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
        form = BookForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('book', bId = obj.id )
    form = BookForm(None)
    return render(request, "bookmodule/addBook.html", {'form':form})

def updateBook(request, bId):
    obj = Book.objects.get(id = bId)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('book', bId = obj.id )
        
    form = BookForm(instance=obj)
    return render(request, "bookmodule/updateBook.html", {'form':form})

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

    