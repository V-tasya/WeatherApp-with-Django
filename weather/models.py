from django.db import models
# models is a model from django
# which contains classes and methods for working with databases

# creating database city
class City(models.Model):
    #City is a database model
    name = models.CharField(max_length=30) #name is a field of tab which respond for a column in database
    # max length of a string is 30 characters
    # django automatically added field id, which is a unique key (column with 1, 2, 3,...)

    # if name = "Paris" this method returns "Paris"
    def __str__(self):
        return self.name
