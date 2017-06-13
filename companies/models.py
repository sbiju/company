from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=150, default='abc')
    location = models.CharField(verbose_name='Location', max_length=150, blank=True, null=True)
    no_of_staff = models.IntegerField(verbose_name='No.of Employees', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['-timestamp']


class Employee(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(verbose_name='Employee Role', max_length=150, blank=True, null=True)
    age = models.IntegerField(verbose_name='Age', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']


class Opening(models.Model):
    company = models.ForeignKey(Company)
    role = models.CharField(verbose_name='Role Name', max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Job Opening'
        verbose_name_plural = 'Job Openings'
        ordering = ['-timestamp']