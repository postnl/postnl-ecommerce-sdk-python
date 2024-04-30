# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from postnlecommerce.api_helper import APIHelper
import postnlecommerce.exceptions.api_exception
from postnlecommerce.models.error_1 import Error1


class LocationsResponseInvalidException(postnlecommerce.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the LocationsResponseInvalidException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(LocationsResponseInvalidException, self).__init__(reason, response)
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
        self.date = APIHelper.RFC3339DateTime.from_value(dictionary.get("Date")).datetime if dictionary.get("Date") else None
        self.error = Error1.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else None
        self.request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else None
