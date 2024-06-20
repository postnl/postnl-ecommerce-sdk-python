# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.checkout_request import CheckoutRequest


class CheckoutControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(CheckoutControllerTests, cls).setUpClass()
        cls.controller = cls.client.checkout
        cls.response_catcher = cls.controller.http_call_back

    # Checkout
    def test_checkout(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"OrderDate":"24-02-2021 12:00:00","ShippingDuration":1,"CutOffTim'
            'es":[{"Day":"00","Available":true,"Type":"Regular","Time":"20:00:0'
            '0"},{"Day":"00","Available":true,"Type":"Today","Time":"12:00:00"}'
            '],"HolidaySorting":true,"Options":["Daytime","Evening","Today","Su'
            'nday","Pickup"],"Locations":2,"Days":3,"Addresses":[{"AddressType"'
            ':"01","Street":"Molengraaffplantsoen","HouseNr":74,"Zipcode":"3571'
            'ZZ","City":"Utrecht","Countrycode":"NL"}]}', CheckoutRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.checkout(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"DeliveryOptions":[{"DeliveryDate":"09-07-2019","Timeframe":[{"Fr'
            'om":"18:00:00","To":"22:30:00","Options":["Daytime"],"ShippingDate'
            '":"08-07-2019","Sustainability":{"Code":"02","Description":"Sustai'
            'nable option"}}]}],"PickupOptions":[{"PickupDate":"09-07-2019","Sh'
            'ippingDate":"08-07-2019","Option":"Pickup","Locations":[{"Address"'
            ':{"Street":"Siriusdreef","Zipcode":"2132WT","HouseNr":42,"HouseNrE'
            'xt":"-60","Countrycode":"NL","CompanyName":"Pickup company BV"},"P'
            'ickupTime":"15:00","OpeningHours":{"Monday":{"From":"08:30:00","To'
            '":"22:30:00"},"Tuesday":{"From":"08:30:00","To":"22:30:00"},"Wedne'
            'sday":{"From":"08:30:00","To":"22:30:00"},"Thursday":{"From":"08:3'
            '0:00","To":"22:30:00"},"Friday":{"From":"08:30:00","To":"22:30:00"'
            '},"Saturday":{"From":"08:30:00","To":"22:30:00"},"Sunday":{"From":'
            '"08:30:00","To":"22:30:00"}},"Distance":234,"LocationCode":"810116'
            '3043","PartnerID":"PNPNL-01","Sustainability":{"Code":"02","Descri'
            'ption":"Sustainable option"}}]}],"Warnings":[{"DeliveryDate":"07-0'
            '7-2019","Code":"5034","Description":"No delivery option found on d'
            'ate","Options":"Daytime"}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

