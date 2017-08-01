# DjangoCrud

> pip install ipython

> mkdir templates

> python manage.py startapp trips

<a href="https://github.com/mingburnu/DjangoCrud/blob/master/DjangoCrud/settings.py">edit /DjangoCrud/settings.py</a>

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



<a href="https://github.com/mingburnu/DjangoCrud/blob/master/trips/models.py">edit /DjangoCrud/trips/models.py</a>

    from django.db import models


    class City(models.Model):
        location = models.CharField(max_length=100)

        def __str__(self):
            return self.location


<a href="https://github.com/mingburnu/DjangoCrud/blob/master/trips/admin.py">edit /DjangoCrud/trips/admin.py</a>
   
    admin.site.register(City)


> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

<a href="https://github.com/mingburnu/DjangoCrud/blob/master/trips/views.py">edit DjangoCrud/trips/views.py</a>

<a href="https://github.com/mingburnu/DjangoCrud/blob/master/trips/urls.py">edit DjangoCrud/trips/urls.py</a>

<a href="https://github.com/mingburnu/DjangoCrud/blob/master/DjangoCrud/urls.py">edit DjangoCrud/urls.py</a>

<a href="https://github.com/mingburnu/DjangoCrud/tree/master/templates">edit DjangoCrud/templates/trips/xxxx.html</a>

<a href="http://127.0.0.1:8000">127.0.0.1:8000</a><br>

### REFERECE
<a href="https://github.com/rayed/django_crud">Django CRUD Example Apps</a><br>
<a href="http://www.effectivedjango.com/forms.html">Effective Django Forms</a><br>
<a href="http://www.atjiang.com/2scoopsdjango1.8-10-best-practices-for-CBV/">Django 的 CBV 最佳实践</a><br>
<a href="https://docs.djangoproject.com/en/dev/ref/forms/fields/">Form fields</a><br>
<a href="https://docs.djangoproject.com/en/1.11/topics/class-based-views/intro/">Introduction to class-based views</a><br>
<a href="http://www.cnblogs.com/jishuweiwang/p/6362859.html">Python菜鸟之路</a><br>
