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


class PostalcodeCheckControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(PostalcodeCheckControllerTests, cls).setUpClass()
        cls.controller = cls.client.postalcode_check
        cls.response_catcher = cls.controller.http_call_back

    # Please note that this API is not available on the sandbox environment.
    #
    #Request example:
    #```
    #curl -X GET "https://api.postnl.nl/shipment/checkout/v1/postalcodecheck?postalcode=3571ZZ&amp;housenumber=74&amp;housenumberaddition=bis" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" 
    #```
    #
    def test_checkout_postalcode_check(self):
        # Parameters for the API call
        postalcode = '3571ZZ'
        housenumber = '74'
        housenumberaddition = 'bis'

        # Perform the API call through the SDK function
        result = self.controller.checkout_postalcode_check(postalcode, housenumber, housenumberaddition)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"city":"UTRECHT","postalCode":"3571ZZ","streetName":"Molengraaff'
            'plantsoen","houseNumber":74,"houseNumberAddition":"bis","formatted'
            'Address":["Molengraaffplantsoen 74 bis","3571ZZ UTRECHT"]}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

