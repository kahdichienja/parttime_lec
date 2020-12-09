from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    """Model definition for Department."""

    # TODO: Define fields here
    name = models.CharField(max_length =191)

    def __str__(self):
        """Unicode representation of Department."""
        return f"{self.name}"

    # TODO: Define custom methods here


class StaffProfile(models.Model):
    """Model definition for StaffProfile."""

    # TODO: Define fields here
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_level = models.CharField(max_length = 191)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lecturer_sirname = models.CharField(max_length = 191)
    other_name = models.CharField(max_length = 191)
    email = models.EmailField()
    address = models.CharField(max_length = 191)
    tel = models.CharField(max_length = 191)
    user_id_or_pe_nember = models.CharField(max_length = 191)



    def __str__(self):
        """Unicode representation of StaffProfile."""
        return f'{self.lecturer_sirname} {self.other_name}'



    # TODO: Define custom methods here


class Unit(models.Model):
    """Model definition for Unit."""

    # TODO: Define fields here 
    name = models.CharField(max_length =191)
    code = models.CharField(max_length =191)



    def __str__(self):
        """Unicode representation of Unit."""
        return f'{self.name} : {self.code}'


    # TODO: Define custom methods here


class AccademicSession(models.Model):
    """Model definition for AccademicSession."""

    # TODO: Define fields here
    semester = models.CharField(max_length =191)
    accademic_year = models.CharField(max_length =191)
    session = models.CharField(max_length =191)

    


    def __str__(self):
        """Unicode representation of AccademicSession."""
        return f'{self.semester}:{self.accademic_year}:{self.session}'

    # TODO: Define custom methods here



class Report(models.Model):
    """Model definition for AccademicSession."""

    # TODO: Define fields here
    staffprofile = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    accademicsession = models.ForeignKey(AccademicSession, on_delete=models.CASCADE)

    def __str__(self):
        """Unicode representation of AccademicSession."""
        return f'{self.staffprofile} Report'

    # TODO: Define custom methods here
