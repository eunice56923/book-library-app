from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Category 
def homepage(request):
    # Fetch all categories
    categories = Category.objects.all()
    books_by_category = {}
    
    for category in categories:
        # Fetch books that belong to each category
        books = Book.objects.filter(category=category)
        if books.exists():
            books_by_category[category] = books

    # Add categories and books to context
    context = {
        'categories': categories,
        'books_by_category': books_by_category,
    }
    
    return render(request, 'home.html', context)

def book_detail(request, pk):
    # Get the book with the given primary key (pk)
    book = get_object_or_404(Book, pk=pk)
    
    # Add the book to context
    context = {
        'book': book,
    }
    
    return render(request, 'book_detail.html', context)

def book_read(request, pk):
    book = Book.objects.get(pk=pk)  # Get the book by primary key
    file_path = book.pdf_file.path  # Assuming the PDF is stored in the 'pdf_file' field of the Book model
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
