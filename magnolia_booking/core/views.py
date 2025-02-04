from django.shortcuts import render

# Create your views here.
def index(request):
    home_index_context = {
        'title': 'Home'
    }
    return render(request=request,
                  template_name='core/index.html',
                  context=home_index_context)