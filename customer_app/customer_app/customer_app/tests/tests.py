import unittest
import pytest
# from unittesttest import TestCase
from ..forms import CustomerForm


class TestCustomerForm(unittest.TestCase):
	def test_valid_form(self):
		valid_form_data = {
		'first_name': 'JAKE',
		'last_name': 'SNAKE',
		'address': '123 valid St',
		'city': 'Anytown',
		'zip_code': '12345',
		'state': 'NY'}

		form = CustomerForm(data=valid_form_data)
		assert form.is_valid()

	def test_empty_first_name_string(self):
		invalid_form_data = {
		'first_name': '',
		'last_name': 'LIZARD',
		'address': '123 Emptystring St',
		'city': 'Anytown',
		'zip_code': '12345',
		'state': 'NY'}

		form = CustomerForm(data=invalid_form_data)
		assert not form.is_valid()