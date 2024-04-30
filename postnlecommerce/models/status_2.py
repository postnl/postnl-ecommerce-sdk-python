# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Status2(object):

    """Implementation of the 'Status2' model.

    The status update. See [Status
    codes](#tag/TandT-status-codes/Status-codes) for possible values.

    Attributes:
        timestamp (str): The timestamp of the update
        status_code (str): The status code
        status_description (str): The status description
        phase_code (str): The phase code
        phase_description (str): The phase description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timestamp": 'Timestamp',
        "status_code": 'StatusCode',
        "status_description": 'StatusDescription',
        "phase_code": 'PhaseCode',
        "phase_description": 'PhaseDescription'
    }

    _optionals = [
        'timestamp',
        'status_code',
        'status_description',
        'phase_code',
        'phase_description',
    ]

    def __init__(self,
                 timestamp=APIHelper.SKIP,
                 status_code=APIHelper.SKIP,
                 status_description=APIHelper.SKIP,
                 phase_code=APIHelper.SKIP,
                 phase_description=APIHelper.SKIP):
        """Constructor for the Status2 class"""

        # Initialize members of the class
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if status_code is not APIHelper.SKIP:
            self.status_code = status_code 
        if status_description is not APIHelper.SKIP:
            self.status_description = status_description 
        if phase_code is not APIHelper.SKIP:
            self.phase_code = phase_code 
        if phase_description is not APIHelper.SKIP:
            self.phase_description = phase_description 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        timestamp = dictionary.get("Timestamp") if dictionary.get("Timestamp") else APIHelper.SKIP
        status_code = dictionary.get("StatusCode") if dictionary.get("StatusCode") else APIHelper.SKIP
        status_description = dictionary.get("StatusDescription") if dictionary.get("StatusDescription") else APIHelper.SKIP
        phase_code = dictionary.get("PhaseCode") if dictionary.get("PhaseCode") else APIHelper.SKIP
        phase_description = dictionary.get("PhaseDescription") if dictionary.get("PhaseDescription") else APIHelper.SKIP
        # Return an object of this model
        return cls(timestamp,
                   status_code,
                   status_description,
                   phase_code,
                   phase_description)
