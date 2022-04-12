from django.db import models


# create class of DjangoClasses w/ module manager
class DjangoClasses(models.Model):
    # course titles
    title = models.CharField(max_length=60)
    # course numbers with integer values
    courseNumber = models.DecimalField(max_length=60, max_digits=10000, decimal_places=2)
    # instructor names
    instructorName = models.CharField(max_length=60)
    # how long the courses last
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()


# three objects from djangoClasses
class1 = DjangoClasses(title="Virtual Environments", courseNumber=1000, instructorName="Dr Thompson", duration=1.5)
class1.save()

# three objects from djangoClasses
class2 = DjangoClasses(title="Modules", courseNumber=1100, instructorName="Dr Jackson", duration=2.0)
class2.save()

# three objects from djangoClasses
class3 = DjangoClasses(title="Templates", courseNumber=1200, instructorName="Dr Morris", duration=2.5)
class3.save()


def __str__(self):
    return self.title
