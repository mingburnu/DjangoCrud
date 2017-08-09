from trips.models import City


def all():
    cs = City.objects.all()
    for c in cs:
        print(c.location + '\n')


all()
