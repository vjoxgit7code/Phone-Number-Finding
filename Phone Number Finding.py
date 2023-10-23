import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

phone_numbers=input("enter the Ph no:\n")
ph_no=phonenumbers.parse(phone_numbers)
tz=timezone.time_zones_for_geographical_number(ph_no)
print("Timezone:",str(tz))
geo=geocoder.description_for_number(ph_no,'en')
print("Geo:",str(geo))
cc=carrier.name_for_number(ph_no,'en')
print("Carrier:",str(cc))

