"""
Test - módulo calc.
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Prueba del módulo cal."""

    def test_add_numbers(self):
        """Prueba de sumar números."""
        res = calc.add(5, 10)

        self.assertEqual(res, 15)

    def test_substract_numbers(self):
        """Prueba de restar números."""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
