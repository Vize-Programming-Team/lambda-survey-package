# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class PhoneNumberTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.lookups.v1.phone_numbers(phone_number="+987654321").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://lookups.twilio.com/v1/PhoneNumbers/+987654321',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "caller_name": {
                    "caller_name": "Delicious Cheese Cake",
                    "caller_type": "CONSUMER",
                    "error_code": null
                },
                "carrier": {
                    "error_code": null,
                    "mobile_country_code": "310",
                    "mobile_network_code": "456",
                    "name": "verizon",
                    "type": "mobile"
                },
                "country_code": "US",
                "national_format": "(510) 867-5309",
                "phone_number": "+15108675309",
                "add_ons": {
                    "status": "successful",
                    "message": null,
                    "code": null,
                    "results": {}
                },
                "url": "https://lookups.twilio.com/v1/PhoneNumbers/phone_number"
            }
            '''
        ))
        
        actual = self.client.lookups.v1.phone_numbers(phone_number="+987654321").fetch()
        
        self.assertIsNotNone(actual)
