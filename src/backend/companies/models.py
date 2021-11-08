from django.db import models


class Company(models.Model):
    corp_code = models.CharField(max_length=100, blank=False, db_index=True)  # 회사코드
    stock_code = models.CharField(max_length=100, blank=True, db_index=True)  # 종목코드
    name = models.CharField(max_length=100, blank=False, db_index=True)  # 종목이름
    modify_date = models.DateField()

    def __str__(self):
        return f"{self.stock_code} {self.name}"
