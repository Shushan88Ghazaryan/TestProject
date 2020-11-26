from django.db import models
# from django_rest import serializers

class Country(models.Model):
    state=models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    dates = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    class Meta:
        verbose_name_plural='Country'
    def __str__(self):
        return '{} {}'.format(self.state, self.capital)

# class Language(models.Model):
#     prog_lang=[
#         ('Java','Java'),
#         ('Py','Python'),
#         ('JS','JavaScript'),
#         ('C','C++'),
#         ('Asm','Asembler'),
#     ]
#     lang=models.CharField(max_length=50,choices=prog_lang)
# class Style(models.Model):
#     prog_style=[
#         ('Web','Frontend'),
#         ('Web','Backend'),
#         ('M','Mobile'),
#         ('A','AI')
#
#     ]
#     st=models.CharField(max_length=50,choices=prog_style)
# class Choice(models.Model):
#     langknow=models.ManyToManyField(Language)
#     stknow=models.ForeignKey(Style,on_delete=models.CASCADE)
# class Prog_lang(models.Model):
#     language=models.CharField(max_length=30)
# class Tech(models.Model):
#     name=models.CharField(max_length=30)
# class Worker(models.Model):
#     name=models.CharField(max_length=30)
#     surname=models.CharField(max_length=30)
#     age=models.SmallIntegerField()
#     rating=models.SmallIntegerField()
#     language=models.ManyToManyField(Prog_lang)
#     technology=models.ForeignKey(Tech,on_delete=models.CASCADE)