from typing import Counter
from django.db import models

# Create your models here.


class Lesson(models.Model):
    Name=models.CharField( max_length=100)
    
    def __str__(self) -> str:
        return f'{self.Name}'
    
    
class Lessonscore(models.Model):
    Lesson=models.ForeignKey(to=Lesson , on_delete=models.PROTECT)
    Score = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.Lesson.Name} '   

    def average(self):
        text=''
        for lesson in Lesson.objects.all() :
            avg=0
            sum=0
            counter=0
            for scorelesson in Lessonscore.objects.all():
                if scorelesson.Lesson.id == lesson.id :
                    sum += scorelesson.Score
                    counter+=1
            if counter != 0 :        
                avg=sum/counter
            text+=str(avg)+','  
        return text          
                        