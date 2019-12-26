from django.db import models

class Wishlist(models.Model):
user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
wished_item = models.ForeignKey(Item,on_delete=models.CASCADE)
slug = models.CharField(max_length=30,null=True,blank=True)
added_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.wished_item.title