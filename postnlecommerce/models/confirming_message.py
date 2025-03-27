# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ConfirmingMessage(object):

    """Implementation of the 'confirmingMessage' model.

    Attributes:
        message_id (str): ID of the message
        message_time_stamp (str): Date/time of sending the message. Format:
            dd-mm-yyyy hh:mm:ss

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message_id": 'MessageID',
        "message_time_stamp": 'MessageTimeStamp'
    }

    def __init__(self,
                 message_id=None,
                 message_time_stamp=None):
        """Constructor for the ConfirmingMessage class"""

        # Initialize members of the class
        self.message_id = message_id 
        self.message_time_stamp = message_time_stamp 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        message_id = dictionary.get("MessageID") if dictionary.get("MessageID") else None
        message_time_stamp = dictionary.get("MessageTimeStamp") if dictionary.get("MessageTimeStamp") else None
        # Return an object of this model
        return cls(message_id,
                   message_time_stamp)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'message_id={self.message_id!r}, '
                f'message_time_stamp={self.message_time_stamp!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'message_id={self.message_id!s}, '
                f'message_time_stamp={self.message_time_stamp!s})')
