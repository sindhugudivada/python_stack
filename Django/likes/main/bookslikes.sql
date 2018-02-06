>>> User.objects.create(first_name="User1", last_name="L1",email="user1@gmail.com") #create user
>>> Book.objects.create(name="sixth", desc="321",uploader_id="3") #have user create book
User.objects.get(id=1).liked_books.add(Book.objects.first()) #adding book to the liked books of user
User.objects.get(id=1).liked_books.add(Book.objects.last())
User.objects.get(id=2).liked_books.add(Book.objects.first())
User.objects.get(id=2).liked_books.add(Book.objects.get(id=3))

# Have the third user like all books:
a=User.objects.get(id=3)
b=Book.objects.all()
a.liked_books.add(*b)

#Display all users who like the first book:
Book.objects.get(id=1).liked_users.all()

#Display the user who uploaded the first book
Book.objects.first().uploader.first_name

Display all users who like the second book:
Book.objects.get(id=2).liked_users.all().values()

Display the user who uploaded the second book:
Book.objects.get(id=2).uploader.first_name