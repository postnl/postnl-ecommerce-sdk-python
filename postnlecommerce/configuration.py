# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import warnings
from enum import Enum
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    # Production server
    PRODUCTION_SERVER = 0
    # Sandbox environment for testing
    NON_PRODUCTION_SERVER = 1


class Server(Enum):
    """An enum for API servers"""
    POSTNL = 0


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def apikey(self):
        return self._custom_header_authentication_credentials.apikey

    @property
    def custom_header_authentication_credentials(self):
        return self._custom_header_authentication_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=3, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION_SERVER, apikey=None,
                 custom_header_authentication_credentials=None):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance,
                         override_http_client_configuration, http_call_back,
                         timeout, max_retries, backoff_factor, retry_statuses,
                         retry_methods)

        # Current API environment
        self._environment = environment

        self._custom_header_authentication_credentials = self.create_auth_credentials_object(
            apikey, custom_header_authentication_credentials)

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   apikey=None, custom_header_authentication_credentials=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        custom_header_authentication_credentials = self.create_auth_credentials_object(
            apikey,
            custom_header_authentication_credentials or self.custom_header_authentication_credentials,
            stack_level=3)
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout, max_retries=max_retries,
            backoff_factor=backoff_factor, retry_statuses=retry_statuses,
            retry_methods=retry_methods, environment=environment,
            custom_header_authentication_credentials=custom_header_authentication_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION_SERVER: {
            Server.POSTNL: 'https://api.postnl.nl'
        },
        Environment.NON_PRODUCTION_SERVER: {
            Server.POSTNL: 'https://api-sandbox.postnl.nl'
        }
    }

    def get_base_uri(self, server=Server.POSTNL):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]

    @staticmethod
    def create_auth_credentials_object(apikey,
                                       custom_header_authentication_credentials,
                                       stack_level=4):
        if apikey is None:
            return custom_header_authentication_credentials

        warnings.warn(message=('The \'apikey\' params are deprecated. Use \'cus'
                               'tom_header_authentication_credentials\' param i'
                               'nstead.'),
                      category=DeprecationWarning,
                      stacklevel=stack_level)

        if custom_header_authentication_credentials is not None:
            return custom_header_authentication_credentials.clone_with(apikey)

        from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthenticationCredentials
        return CustomHeaderAuthenticationCredentials(apikey)
