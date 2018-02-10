import json
import logging
import schedule
import time

from django.core.management.base import BaseCommand

from apps.portfolio.models import Exchange

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "balances portfolios"



    def handle(self, *args, **options):
        logger.info("Analyzing portfolios")
        exchanges = Exchange.objects.all()
        USD_balance = self.get_total_USD_balance(exchanges)

        logger.info("Preparing opportunity assessment")
        # load sns signals and prioritize their addition to virtual portfolio

        logger.info("Running risk assessment")
        # re-balance portfolio to mitigate any risks

        # calculate difference between actual and desired portfolio

        # calculate shortest path and compile list of trades

        # drop small trades from the list

        # place orders and set watch configs

        # assign order watchers

        pass



    def get_total_USD_balance(self, exchanges):
        total_USD_balance = 0.0
        for exchange in exchanges:
            try:
                total_USD_balance += exchange.get_USD_balance()
            except:
                logging.error("error checking balance on %s exchange: %d" %
                              (exchange.get_exchange_display()(), exchange.id))
        return total_USD_balance

