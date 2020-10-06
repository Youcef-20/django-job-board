from django.db import models

# Create your models here.
'''
django model field
 - html widget
 - validation
 - db size
'''
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job (models.Model) : #Table

    Title = models.CharField(max_length=10) #column
   #location
    Job_Type = models.CharField(max_length=15,choices=JOB_TYPE)
    Description = models.TextField(max_length=1000)
    Published_at = models.TimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    #category
    Experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.Title

class Category(models.Model) :
  name = models.CharField(max_length=25)
  def __str__(self):
      return self.name

