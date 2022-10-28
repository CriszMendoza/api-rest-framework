"""
Comando Django para esperar a que la base de datos esté disponible.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comando Django para esperar la base de datos."""

    def handle(self, *args, **options):
        """Punto de entrada para el comando"""
        self.stdout.write('Waiting for database...')

        db_up = False
        count = 0

        while db_up is False or count == 6:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailible, waiting 1 second...')
                time.sleep(1)
                count += 1

        self.stdout.write(self.style.SUCCESS('Database available!'))
