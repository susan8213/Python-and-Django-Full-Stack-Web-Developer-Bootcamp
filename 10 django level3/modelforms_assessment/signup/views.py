from django.shortcuts import render
from signup.models import User
from signup.forms import User, UserForm

# Create your views here.
def index(request):
    return render(request, 'signup/index.html')

def user_list(request):
    user_records = User.objects.all()
    context = {"user_records": user_records}
    return render(request, 'signup/users.html', context=context)

def signup(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid:
            form.save()
            return index(request)
        else:
            print('ERROR: FORM INVALID')
    return render(request, 'signup/signup.html', {"form": UserForm()})
    