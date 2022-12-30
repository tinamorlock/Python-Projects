from django.db import models

# Creates model of University Campuses

class UniversityCampus(models.Model):
    campus_ID = models.IntegerField(default="", blank=True, null=False)
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_state = models.CharField(max_length=2, default="", blank=True, null=False)

    # creates model manager

    object = models.Manager()

    # displays the object output values in the form of a string
    # this needs to be detailed enough so user knows which one it is
    # but does not need to include all fields

    def __str__(self):
        # returns the input value of the campus name and state
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name} - {0.campus_state}'
        return display_campus.format(self)

    # removes added s that Django adds to the model name in the browser display

    class Meta:
        verbose_name_plural = "University Campus"