from django.shortcuts import render
from .utils import search_student_by_id

# Create your views here.

def index(request):
    """หน้าแรกของ myapp"""
    return render(request, 'myapp/home.html')

def search_student(request):
    """
    View for searching student data.
    """
    query = request.GET.get('student_id')
    results = []
    error_message = None

    if query:
        if query.isdigit():
            results = search_student_by_id(query)
        else:
            error_message = "คุณต้องใส่รหัสนักศึกษาที่เป็นตัวเลขเท่านั้น"
    
    return render(request, 'myapp/search_results.html', {'results': results, 'query': query, 'error_message': error_message})
