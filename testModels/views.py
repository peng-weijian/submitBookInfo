from django.shortcuts import render,HttpResponse
from testModels import models

# Create your views here.

def add_author_info(author_name):
    author_obj = models.Author.objects.create(name=author_name)
    return author_obj   #这里一定要return一个对象，否则后面添加没法使用

def add_book_info(req):
    if req.method == 'POST':
        title = req.POST.get("title")
        author_1_name = req.POST.get("author_1")
        author_2_name = req.POST.get("author_2")
        publisher = req.POST.get("publisher")
        print("出版商:" + publisher)
        price = req.POST.get("price")
        if author_1_name:
            author_1_obj = models.Author.objects.filter(name=author_1_name).first()
            if not author_1_obj:
                print('作者1在数据库中不存在')
                author_1_obj = add_author_info(author_1_name)
        if author_2_name:
            author_2_obj = models.Author.objects.filter(name=author_2_name).first()
            if not author_2_obj:
                print('作者2在数据库中不存在')
                author_2_obj = add_author_info(author_2_name)

        # publisher_obj = models.Publisher.objects.filter(name=publisher).first()
        publisher_obj = models.Publisher.objects.get(name=publisher)

        book_obj = models.Book.objects.create(title=title, publisher=publisher_obj,price=price)
        print(author_1_obj,author_2_obj)
        book_obj.author.add(author_1_obj,author_2_obj)
        summit_status = 1
        return render(req,'addBookInfo.html',{"summit_status":summit_status})

    return render(req,'addBookInfo.html')