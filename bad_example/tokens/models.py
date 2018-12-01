from django.db import models
import datetime
import random
import base64
import json
from rest_framework.authtoken.models import Token
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class BadToken(models.Model):
    """
    The default authorization token model.
    """

    def __init__(self):
        super().__init__()
        self.generate_key()
        self.save()

    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(BadToken, self).save(*args, **kwargs)

    def generate_key(self):
        time = datetime.datetime.now()
        number = random.randint(0, 50)
        sentence = f'{time}{number}{time.date()}'
        sutf8 = sentence.encode("utf-8")
        self.key = base64.b64encode(sutf8)

    def __str__(self):
        return self.key
