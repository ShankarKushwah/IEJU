from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=60, db_column='branch_name')

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=60, db_column='semester_name')
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return self.branch


class Syllabus(models.Model):
    name = models.CharField(max_length=60, db_column='syllabus_name')
    branch = models.ForeignKey(Branch)
    semester = models.ForeignKey(Semester)
