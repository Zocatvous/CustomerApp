from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
	class StateChoices(models.TextChoices):
		ALABAMA = 'AL', 'Alabama'
		ALASKA = 'AK', 'Alaska'
		ARIZONA = 'AZ', 'Arizona'
		ARKANSAS = 'AR', 'Arkansas'
		CALIFORNIA = 'CA', 'California'
		COLORADO = 'CO', 'Colorado'
		CONNECTICUT = 'CT', 'Connecticut'
		DELAWARE = 'DE', 'Delaware'
		FLORIDA = 'FL', 'Florida'
		GEORGIA = 'GA', 'Georgia'
		HAWAII = 'HI', 'Hawaii'
		IDAHO = 'ID', 'Idaho'
		ILLINOIS = 'IL', 'Illinois'
		INDIANA = 'IN', 'Indiana'
		IOWA = 'IA', 'Iowa'
		KANSAS = 'KS', 'Kansas'
		KENTUCKY = 'KY', 'Kentucky'
		LOUISIANA = 'LA', 'Louisiana'
		MAINE = 'ME', 'Maine'
		MARYLAND = 'MD', 'Maryland'
		MASSACHUSETTS = 'MA', 'Massachusetts'
		MICHIGAN = 'MI', 'Michigan'
		MINNESOTA = 'MN', 'Minnesota'
		MISSISSIPPI = 'MS', 'Mississippi'
		MISSOURI = 'MO', 'Missouri'
		MONTANA = 'MT', 'Montana'
		NEBRASKA = 'NE', 'Nebraska'
		NEVADA = 'NV', 'Nevada'
		NEW_HAMPSHIRE = 'NH', 'New Hampshire'
		NEW_JERSEY = 'NJ', 'New Jersey'
		NEW_MEXICO = 'NM', 'New Mexico'
		NEW_YORK = 'NY', 'New York'
		NORTH_CAROLINA = 'NC', 'North Carolina'
		NORTH_DAKOTA = 'ND', 'North Dakota'
		OHIO = 'OH', 'Ohio'
		OKLAHOMA = 'OK', 'Oklahoma'
		OREGON = 'OR', 'Oregon'
		PENNSYLVANIA = 'PA', 'Pennsylvania'
		RHODE_ISLAND = 'RI', 'Rhode Island'
		SOUTH_CAROLINA = 'SC', 'South Carolina'
		SOUTH_DAKOTA = 'SD', 'South Dakota'
		TENNESSEE = 'TN', 'Tennessee'
		TEXAS = 'TX', 'Texas'
		UTAH = 'UT', 'Utah'
		VERMONT = 'VT', 'Vermont'
		VIRGINIA = 'VA', 'Virginia'
		WASHINGTON = 'WA', 'Washington'
		WEST_VIRGINIA = 'WV', 'West Virginia'
		WISCONSIN = 'WI', 'Wisconsin'
		WYOMING = 'WY', 'Wyoming'

	first_name = models.CharField(validators=[MinLengthValidator(1)], max_length=100)
	last_name = models.CharField(max_length=100)
	address = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=10)
	state = models.CharField(max_length=2, choices=StateChoices.choices)

	def __str__(self):
		return f"<Customer:{self.first_name} {self.last_name}>"