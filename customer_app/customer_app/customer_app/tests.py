import unittest
import pytest
from django.test import TestCase
# from unittesttest import TestCase
from ..customer_app.forms import CustomerForm


@pytest.fixture
def valid_form_data():
	return {
		'first_name': 'John',
		'last_name': 'Doe',
		'address': '123 Main St',
		'city': 'Anytown',
		'zip_code': '12345',
		'state': 'NY'
	}

@pytest.fixture
def invalid_form_data():
	return {
		'first_name': '',
		'last_name': 'Doe',
		'address': '123 Main St',
		'city': 'Anytown',
		'zip_code': '12345',
		'state': 'NY'
	}

@pytest.mark.django_db
class TestCustomerForm(TestCase):
	def test_valid_form(self, valid_form_data):
		form = CustomerForm(data=valid_form_data)
		assert form.is_valid()

	def test_empty_string(self, invalid_form_data):
		form = CustomerForm(data=invalid_form_data)
		assert not form.is_valid()