from django.db import models
from django.utils import timezone
from django.urls import reverse

STATUS = (
    ('1', "Безработный"),
    ('2', "Студент"),
    ('3', "Работник"),
)

CURRENT_POSITION = (
    ('1', "IT"),
    ('2', "BA/ECO"),
    ('3', "IR"),
    ('4', "LNG"),
    ('5', "CHN"),
    ('6', "LAW"),
    ('7', "Другое"),
)


class Info(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24)
    location = models.CharField(max_length=150)
    job = models.CharField(choices=STATUS, max_length=24)
    position = models.CharField(choices=CURRENT_POSITION, max_length=24)
    created_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    email = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    photo = models.ImageField

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    is_published = models.BooleanField(default=True)

    # def get_absolute_url(self):
    #     return reverse('books:detail', args=[self.id])

    def __str__(self):
        return self.title


# ---------------------------
# import the standard Django Model
# from built-in library


# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
    # fields of the model
    title = models.CharField(max_length=200)
    description = models.TextField()

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('create_some', kwargs={"id": self.id})  # f"/show_some/{self.id}"
