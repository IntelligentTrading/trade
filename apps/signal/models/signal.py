import json
import logging
import boto
from boto.sqs.message import Message
from datetime import datetime
from apps.common.behaviors import Timestampable
from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

logger = logging.getLogger(__name__)


class Signal(Timestampable, models.Model):

    timestamp = UnixTimeStampField(null=False)
    transaction_currency = models.CharField(max_length=6, null=False, blank=False)
    counter_currency = models.CharField(max_length=6, null=False, blank=False)

    signal = models.CharField(max_length=15, null=True)
    trend = models.CharField(max_length=15, null=True)

    strength_value = models.IntegerField(null=True)
    strength_max = models.IntegerField(null=True)

    price = models.BigIntegerField(null=False)

    rsi_value = models.FloatField(null=True)

    # MODEL PROPERTIES


    # MODEL FUNCTIONS

    def print(self):
        logger.info("PRINTING SIGNAL DATA: " + str(self.__dict__))


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Signal, dispatch_uid="send_signal")
def send_update_portfolio(sender, instance, **kwargs):
    logging.debug("signal saved, sending update to portfolio")
    pass

