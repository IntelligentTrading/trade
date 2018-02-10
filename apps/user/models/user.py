import json
import uuid
import logging

from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.common.behaviors import Timestampable
import os


class User(AbstractUser, Timestampable):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

User._meta.get_field('username')._unique = False
