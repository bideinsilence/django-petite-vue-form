from django.shortcuts import render

# Create your views here.
def test_petite_vue(request):
    return render(request, 'petite_vue_app/test-form.html')
