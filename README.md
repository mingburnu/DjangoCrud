# DjangoCrud

> pip install ipython

> mkdir templates

> python manage.py startapp trips

[edit /DjangoCrud/settings.py](https://github.com/mingburnu/DjangoCrud/blob/master/DjangoCrud/settings.py)

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        },
    ]

    INSTALLED_APPS = [
        ...
        'trips',
    ] 



[edit /DjangoCrud/trips/models.py](https://github.com/mingburnu/DjangoCrud/blob/master/trips/models.py)

    from django.db import models


    class City(models.Model):
        location = models.CharField(max_length=100)

        def __str__(self):
            return self.location


[edit /DjangoCrud/trips/admin.py](https://github.com/mingburnu/DjangoCrud/blob/master/trips/admin.py)
   
    admin.site.register(City)


> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

[edit DjangoCrud/trips/views.py](https://github.com/mingburnu/DjangoCrud/blob/master/trips/views.py)

[edit DjangoCrud/trips/urls.py](https://github.com/mingburnu/DjangoCrud/blob/master/trips/urls.py)

[edit DjangoCrud/urls.py](https://github.com/mingburnu/DjangoCrud/blob/master/DjangoCrud/urls.py)

[edit DjangoCrud/templates/trips/xxxx.html](https://github.com/mingburnu/DjangoCrud/tree/master/templates)

[127.0.0.1:8000](http://127.0.0.1:8000)

[edit /DjangoCrud/script.py](https://github.com/mingburnu/DjangoCrud/blob/master/script.py)
> python manage.py shell < script.py

### REFERECE
[Django CRUD Example Apps](https://github.com/rayed/django_crud)
[Effective Django Forms](http://www.effectivedjango.com/forms.html)
[Django 的 CBV 最佳实践](http://www.atjiang.com/2scoopsdjango1.8-10-best-practices-for-CBV/)
[Form fields](https://docs.djangoproject.com/en/dev/ref/forms/fields/)
[Introduction to class-based views](https://docs.djangoproject.com/en/1.11/topics/class-based-views/intro/)
[Python菜鸟之路](http://www.cnblogs.com/jishuweiwang/p/6362859.html)
