import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

import django 
django.setup() 
import random
from faker import factory,Faker 
from book.models import * 
from model_bakery.recipe import Recipe,foreign_key 

fake = Faker() 

# for k in range(2):
  
    # author.make()
img_list = [
        "bookimages/9789393986078_16697197190.jpg",
        "bookimages/9780747532743.jpg",
        "bookimages/wp4089704_USu61Tz.jpg",
        "bookimages/9780330284141.jpg",
        "bookimages/9780330284141.jpg",
        "bookimages/9780552166157.jpg",
    ]
cat = [1,2,3,4,5]
for k in range(20):
        print(k)
        # exit
        books = Recipe(Books,
            title = fake.name(),
            description = fake.sentence(nb_words=500,variable_nb_words=True),
            category = Category.objects.get(pk=random.choice(cat)),
            isbn = 34523456436 ,
            current_price = 345,
            original_price = 453,
            author = fake.name(),
            image = random.choice(img_list)  )

        books.make()