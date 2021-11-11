from django.shortcuts import render
from .models import Lesson , Lessonscore
from .forms import Lessonform


# Create your views here.

def index_view(request):
    lessonscore = Lessonscore() 
    
    lessons = Lesson.objects.all()
    if request.method == "POST":
        form = Lessonform( request.POST )
        
        if form.is_valid():
            print(form)
            form.save()
    else :
        form=Lessonform() 
               
    
    context={ 
             
             'lessons': lessons ,
             'form': form , 
             'chartdata' : lessonscore.average()
             
             
            }
    
    return render(request , "dashboard/index.html" , context )
    