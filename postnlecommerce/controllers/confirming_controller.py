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
from postnlecommerce.models.confirming_response import ConfirmingResponse
from postnlecommerce.exceptions.confirming_response_error_exception import ConfirmingResponseErrorException
from postnlecommerce.exceptions.unauthorized_exception import UnauthorizedException
from postnlecommerce.exceptions.method_not_allowed_only_get_post_exception import MethodNotAllowedOnlyGetPostException
from postnlecommerce.exceptions.too_many_requests_exception import TooManyRequestsException
from postnlecommerce.exceptions.internal_server_error_exception import InternalServerErrorException


class ConfirmingController(BaseController):

    """A Controller to access Endpoints in the postnlecommerce API."""
    def __init__(self, config):
        super(ConfirmingController, self).__init__(config)

    def confirm_shipment(self,
                         body):
        """Does a POST request to /shipment/v2/confirm.

        TODO: type endpoint description here.

        Args:
            body (ConfirmingRequest): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                confirmation

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.POSTNL)
            .path('/shipment/v2/confirm')
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
            .deserialize_into(ConfirmingResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Error payload', ConfirmingResponseErrorException)
            .local_error('401', 'Invalid apikey', UnauthorizedException)
            .local_error('405', 'Method not allowed', MethodNotAllowedOnlyGetPostException)
            .local_error('429', 'Too many requests', TooManyRequestsException)
            .local_error('500', 'Internal server error', InternalServerErrorException)
        ).execute()
