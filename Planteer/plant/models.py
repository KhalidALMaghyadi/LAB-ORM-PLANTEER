from django.db import models

# Create your models here.


from django.db import models

# Create your models here.
class Plant(models.Model):
    name  = models.CharField(max_length=2048)
    about = models.TextField()
    used_for = models.TextField() 
    image = models.ImageField(upload_to="images/" , default="images/default.jpg")
    
    
    categoryChoices= models.TextChoices("Category", "Tree Fruit Vegetables")
    category  = models.CharField(max_length=64, choices=categoryChoices.choices, default=categoryChoices.Tree)
    
    is_edible = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)    
    