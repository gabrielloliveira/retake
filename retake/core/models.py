import uuid

from django.db import models


class TimeStampedModel(models.Model):
    uuid = models.UUIDField("UUID", unique=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        abstract = True


class Process(TimeStampedModel):
    number = models.CharField("número", max_length=255, unique=True)
    class_name = models.CharField("classe", max_length=255)
    subject = models.CharField("assunto", max_length=255)
    judge = models.CharField("juíz", max_length=255)
    parts = models.ManyToManyField("Part", verbose_name="partes", blank=True)

    @property
    def parts_names(self):
        return [f"{x.name} - {x.category}" for x in self.parts.all()]

    def __str__(self):
        return self.number


class Part(TimeStampedModel):
    name = models.CharField("nome", max_length=255)
    category = models.CharField("categoria", max_length=255)

    def __str__(self):
        return self.name
