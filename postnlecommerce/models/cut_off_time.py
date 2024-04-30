# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class CutOffTime(object):

    """Implementation of the 'CutOffTime' model.

    TODO: type model description here.

    Attributes:
        day (DayEnum): The day for which the cutoff time applies. 00 is your
            default cutoff that applies to all otherwise not specified days,
            01 to 07 is Monday to Sunday.
        available (bool): Specifies whether you are available to process
            shipments during the selected day
        mtype (Type1Enum): Specifies the type belonging to the cutoff time.
        time (str): Specifies the cutoff time (mandatory when Available is
            true)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day": 'Day',
        "available": 'Available',
        "mtype": 'Type',
        "time": 'Time'
    }

    _optionals = [
        'available',
        'mtype',
        'time',
    ]

    def __init__(self,
                 day=None,
                 available=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 time=APIHelper.SKIP):
        """Constructor for the CutOffTime class"""

        # Initialize members of the class
        self.day = day 
        if available is not APIHelper.SKIP:
            self.available = available 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if time is not APIHelper.SKIP:
            self.time = time 

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
        day = dictionary.get("Day") if dictionary.get("Day") else None
        available = dictionary.get("Available") if "Available" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        time = dictionary.get("Time") if dictionary.get("Time") else APIHelper.SKIP
        # Return an object of this model
        return cls(day,
                   available,
                   mtype,
                   time)
