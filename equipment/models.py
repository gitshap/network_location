from statistics import mode
from django.db import models

class Building(models.Model):
    building = models.CharField(max_length=255)

    def __str__(self):
        return self.building


class Floor(models.Model):
    floor = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.floor} in {self.building}'


class Office(models.Model):
    office = models.CharField(max_length=255)

    def __str__(self):
        return self.office

class Router(models.Model):
    asset_tag = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Switch(models.Model):
    asset_tag = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    router = models.ForeignKey(Router, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Computer(models.Model):
    asset_tag = models.CharField(max_length=255)
    pc_name = models.CharField(max_length=255)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)

    is_reachable = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.pc_name
