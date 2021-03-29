import csv

from cats.models import Info, Breed, Cat

def run():
    fhand = open('scripts/meow.csv')
    reader  = csv.reader(fhand)
    next(reader)

    Info.objects.all().delete()
    Breed.objects.all().delete()

    for row in reader:
        print(row)

        b, created = Breed.objects.get_or_create(name=row[1])

        i = Cat(nickname=row[0], breed=b, weight=row[2])
        i.save()
        