import json
import logging
import schedule
import time

from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "reads ITT signals from SNS"

    def handle(self, *args, **options):
        logger.info("Starting to read from SNS...")
        pass
