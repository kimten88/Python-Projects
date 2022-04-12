from django.db import models

# three objects from djangoClasses
TITLE_CHOICES = {
    ('Virtual Environments', 'Virtual Environments'),
    ('Models', 'Models'),
    ('Templates', 'Templates'),
}


# create class of DjangoClasses w/ module manager
class DjangoClasses(models.Model):
    # course titles
    title = models.CharField(max_length=60, choices=TITLE_CHOICES)
    # course numbers with integer values
    courseNumber = models.DecimalField(max_length=60, max_digits=10000, decimal_places=2)
    # instructor names
    instructorName = models.CharField(max_length=60)
    # how long the courses last
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title
