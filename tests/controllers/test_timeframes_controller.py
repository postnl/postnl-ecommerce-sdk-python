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


class TimeframesControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(TimeframesControllerTests, cls).setUpClass()
        cls.controller = cls.client.timeframes
        cls.response_catcher = cls.controller.http_call_back

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/calculate/timeframes?AllowSundaySorting=false&StartDate=30-06-2022&EndDate=02-07-2022&CountryCode=NL&PostalCode=2132WT&HouseNumber=42&HouseNrExt=A&City=Hoofddorp&Street=Siriusdreef&Options=Daytime%2CEvening" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_retrieve_delivery_timeframes(self):
        # Parameters for the API call
        allow_sunday_sorting = False
        start_date = '30-06-2022'
        end_date = '02-07-2022'
        country_code = 'NL'
        postal_code = '2132WT'
        house_number = 42
        options = APIHelper.json_deserialize('["Daytime","Evening","Sunday"]')
        house_nr_ext = 'A'
        city = 'Hoofddorp'
        street = 'Siriusdreef'

        # Perform the API call through the SDK function
        result = self.controller.retrieve_delivery_timeframes(allow_sunday_sorting, start_date, end_date, country_code, postal_code, house_number, options, house_nr_ext, city, street)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"Timeframes":{"Timeframe":[{"Date":"02-07-2022","Timeframes":{"Ti'
            'meframeTimeframe":[{"From":"12:30:00","Options":{"string":"Daytime'
            '"},"To":"14:30:00","Sustainability":{"Code":"02","Description":"Su'
            'stainable option"}}]}}]},"ReasonNoTimeframes":{"ReasonNoTimeframe"'
            ':[{"Code":"1","Date":"02-07-2022","Description":"Delivery date not'
            ' allowed","Options":{"string":"Evening"},"Sustainability":{"Code":'
            '"02","Description":"Sustainable option"}}]}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

