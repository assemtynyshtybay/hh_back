from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    def __str__(self):
        return '{}: {}'.format(self.id,self.name)

    def __unicode__(self):
        return "%s" % self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    salary = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id,self.name)

    def __unicode__(self):
        return "%s" % self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }


