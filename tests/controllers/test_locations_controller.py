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


class LocationsControllerTests(ControllerTestBase):

    controller = None

    @classmethod
    def setUpClass(cls):
        super(LocationsControllerTests, cls).setUpClass()
        cls.controller = cls.client.locations
        cls.response_catcher = cls.controller.http_call_back

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest?CountryCode=NL&PostalCode=2132WT&City=Hoofddorp&Street=Siriusdreef&HouseNumber=42&HouseNumberExtension=-60&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_get_pickup_locations_by_address(self):
        # Parameters for the API call
        country_code = 'NL'
        postal_code = '2132WT'
        city = 'Hoofddorp'
        street = 'Siriusdreef'
        house_number = 42
        house_number_extension = '-60'
        delivery_date = '24-12-2022'
        opening_time = '09:00:00'
        delivery_options = None

        # Perform the API call through the SDK function
        result = self.controller.get_pickup_locations_by_address(country_code, postal_code, city, street, house_number, house_number_extension, delivery_date, opening_time, delivery_options)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"GetLocationsResult":{"ResponseLocation":[{"Address":{"City":"Cit'
            'y6","Countrycode":"Countrycode2","HouseNr":136,"HouseNrExt":"House'
            'NrExt4","Remark":"Remark8"},"DeliveryOptions":{"string":["string6"'
            ',"string7"]},"Distance":244,"Latitude":103.5,"LocationCode":102}]}'
            '}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest/geocode?Latitude=52.2864669620795&Longitude=4.68239055845954&CountryCode=NL&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_get_pickup_locations_by_coordinates(self):
        # Parameters for the API call
        latitude = 52.2864669620795
        longitude = 4.68239055845954
        country_code = 'NL'
        delivery_date = '24-12-2022'
        opening_time = '09:00:00'
        delivery_options = None

        # Perform the API call through the SDK function
        result = self.controller.get_pickup_locations_by_coordinates(latitude, longitude, country_code, delivery_date, opening_time, delivery_options)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"GetLocationsResult":{"ResponseLocation":[{"Address":{"City":"Cit'
            'y6","Countrycode":"Countrycode2","HouseNr":136,"HouseNrExt":"House'
            'NrExt4","Remark":"Remark8"},"DeliveryOptions":{"string":["string6"'
            ',"string7"]},"Distance":244,"Latitude":103.5,"LocationCode":102}]}'
            '}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/area?LatitudeNorth=52.156439&LongitudeWest=5.015643&LatitudeSouth=52.017473&LongitudeEast=5.065254&CountryCode=NL&DeliveryDate=24-12-2023&OpeningTime=09%3A00%3A00" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" \
    #```
    #
    def test_get_pickup_locations_within_area(self):
        # Parameters for the API call
        latitude_north = 52.156439
        longitude_west = 5.015643
        latitude_south = 52.017473
        longitude_east = 5.065254
        country_code = 'NL'
        delivery_date = '24-12-2023'
        opening_time = '09:00:00'
        delivery_options = None

        # Perform the API call through the SDK function
        result = self.controller.get_pickup_locations_within_area(latitude_north, longitude_west, latitude_south, longitude_east, country_code, delivery_date, opening_time, delivery_options)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"GetLocationsResult":{"ResponseLocation":[{"Address":{"City":"Cit'
            'y6","Countrycode":"Countrycode2","HouseNr":136,"HouseNrExt":"House'
            'NrExt4","Remark":"Remark8"},"DeliveryOptions":{"string":["string6"'
            ',"string7"]},"Distance":244,"Latitude":103.5,"LocationCode":102}]}'
            '}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Request example:
    #```
    #curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/lookup?LocationCode=216877" \
    # -H "Accept: application/json" \
    # -H "apikey: APIKEY-HERE" 
    #```
    #
    def test_get_pickup_location(self):
        # Parameters for the API call
        location_code = '216877'

        # Perform the API call through the SDK function
        result = self.controller.get_pickup_location(location_code)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"GetLocationsResult":{"ResponseLocation":{"Address":{"City":"City'
            '6","Countrycode":"Countrycode2","HouseNr":136,"HouseNrExt":"HouseN'
            'rExt4","Remark":"Remark8"},"DeliveryOptions":{"string":["string6",'
            '"string7"]},"Distance":244,"Latitude":103.5,"LocationCode":102}}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

