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
from postnlecommerce.models.barcode_response import BarcodeResponse
from postnlecommerce.exceptions.barcode_response_invalid_exception import BarcodeResponseInvalidException
from postnlecommerce.exceptions.unauthorized_exception import UnauthorizedException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.too_many_requests_exception import TooManyRequestsException
from postnlecommerce.exceptions.internal_server_error_exception import InternalServerErrorException


class BarcodeController(BaseController):

    """A Controller to access Endpoints in the postnlecommerce API."""
    def __init__(self, config):
        super(BarcodeController, self).__init__(config)

    def generate_barcode(self,
                         customer_code,
                         customer_number,
                         mtype,
                         serie=None,
                         range=None):
        """Does a GET request to /shipment/v1_1/barcode.

        Request example:
        ```
        curl -X GET
        "https://api-sandbox.postnl.nl/shipment/v1_1/barcode?CustomerCode=DEVC&
        amp;CustomerNumber=11223344&amp;Type=3S&amp;Serie=000000000-999999999&a
        mp" \
         -H "Accept: application/json" \
         -H "apikey: APIKEY-HERE" 
        ```

        Args:
            customer_code (str): The customer code for which you want a
                barcode to be generated
            customer_number (str): The customer code for which you want a
                barcode to be generated
            mtype (TypeEnum): The barcode type that you want to be generated
            serie (str, optional): Barcode serie in the format
                '###000000-###000000', for example 100000-20000. The range
                must consist of a minimal difference of 100.000. It is allowed
                to add extra leading zeros at the beginning of the serie. See
                [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoi
                nts/send-track/barcode/guidelines) for more information.
            range (str, optional): Only used for International Mail and Packet
                products (PEPS) shipments (with type LA, RI, UE). Identifying
                the issuing postal administration's country (NL in this
                case).

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                barcode

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v1_1/barcode')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('CustomerCode')
                         .value(customer_code))
            .query_param(Parameter()
                         .key('CustomerNumber')
                         .value(customer_number))
            .query_param(Parameter()
                         .key('Type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('Serie')
                         .value(serie))
            .query_param(Parameter()
                         .key('Range')
                         .value(range))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BarcodeResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', BarcodeResponseInvalidException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()
