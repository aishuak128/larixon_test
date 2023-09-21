from django.db import models

# Category - категории объявлений, поля: name 
# City - город объявления, поля: name 
# Advert - объявление, поля: title, description, city, category, views


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    print('ffffdsfkdlsjaflkdjsaflkdjsafljdlskaf;dlsakjfjdklsajfdklasjflkdasjflkdsajflkdsajfkldsafdsfdsfdsfdsfdsfdsfdsfdsfdsfds')
    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        


class City(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
       return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'



class Advert(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=500, blank=True, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='adverts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='adverts')
    visited = models.IntegerField(blank=True, default=0, null=False, editable=False)

    
