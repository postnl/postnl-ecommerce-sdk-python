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
from postnlecommerce.models.confirming_request import ConfirmingRequest


class ConfirmingControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(ConfirmingControllerTests, cls).setUpClass()
        cls.controller = cls.client.confirming
        cls.response_catcher = cls.controller.http_call_back

    # Confirm a shipment to PostNL
    def test_confirm_shipment(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"Customer":{"Address":{"AddressType":"02","City":"Den Haag","Comp'
            'anyName":"PostNL","Countrycode":"NL","HouseNr":"3","Street":"Waldo'
            'rpstraat","Zipcode":"2521CA"},"CollectionLocation":"123456","Conta'
            'ctPerson":"Janssen","CustomerCode":"DEVC","CustomerNumber":"112233'
            '44","Email":"email@company.com","Name":"Janssen"},"Message":{"Mess'
            'ageID":"1","MessageTimeStamp":"08-09-2022 12:00:00"},"Shipments":['
            '{"Addresses":[{"AddressType":"01","City":"Utrecht","Countrycode":"'
            'NL","FirstName":"Peter","HouseNr":"9","HouseNrExt":"a bis","Name":'
            '"de Ruiter","Street":"Bilderdijkstraat","Zipcode":"3532VA"}],"Barc'
            'ode":"3SDEVC748859096","Contacts":[{"ContactType":"01","Email":"re'
            'ceiver@email.com","SMSNr":"+31612345678","TelNr":"+31301234567"}],'
            '"Dimension":{"Weight":2000},"ProductCodeDelivery":"3085"}]}', ConfirmingRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.confirm_shipment(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"ResponseShipments":[{"Errors":[],"Warnings":[{"code":"1280103","'
            'description":"Address is unknown"}],"Barcode":"3SDEVC281677095"}]}'
            '')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

