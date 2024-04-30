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


class DeliverydateControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(DeliverydateControllerTests, cls).setUpClass()
        cls.controller = cls.client.deliverydate
        cls.response_catcher = cls.controller.http_call_back

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/shipping?DeliveryDate=30-05-2022&amp;ShippingDuration=1&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #
    #```
    #
    def test_calculate_shipping_date(self):
        # Parameters for the API call
        delivery_date = '30-05-2022'
        shipping_duration = 1
        postal_code = '2132WT'
        country_code = 'NL'
        origin_country_code = 'NL'
        city = 'Hoofddorp'
        street = 'Siriusdreef'
        house_number = 42
        house_nr_ext = 'A'

        # Perform the API call through the SDK function
        result = self.controller.calculate_shipping_date(delivery_date, shipping_duration, postal_code, country_code, origin_country_code, city, street, house_number, house_nr_ext)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


