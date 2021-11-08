import datetime
from django.core.management.base import BaseCommand
from companies.models import Company
from dartapi import DartAPI


class Command(BaseCommand):
    help = "This command seed company dart api."

    def handle(self, *args, **options):
        dart = DartAPI()
        corp_list = dart.get_corp_code()
        for corp in corp_list:
            stock_code = corp["stock_code"].replace(" ", "")
            # stock code 없는 경우 제외
            if not stock_code:
                continue
            Company.objects.create(
                corp_code=corp["corp_code"],
                stock_code=corp["stock_code"],
                name=corp["corp_name"],
                modify_date=datetime.datetime.strptime(corp["modify_date"], "%Y%m%d"),
            )
            name = corp["corp_name"]
            self.stdout.write(self.style.SUCCESS(f"{name} company Created"))
