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
from postnlecommerce.models.labelling_request import LabellingRequest


class LabellingControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(LabellingControllerTests, cls).setUpClass()
        cls.controller = cls.client.labelling
        cls.response_catcher = cls.controller.http_call_back

    # Generate a label and confirmation
    def test_generate_label(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"Customer":{"Address":{"AddressType":"02","City":"Den Haag","Comp'
            'anyName":"PostNL","Countrycode":"NL","HouseNr":"3","Street":"Waldo'
            'rpstraat","Zipcode":"2521CA"},"CollectionLocation":"123456","Conta'
            'ctPerson":"Janssen","CustomerCode":"DEVC","CustomerNumber":"112233'
            '44","Email":"email@company.com","Name":"Janssen"},"Message":{"Mess'
            'ageID":"1","MessageTimeStamp":"08-09-2022 12:00:00","Printertype":'
            '"GraphicFile|PDF"},"Shipments":[{"Addresses":[{"AddressType":"01",'
            '"City":"Utrecht","Countrycode":"NL","FirstName":"Peter","HouseNr":'
            '"9","HouseNrExt":"a bis","Name":"de Ruiter","Street":"Bilderdijkst'
            'raat","Zipcode":"3532VA"}],"Barcode":"3SDEVC748859096","Contacts":'
            '[{"ContactType":"01","Email":"receiver@email.com","SMSNr":"+316123'
            '45678","TelNr":"+31301234567"}],"Dimension":{"Weight":2000},"Produ'
            'ctCodeDelivery":"3085"}]}', LabellingRequest.from_dictionary)
        confirm = True

        # Perform the API call through the SDK function
        result = self.controller.generate_label(body, confirm)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"MergedLabels":[],"ResponseShipments":[{"Barcode":"3SDEVC27273080'
            '3","Errors":[],"Warnings":[],"Labels":[{"Content":"JVBERi0xLjMKJeL'
            'jz9MKNSAwIG9iago8PAovQ29udGVudHMg[TRUNCATED]","Labeltype":"Label",'
            '"OutputType":"PDF"}],"ProductCodeDelivery":"3085"}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

