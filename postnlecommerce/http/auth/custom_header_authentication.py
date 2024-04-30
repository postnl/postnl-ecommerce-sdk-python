# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth


class CustomHeaderAuthentication(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in CustomHeaderAuthentication

        """
        return "CustomHeaderAuthentication: apikey is undefined."

    def __init__(self, custom_header_authentication_credentials):
        auth_params = {}
        if custom_header_authentication_credentials is not None \
                and custom_header_authentication_credentials.apikey is not None:
            auth_params["apikey"] = custom_header_authentication_credentials.apikey
        super().__init__(auth_params=auth_params)


class CustomHeaderAuthenticationCredentials:

    @property
    def apikey(self):
        return self._apikey

    def __init__(self, apikey):
        if apikey is None:
            raise ValueError('apikey cannot be None')
        self._apikey = apikey

    def clone_with(self, apikey=None):
        return CustomHeaderAuthenticationCredentials(apikey or self.apikey)
