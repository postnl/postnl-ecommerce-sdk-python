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
from postnlecommerce.models.deliverydate_delivery_response import DeliverydateDeliveryResponse
from postnlecommerce.models.deliverydate_shipping_response import DeliverydateShippingResponse
from postnlecommerce.exceptions.invalid_request_exception import InvalidRequestException
from postnlecommerce.exceptions.unauthorized_exception import UnauthorizedException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.too_many_requests_exception import TooManyRequestsException
from postnlecommerce.exceptions.internal_server_error_exception import InternalServerErrorException


class DeliverydateController(BaseController):

    """A Controller to access Endpoints in the postnlecommerce API."""
    def __init__(self, config):
        super(DeliverydateController, self).__init__(config)

    def calculate_delivery_date(self,
                                shipping_date,
                                shipping_duration,
                                cut_off_time,
                                postal_code,
                                country_code,
                                options,
                                origin_country_code='NL',
                                city=None,
                                street=None,
                                house_number=None,
                                house_nr_ext=None,
                                cut_off_time_monday=None,
                                available_monday=None,
                                cut_off_time_tuesday=None,
                                available_tuesday=None,
                                cut_off_time_wednesday=None,
                                available_wednesday=None,
                                cut_off_time_thursday=None,
                                available_thursday=None,
                                cut_off_time_friday=None,
                                available_friday=None,
                                cut_off_time_saturday=None,
                                available_saturday=None,
                                cut_off_time_sunday=None,
                                available_sunday=None):
        """Does a GET request to /shipment/v2_2/calculate/date/delivery.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/delivery?Sh
        ippingDate=29-05-2022+14%3A00%3A00&amp;ShippingDuration=1&amp;CutOffTim
        e=17%3A00%3A00&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofdd
        orp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" 
        ```

        Args:
            shipping_date (str): Date/time of preparing the shipment for
                sending. Format: dd-MM-yyyy hh:mm:ss
            shipping_duration (int): The duration it takes for the shipment to
                be delivered to PostNL in days. A value of 1 means that the
                parcel will be delivered to PostNL on the same day as the date
                specified in ShippingDate. A value of 2 means the parcel will
                arrive at PostNL a day later etc.
            cut_off_time (str): Default cutoff time
            postal_code (str): Zipcode of the destination address
            country_code (CountrycodeEnum): The ISO2 destination country code
            options (List[DeliverydateOptionEnum]): The delivery options that
                you want to take into account when calculating the expected
                delivery date
            origin_country_code (OriginCountryCodeEnum, optional): The ISO2
                origin country code
            city (str, optional): City of the destination address
            street (str, optional): The street name of the destination
                address.
            house_number (int, optional): The house number of the destination
                address
            house_nr_ext (str, optional): House number extension of the
                delivery address
            cut_off_time_monday (str, optional): Overrides default cutoff time
                specified in the CutOffTime parameter for mondays
                specifically
            available_monday (bool, optional): Specifies if you are available
                to ship to PostNL on mondays
            cut_off_time_tuesday (str, optional): Overrides default cutoff
                time specified in the CutOffTime parameter for tuesdays
                specifically
            available_tuesday (bool, optional): Specifies if you are available
                to ship to PostNL on tuesdays
            cut_off_time_wednesday (str, optional): Overrides default cutoff
                time specified in the CutOffTime parameter for wednesdays
                specifically
            available_wednesday (bool, optional): Specifies if you are
                available to ship to PostNL on wednesdays
            cut_off_time_thursday (str, optional): Overrides default cutoff
                time specified in the CutOffTime parameter for thursdays
                specifically
            available_thursday (bool, optional): Specifies if you are
                available to ship to PostNL on thursdays
            cut_off_time_friday (str, optional): Overrides default cutoff time
                specified in the CutOffTime parameter for fridays
                specifically
            available_friday (bool, optional): Specifies if you are available
                to ship to PostNL on fridays
            cut_off_time_saturday (str, optional): Overrides default cutoff
                time specified in the CutOffTime parameter for saturdays
                specifically
            available_saturday (bool, optional): Specifies if you are
                available to ship to PostNL on saturdays
            cut_off_time_sunday (str, optional): Overrides default cutoff time
                specified in the CutOffTime parameter for sundays
                specifically
            available_sunday (bool, optional): Specifies if you are available
                to ship to PostNL on sundays

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Expected
                earliest delivery date

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_2/calculate/date/delivery')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('ShippingDate')
                         .value(shipping_date))
            .query_param(Parameter()
                         .key('ShippingDuration')
                         .value(shipping_duration))
            .query_param(Parameter()
                         .key('CutOffTime')
                         .value(cut_off_time))
            .query_param(Parameter()
                         .key('PostalCode')
                         .value(postal_code))
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('Options')
                         .value(options))
            .query_param(Parameter()
                         .key('OriginCountryCode')
                         .value(origin_country_code))
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
                         .key('HouseNrExt')
                         .value(house_nr_ext))
            .query_param(Parameter()
                         .key('CutOffTimeMonday')
                         .value(cut_off_time_monday))
            .query_param(Parameter()
                         .key('AvailableMonday')
                         .value(available_monday))
            .query_param(Parameter()
                         .key('CutOffTimeTuesday')
                         .value(cut_off_time_tuesday))
            .query_param(Parameter()
                         .key('AvailableTuesday')
                         .value(available_tuesday))
            .query_param(Parameter()
                         .key('CutOffTimeWednesday')
                         .value(cut_off_time_wednesday))
            .query_param(Parameter()
                         .key('AvailableWednesday')
                         .value(available_wednesday))
            .query_param(Parameter()
                         .key('CutOffTimeThursday')
                         .value(cut_off_time_thursday))
            .query_param(Parameter()
                         .key('AvailableThursday')
                         .value(available_thursday))
            .query_param(Parameter()
                         .key('CutOffTimeFriday')
                         .value(cut_off_time_friday))
            .query_param(Parameter()
                         .key('AvailableFriday')
                         .value(available_friday))
            .query_param(Parameter()
                         .key('CutOffTimeSaturday')
                         .value(cut_off_time_saturday))
            .query_param(Parameter()
                         .key('AvailableSaturday')
                         .value(available_saturday))
            .query_param(Parameter()
                         .key('CutOffTimeSunday')
                         .value(cut_off_time_sunday))
            .query_param(Parameter()
                         .key('AvailableSunday')
                         .value(available_sunday))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeliverydateDeliveryResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()

    def calculate_shipping_date(self,
                                delivery_date,
                                shipping_duration,
                                postal_code,
                                country_code,
                                origin_country_code='NL',
                                city=None,
                                street=None,
                                house_number=None,
                                house_nr_ext=None):
        """Does a GET request to /shipment/v2_2/calculate/date/shipping.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/shipping?De
        liveryDate=30-05-2022&amp;ShippingDuration=1&amp;PostalCode=2132WT&amp;
        CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumbe
        r=42&amp;HouseNrExt=A" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" \
        ```

        Args:
            delivery_date (str): Date of the expected delivery (to the final
                destination) of the shipment.
            shipping_duration (int): The duration it takes for the shipment to
                be delivered to PostNL in days. A value of 1 means that the
                parcel will be delivered to PostNL on the same day as the date
                specified in ShippingDate. A value of 2 means the parcel will
                arrive at PostNL a day later etc.
            postal_code (str): Zipcode of the address
            country_code (CountrycodeEnum): The ISO2 destination country code
            origin_country_code (OriginCountryCodeEnum, optional): The ISO2
                country code of the origin country
            city (str, optional): City of the destination address
            street (str, optional): The street name of the destination
                address
            house_number (int, optional): The house number of the destination
                address
            house_nr_ext (str, optional): House number extension of the
                destination address

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. The
                calculated date that the parcel needs to be shipped to PostNL

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2_2/calculate/date/shipping')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('DeliveryDate')
                         .value(delivery_date))
            .query_param(Parameter()
                         .key('ShippingDuration')
                         .value(shipping_duration))
            .query_param(Parameter()
                         .key('PostalCode')
                         .value(postal_code))
            .query_param(Parameter()
                         .key('CountryCode')
                         .value(country_code))
            .query_param(Parameter()
                         .key('OriginCountryCode')
                         .value(origin_country_code))
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
                         .key('HouseNrExt')
                         .value(house_nr_ext))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeliverydateShippingResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', InvalidRequestException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()
