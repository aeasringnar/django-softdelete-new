### Django-softdelete-new

基于Django的轻量级软删除插件，支持Django>=1.11。

#### 快速开始

1、安装插件

```bash
pip install django-softdelete-new
```

2、导入基本Model

```bash
from soft_delete_new.models import SoftDeleteModel
```

3、将`SoftDeleteModel`类继承到模型类。它将添加以下功能：

​	`objects`的行为将发生以下变化：

​		返回所有非软删除的数据对象

​		delete() 方法将变成软删除方法。

​		hard_delete() 增加的方法，将数据真正从数据库中删除。

​	`all_objects` 是新增加的行为：

​		将始终返回软删除和非软删除的对象

​		only_deleted() 仅返回软删除对象的方法

​		undelete() 可以将`all_objects`返回的已经软删除的对象置为非软删除。

#### 实例

```python
from django.db import models
from soft_delete_it.models import SoftDeleteModel


class Author(SoftDeleteModel):
    name = models.CharField(max_length=50)
    dob = models.DateField()


class Article(SoftDeleteModel):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')


Bob = Author.objects.create(name='bob', dob='2000-12-12')
John = Author.objects.create(name='john', dob='1990-10-12')

Author.objects.all() # return QuerySet with 2 objects
Bob.delete() # Bob is soft-deleted
Author.objects.all() # return QuerySet with 1 object, John
Author.all_objects.all() # return QuerySet with 2 object, Bob and John
Bob.undelete() # un-deletes Bob object
Author.objects.all() # return QuerySet with 2 objects


article1 = Article(title='Bob The Builder', body='')
article1.author = Bob
article1.save()

Article.objects.all() # return QuerySet with 1 object, article1

Bob.delete() # soft-deletes both Bob and article1 as Article's author field is on_delete_cascade and it Inherits SoftDeleteModel
```