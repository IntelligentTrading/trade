import json
import logging
import boto
from boto.sqs.message import Message
from datetime import datetime
from apps.common.behaviors import Timestampable
from django.db import models

logger = logging.getLogger(__name__)

(BITTREX, BINANCE, KUCOIN, TDAX) = list(range(4))
EXCHANGE_CHOICES = (
    (BITTREX, 'BITTREX'),
    (BINANCE, 'BINANCE'),
    (KUCOIN, 'KUCOIN'),
    (TDAX, 'TDAX'),
)

class Exchange(Timestampable, models.Model):

    exchange = models.IntegerField(choices=EXCHANGE_CHOICES)
    api_key_encrypted = models.CharField(max_length=200, default="")
    api_secret_encrypted = models.CharField(max_length=200, default="")


    # MODEL PROPERTIES
    @property
    def api_key(self):
        from apps.common.utilities.encrypt_decrypt import decrypt
        return decrypt(self.api_key_encrypted)

    @api_key.setter
    def api_key(self, value):
        from apps.common.utilities.encrypt_decrypt import encrypt
        self.api_key_encrypted = encrypt(value)

    @property
    def api_secret(self):
        from apps.common.utilities.encrypt_decrypt import decrypt
        return decrypt(self.api_secret_encrypted)

    @api_secret.setter
    def api_secret(self, value):
        from apps.common.utilities.encrypt_decrypt import encrypt
        self.api_secret_encrypted = encrypt(value)


    # MODEL FUNCTIONS

    def print(self):
        logger.info("PRINTING SIGNAL DATA: " + str(self.__dict__))


from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Exchange, dispatch_uid="send_signal")
def send_update_portfolio(sender, instance, **kwargs):
    logging.debug("signal saved, sending update to portfolio")
    pass
