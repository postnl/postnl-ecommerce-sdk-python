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
from postnlecommerce.models.checkout_response import CheckoutResponse
from postnlecommerce.exceptions.checkout_response_invalid_exception import CheckoutResponseInvalidException
from postnlecommerce.exceptions.barcode_method_not_allowed_exception import BarcodeMethodNotAllowedException
from postnlecommerce.exceptions.barcode_response_error_exception import BarcodeResponseErrorException


class CheckoutController(BaseController):

    """A Controller to access Endpoints in the postnlecommerce API."""
    def __init__(self, config):
        super(CheckoutController, self).__init__(config)

    def checkout(self,
                 body):
        """Does a POST request to /shipment/v1/checkout.

        TODO: type endpoint description here.

        Args:
            body (CheckoutRequest): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Status
                object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v1/checkout')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('APIKeyHeader'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CheckoutResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Invalid request', CheckoutResponseInvalidException)
            .local_error('401', 'Invalid apikey', BarcodeMethodNotAllowedException)
            .local_error('405', 'Method not allowed', BarcodeMethodNotAllowedException)
            .local_error('429', 'Too many requests', BarcodeMethodNotAllowedException)
            .local_error('500', 'Internal server error', BarcodeResponseErrorException)
        ).execute()
