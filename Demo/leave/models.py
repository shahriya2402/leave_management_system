from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Addm(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    mid = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    fdate = models.CharField(max_length=50)
    cno = models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    man_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.f_name


class Dept(models.Model):
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.dept

class Gender(models.Model):
    gen = models.CharField(max_length=50)

    def __str__(self):
        return self.gen

class Job(models.Model):
    job = models.CharField(max_length=50)

    def __str__(self):
        return self.job



class Hr_login(models.Model):
    email = models.CharField(max_length=50)
    n_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Addemp(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    eid = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    fdate = models.CharField(max_length=50)
    cno = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    e_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.f_name


class Man_login(models.Model):
    email = models.CharField(max_length=25)
    mid = models.CharField(max_length=25)
    f_name = models.CharField(max_length=25)
    man_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.email


class E_login(models.Model):
    eid = models.CharField(max_length=5)
    f_name = models.CharField(max_length=25)
    e_pass = models.CharField(max_length=10)

    def __str__(self):
        return self.eid

class Eleave(models.Model):
    eid = models.CharField(max_length=5)
    f_name = models.CharField(max_length=50)
    sdate = models.CharField(max_length=15)
    edate = models.CharField(max_length=15)
    ltype = models.CharField(max_length=50)

    def __str__(self):
        return self.eid

class Mleave(models.Model):
    mid = models.CharField(max_length=5)
    f_name = models.CharField(max_length=5)
    sdate = models.CharField(max_length=15)
    edate = models.CharField(max_length=15)
    ltype = models.CharField(max_length=50)

    def __str__(self):
        return self.mid


class Viewleave(models.Model):
    eid = models.CharField(max_length=5)
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.eid

class Viewleave1(models.Model):
    mid = models.CharField(max_length=5)
    status1 = models.CharField(max_length=15)

    def __str__(self):
        return self.mid

class Ltype(models.Model):
    ltype = models.CharField(max_length=50)

    def __str__(self):
        return self.ltype


class Acceptreject(models.Model):
    eid = models.CharField(max_length=5)
    f_name = models.CharField(max_length=50)
    sdate = models.CharField(max_length=15)
    edate = models.CharField(max_length=15)
    ltype = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.eid

class Acceptreject1(models.Model):
    mid = models.CharField(max_length=5)
    f_name = models.CharField(max_length=50)
    sdate = models.CharField(max_length=15)
    edate = models.CharField(max_length=15)
    ltype = models.CharField(max_length=50)
    status1 = models.CharField(max_length=20)

    def __str__(self):
        return self.mid




