from django.db import models


class Company(models.Model):
    corp_code = models.CharField(max_length=100, blank=False)  # 회사코드
    stock_code = models.CharField(max_length=100, blank=True)  # 종목코드
    name = models.CharField(max_length=100, blank=False)  # 종목이름
    modify_date = models.DateTimeField()

    def __str__(self):
        return f"{self.stock_code} {self.name}"
