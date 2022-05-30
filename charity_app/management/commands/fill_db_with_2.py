from django.core.management.base import BaseCommand
from charity_app.models import Institution, Category, Donation
from django.contrib.auth.models import User
from datetime import date, datetime

class Command(BaseCommand):
    help = "Adding some examples to db"

    def handle(self, *args, **options):

        Institution.objects.create(
            name="Fundacja Kierunek Przygoda",
            description="Podstawowym celem Fundacji „KIERUNEK PRZYGODA” jest stwarzanie warunków do prawidłowego rozwoju psychoruchowego dzieci i młodzieży oraz do pozytywnego kształtowania ich charakteru, propagowanie postaw proekologicznych w duchu szacunku do innych istnień, organizacja czasu wolnego oraz wypoczynku letniego i zimowego, wspólne z dziećmi i ich rodzicami poznawanie tradycji naszego regionu i kraju.",
            type=0,
            get insgt

            # categories=Category.objects.add(id=2),

        #     Przykład
        # add()
        # t1 = Topping.objects.create(name='anchovies', price=3.50)
        # t2 = Topping.objects.create(name='onion', price=2.00)
        # p = Pizza.objects.create(size=1)  # mała pizza
        # p.toppings.add(t1)
        # p.toppings.add(t2)