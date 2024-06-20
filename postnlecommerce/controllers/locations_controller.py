# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
from postnlecommerce.configuration import Server
from postnlecommerce.http.api_response import ApiResponse
from postnlecommerce.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from postnlecommerce.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from postnlecommerce.models.locations_response_multiple import LocationsResponseMultiple
from postnlecommerce.models.location_response_single import LocationResponseSingle
from postnlecommerce.exceptions.invalid_request_exception import InvalidRequestException
from postnlecommerce.exceptions.unauthorized_exception import UnauthorizedException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.too_many_requests_exception import TooManyRequestsException
from postnlecommerce.exceptions.internal_server_error_exception import InternalServerErrorException


class LocationsController(BaseController):

    """A Controller to access Endpoints in the postnlecommerce API."""
    def __init__(self, config):
        super(LocationsController, self).__init__(config)

    def get_pickup_locations_by_address(self,
                                        country_code,
                                        postal_code,
                                        city=None,
                                        street=None,
                                        house_number=None,
                                        house_number_extension=None,
                                        delivery_date=None,
                                        opening_time=None,
                                        delivery_options=None):
        """Does a GET request to /shipment/v2_1/locations/nearest.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest?CountryC
        ode=NL&PostalCode=2132WT&City=Hoofddorp&Street=Siriusdreef&HouseNumber=
        42&HouseNumberExtension=-60&DeliveryDate=24-12-2022&OpeningTime=09%3A00
        %3A00" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            country_code (CountrycodeEnum): The country of the recipient's
                address
            postal_code (str): The zipcode of the recipient's address
            city (str, optional): The city of the recipient's address
            street (str, optional): The street name of the recipient's
                address
            house_number (int, optional): The house number of the recipient's
                address
            house_number_extension (str, optional): The house number extension
                of the recipient's address
            delivery_date (str, optional): The date of the earliest delivery
                date at the pickup location. Format:  dd-MM-yyyy. Note: this
                date cannot be in the past, otherwise an error is returned. If
                not provided, the present day is used as a default
            opening_time (str, optional): Opening time filter. Format:
                hh:mm:ss. This field will be used to filter out locations that
                are closed at the time provided. If no opening time is
                provided all locations will be returned regardless of their
                opening times.
            delivery_options (List[LocationsDeliveryOptionEnum], optional):
                The pickup location types for which locations should be
                filtered. By default all location types are returned (PG =
                Retail points and parcel lockers). This can be used to filter
                on only parcel lockers (PA) or specifically exclude parcel
                lockers from the response (PG_EX).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Locations
                nearest to the address provided

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_1/locations/nearest')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('PostalCode')
                         .value(postal_code))
            .query_param(Parameter()
                         .key('City')
                         .value(city))
            .query_param(Parameter()
                         .key('Street')
                         .value(street))
            .query_param(Parameter()
                         .key('HouseNumber')
                         .value(house_number))
            .query_param(Parameter()
                         .key('HouseNumberExtension')
                         .value(house_number_extension))
            .query_param(Parameter()
                         .key('DeliveryDate')
                         .value(delivery_date))
            .query_param(Parameter()
                         .key('OpeningTime')
                         .value(opening_time))
            .query_param(Parameter()
                         .key('DeliveryOptions')
                         .value(delivery_options))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LocationsResponseMultiple.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()

    def get_pickup_locations_by_coordinates(self,
                                            latitude,
                                            longitude,
                                            country_code,
                                            delivery_date=None,
                                            opening_time=None,
                                            delivery_options=None):
        """Does a GET request to /shipment/v2_1/locations/nearest/geocode.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest/geocode?
        Latitude=52.2864669620795&Longitude=4.68239055845954&CountryCode=NL&Del
        iveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            latitude (float): The latitude of the location
            longitude (float): The longitude of the location
            country_code (CountrycodeEnum): The coutry for which the
                coordinates are provided
            delivery_date (str, optional): The date of the earliest delivery
                date. Format:  dd-MM-yyyy. Note: this date cannot be in the
                past, otherwise an error is returned.
            opening_time (str, optional): Opening time filter. Format:
                hh:mm:ss. This field will be used to filter out locations that
                are closed at the time provided.
            delivery_options (List[LocationsDeliveryOptionEnum], optional):
                The pickup location types for which locations should be
                filtered. By default all location types are returned (PG =
                Retail points and parcel lockers). This can be used to filter
                on only parcel lockers (PA) or specifically exclude parcel
                lockers from the response (PG_EX).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Locations
                nearest to the coordinates provided

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_1/locations/nearest/geocode')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('Latitude')
                         .value(latitude))
            .query_param(Parameter()
                         .key('Longitude')
                         .value(longitude))
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('DeliveryDate')
                         .value(delivery_date))
            .query_param(Parameter()
                         .key('OpeningTime')
                         .value(opening_time))
            .query_param(Parameter()
                         .key('DeliveryOptions')
                         .value(delivery_options))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LocationsResponseMultiple.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()

    def get_pickup_locations_within_area(self,
                                         latitude_north,
                                         longitude_west,
                                         latitude_south,
                                         longitude_east,
                                         country_code,
                                         delivery_date=None,
                                         opening_time=None,
                                         delivery_options=None):
        """Does a GET request to /shipment/v2_1/locations/area.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_1/locations/area?LatitudeNor
        th=52.156439&LongitudeWest=5.015643&LatitudeSouth=52.017473&LongitudeEa
        st=5.065254&CountryCode=NL&DeliveryDate=24-12-2023&OpeningTime=09%3A00%
        3A00" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            latitude_north (float): The northmost coordinates of the area
            longitude_west (float): The westmost coordinates of the area
            latitude_south (float): The southmost coordinates of the area
            longitude_east (float): The eastmost coordinates of the area
            country_code (CountrycodeEnum): TODO: type description here.
            delivery_date (str, optional): The date of the earliest delivery
                date. Format:  dd-MM-yyyy. Note: this date cannot be in the
                past, otherwise an error is returned.
            opening_time (str, optional): Opening time filter. Format:
                hh:mm:ss. This field will be used to filter out locations that
                are closed at the time provided.
            delivery_options (List[LocationsDeliveryOptionEnum], optional):
                The pickup location types for which locations should be
                filtered. By default all location types are returned (PG =
                Retail points and parcel lockers). This can be used to filter
                on only parcel lockers (PA) or specifically exclude parcel
                lockers from the response (PG_EX).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Locations
                nearest to the area provided

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_1/locations/area')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('LatitudeNorth')
                         .value(latitude_north))
            .query_param(Parameter()
                         .key('LongitudeWest')
                         .value(longitude_west))
            .query_param(Parameter()
                         .key('LatitudeSouth')
                         .value(latitude_south))
            .query_param(Parameter()
                         .key('LongitudeEast')
                         .value(longitude_east))
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('DeliveryDate')
                         .value(delivery_date))
            .query_param(Parameter()
                         .key('OpeningTime')
                         .value(opening_time))
            .query_param(Parameter()
                         .key('DeliveryOptions')
                         .value(delivery_options))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LocationsResponseMultiple.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()

    def get_pickup_location(self,
                            location_code):
        """Does a GET request to /shipment/v2_1/locations/lookup.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_1/locations/lookup?LocationC
        ode=216877" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" 
        ```

        Args:
            location_code (str): LocationCode information

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Location
                information

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_1/locations/lookup')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('LocationCode')
                         .value(location_code))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LocationResponseSingle.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()
