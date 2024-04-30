# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Label1(object):

    """Implementation of the 'Label1' model.

    TODO: type model description here.

    Attributes:
        content (str): Base64 encoded label content
        labeltype (str): Type of the label. See Guidelines
        output_type (str): Content type of the label, e.g. zebra of pdf. Note:
            It is not recommended to send .PDF files/labels directly to a
            Zebra printer. See Guidelines.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "content": 'Content',
        "labeltype": 'Labeltype',
        "output_type": 'OutputType'
    }

    _optionals = [
        'content',
        'labeltype',
        'output_type',
    ]

    def __init__(self,
                 content=APIHelper.SKIP,
                 labeltype=APIHelper.SKIP,
                 output_type=APIHelper.SKIP):
        """Constructor for the Label1 class"""

        # Initialize members of the class
        if content is not APIHelper.SKIP:
            self.content = content 
        if labeltype is not APIHelper.SKIP:
            self.labeltype = labeltype 
        if output_type is not APIHelper.SKIP:
            self.output_type = output_type 

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
        content = dictionary.get("Content") if dictionary.get("Content") else APIHelper.SKIP
        labeltype = dictionary.get("Labeltype") if dictionary.get("Labeltype") else APIHelper.SKIP
        output_type = dictionary.get("OutputType") if dictionary.get("OutputType") else APIHelper.SKIP
        # Return an object of this model
        return cls(content,
                   labeltype,
                   output_type)
