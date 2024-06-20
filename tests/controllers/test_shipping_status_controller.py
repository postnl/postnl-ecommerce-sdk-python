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


class ShippingStatusControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(ShippingStatusControllerTests, cls).setUpClass()
        cls.controller = cls.client.shipping_status
        cls.response_catcher = cls.controller.http_call_back

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/barcode/3SDEVC172649258" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_get_status_by_barcode(self):
        # Parameters for the API call
        barcode = '3SDEVC172649258'
        detail = False
        language = 'NL'
        max_days = '14'

        # Perform the API call through the SDK function
        result = self.controller.get_status_by_barcode(barcode, detail, language, max_days)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"CurrentStatus":{"Shipment":{"MainBarcode":"3SDEVC288882229","Bar'
            'code":"3SDEVC288882229","ShipmentAmount":"1","ShipmentCounter":"1"'
            ',"Customer":{"CustomerCode":"DEVC","CustomerNumber":"11223344","Na'
            'me":"Testaccount API PNP"},"ProductCode":"002285","ProductDescript'
            'ion":"Parcels, domestic &lt;= 10 kg","Reference":"2022133316350958'
            '07","DeliveryDate":"2022-11-08","Dimension":{"Height":"125","Lengt'
            'h":"250","Volume":"6250","Weight":"180","Width":"200"},"Address":['
            '{"AddressType":"01","Building":"{}","City":"Utrecht","CompanyName"'
            ':"{}","CountryCode":"NL","DepartmentName":"{}","District":"{}","Fi'
            'rstName":"Peter","Floor":"{}","HouseNumber":"74","HouseNumberSuffi'
            'x":"{}","LastName":"de Ruiter","Region":"{}","Remark":"{}","Street'
            '":"Molengraaffplantsoen","Zipcode":"3571ZZ"},{"AddressType":"02","'
            'Building":"{}","City":"Hoofddorp","CompanyName":"PostNL Pakketten"'
            ',"CountryCode":"NL","DepartmentName":"{}","District":"{}","FirstNa'
            'me":"{}","Floor":"{}","HouseNumber":"42","HouseNumberSuffix":"-60"'
            ',"LastName":"{}","Region":"{}","Remark":"{}","Street":"Siriusdreef'
            '","Zipcode":"2132WT"}],"ProductOptions":[{"OptionCode":"6","Charac'
            'teristicCode":"118"}],"Status":{"TimeStamp":"08-11-2022 10:13:20",'
            '"StatusCode":"7","StatusDescription":"Shipment out for delivery","'
            'PhaseCode":"3","PhaseDescription":"Distribution"}}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/reference?detail=true&language=NL&customerCode={{CustomerCode}}&customerNumber={{CustomerNumber}}&reference=REF98173245876329" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" 
    #```
    #
    def test_get_status_by_reference(self):
        # Parameters for the API call
        customer_code = 'DEVC'
        customer_number = '11223344'
        reference_id = 'REF-12345'
        detail = False
        language = 'NL'
        max_days = '14'

        # Perform the API call through the SDK function
        result = self.controller.get_status_by_reference(customer_code, customer_number, reference_id, detail, language, max_days)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"CurrentStatus":{"Shipment":{"MainBarcode":"3SDEVC288882229","Bar'
            'code":"3SDEVC288882229","ShipmentAmount":"1","ShipmentCounter":"1"'
            ',"Customer":{"CustomerCode":"DEVC","CustomerNumber":"11223344","Na'
            'me":"Testaccount API PNP"},"ProductCode":"002285","ProductDescript'
            'ion":"Parcels, domestic &lt;= 10 kg","Reference":"2022133316350958'
            '07","DeliveryDate":"2022-11-08","Dimension":{"Height":"125","Lengt'
            'h":"250","Volume":"6250","Weight":"180","Width":"200"},"Address":['
            '{"AddressType":"01","Building":"{}","City":"Utrecht","CompanyName"'
            ':"{}","CountryCode":"NL","DepartmentName":"{}","District":"{}","Fi'
            'rstName":"Peter","Floor":"{}","HouseNumber":"74","HouseNumberSuffi'
            'x":"{}","LastName":"de Ruiter","Region":"{}","Remark":"{}","Street'
            '":"Molengraaffplantsoen","Zipcode":"3571ZZ"},{"AddressType":"02","'
            'Building":"{}","City":"Hoofddorp","CompanyName":"PostNL Pakketten"'
            ',"CountryCode":"NL","DepartmentName":"{}","District":"{}","FirstNa'
            'me":"{}","Floor":"{}","HouseNumber":"42","HouseNumberSuffix":"-60"'
            ',"LastName":"{}","Region":"{}","Remark":"{}","Street":"Siriusdreef'
            '","Zipcode":"2132WT"}],"ProductOptions":[{"OptionCode":"6","Charac'
            'teristicCode":"118"}],"Status":{"TimeStamp":"08-11-2022 10:13:20",'
            '"StatusCode":"7","StatusDescription":"Shipment out for delivery","'
            'PhaseCode":"3","PhaseDescription":"Distribution"}}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/signature/3SDEVC172649258" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" 
    #```
    #
    def test_get_shipment_signature(self):
        # Parameters for the API call
        barcode = '3SDEVC172649258'

        # Perform the API call through the SDK function
        result = self.controller.get_shipment_signature(barcode)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"Signature":{"Barcode":"3SDEVC317858754","SignatureDate":"2022-11'
            '-07T19:28:16","SignatureImage":"iVBORw0KGgoAAAANSUhEUgAAAogAAAGTCA'
            'YAAACrs[TRUNCATED]"}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/11223344/updatedshipments?period=2022-12-25T10:00:00&amp;period=2022-12-25T10:12:00" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_get_updated_status_by_customer_number(self):
        # Parameters for the API call
        customernumber = '11223344'
        period = APIHelper.json_deserialize('["2022-11-07T12:00:00.000","2022-11-07T12:05:00.000"]')

        # Perform the API call through the SDK function
        result = self.controller.get_updated_status_by_customer_number(customernumber, period)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"Barcode":"3SDEVC2260332157","CreationDate":"2022-11-07T00:00:00'
            '","CustomerNumber":"11223344","CustomerCode":"DEVC","Status":{"Tim'
            'estamp":"2022-11-08T02:17:49","StatusCode":"5","StatusDescription"'
            ':"Zending gesorteerd","PhaseCode":"2","PhaseDescription":"Sorterin'
            'g"}},{"Barcode":"3SDEVC775533088","CreationDate":"2022-11-07T00:00'
            ':00","CustomerNumber":"11223344","CustomerCode":"DEVC","Status":{"'
            'Timestamp":"2022-11-08T04:15:00","StatusCode":"13","StatusDescript'
            'ion":"Voorgemeld: nog niet aangenomen","PhaseCode":"1","PhaseDescr'
            'iption":"Collectie"}},{"Barcode":"3SDEVC563372025","CreationDate":'
            '"2022-11-07T00:00:00","CustomerNumber":"11223344","CustomerCode":"'
            'DEVC","Status":{"Timestamp":"2022-11-08T04:15:00","StatusCode":"13'
            '","StatusDescription":"Voorgemeld: nog niet aangenomen","PhaseCode'
            '":"1","PhaseDescription":"Collectie"}},{"Barcode":"3SDEVC336510881'
            '","CreationDate":"2022-11-08T00:00:00","CustomerNumber":"11223344"'
            ',"CustomerCode":"DEVC","Status":{"Timestamp":"2022-11-08T01:01:28"'
            ',"StatusCode":"1","StatusDescription":"Zending voorgemeld","PhaseC'
            'ode":"1","PhaseDescription":"Collectie"}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

