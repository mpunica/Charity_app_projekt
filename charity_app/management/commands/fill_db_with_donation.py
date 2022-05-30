from django.core.management.base import BaseCommand
from charity_app.models import Institution, Category, Donation
from django.contrib.auth.models import User
from datetime import date, datetime


class Command(BaseCommand):
    help = "Adding some examples to db"

    def handle(self, *args, **options):

        # User.objects.create(
        #     password=111,
        #     is_superuser=False,
        #     username="monika2",
        #     first_name="mon",
        #     last_name="go",
        #     email="globalmongo@gmail.com",
        #     is_staff=True,
        #     is_active=True,
        #     # date_joined=datetime(2021, 6, 30, 11, 30, 44),
        # )

        Category.objects.create(
            name="ubrania które nadają się do ponownego użycia",
        )
        Category.objects.create(
            name="ubrania do wyrzucenia",
        )
        Category.objects.create(
            name="zabawki",
        )
        Category.objects.create(
            name="książki",
        )
        Category.objects.create(
            name="inne",
        )

        Institution.objects.create(
            name="Fundacja Kierunek Przygoda",
            description="Podstawowym celem Fundacji „KIERUNEK PRZYGODA” jest stwarzanie warunków do prawidłowego rozwoju psychoruchowego dzieci i młodzieży oraz do pozytywnego kształtowania ich charakteru, propagowanie postaw proekologicznych w duchu szacunku do innych istnień, organizacja czasu wolnego oraz wypoczynku letniego i zimowego, wspólne z dziećmi i ich rodzicami poznawanie tradycji naszego regionu i kraju.",
            type=0,
            # categories=Category.objects.get(id=2),
        )
        Institution.objects.create(
            name="Organizacja Książka dla nastolatki",
            description="Podstawowym celem Organizacji jest stwarzanie warunków do czytania dla nastolatków",
            type=1,
            # categories=Category.objects.get(id=3),
        )
        Institution.objects.create(
            name="Organizacja Książka dla chłopaka",
            description="Podstawowym celem Organizacji jest stwarzanie warunków do czytania dla chłopców",
            type=1,
            # categories=Category.objects.get(id=3),
        )

        Institution.objects.create(
            name="StartUp sąsiedzki",
            description="Podstawowym celem jest zebranie funduszy na górkę saneczkową z siłownią dla seniorów i miejscem na piknik",
            type=2,
            # categories=Category.objects.get(id=4),
        )

        Donation.objects.create(
            quantity=2,
            # categories="książki",
            institution=Institution.objects.get(id=2),
            address="ul. Sąsiedzka , Kiełczów",
            phone_number=222222222,
            zip_code="55-093",
            pick_up_date = date(year=2021, month=7, day=29),
            pick_up_time = "11:30",
            pick_up_comment = "książki dla młodzieży",
            user=User.objects.get(id=1),
        )