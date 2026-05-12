from django.db import models


class Budget(models.Model):

    month = models.CharField(max_length=20)

    income = models.IntegerField()

    expense = models.IntegerField()

    profit = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        self.profit = self.income - self.expense

        super().save(*args, **kwargs)

    def __str__(self):

        return self.month