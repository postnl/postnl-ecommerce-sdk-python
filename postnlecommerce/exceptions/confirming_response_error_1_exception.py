# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
import postnlecommerce.exceptions.api_exception
from postnlecommerce.models.response_shipment import ResponseShipment


class ConfirmingResponseError1Exception(postnlecommerce.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ConfirmingResponseError1Exception class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ConfirmingResponseError1Exception, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.response_shipments = None
        if dictionary.get('ResponseShipments') is not None:
            self.response_shipments = [ResponseShipment.from_dictionary(x) for x in dictionary.get('ResponseShipments')]
        else:
            self.response_shipments = None
