# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class LabellingLabel(object):

    """Implementation of the 'labellingLabel' model.

    Attributes:
        content (str): Base64 encoded label content
        labeltype (str): Type of the label. See possible [Label
            types](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/label-types)
        output_type (str): Content type of the label, e.g. zebra of pdf.

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
        """Constructor for the LabellingLabel class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        content = dictionary.get("Content") if dictionary.get("Content") else APIHelper.SKIP
        labeltype = dictionary.get("Labeltype") if dictionary.get("Labeltype") else APIHelper.SKIP
        output_type = dictionary.get("OutputType") if dictionary.get("OutputType") else APIHelper.SKIP
        # Return an object of this model
        return cls(content,
                   labeltype,
                   output_type)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'content={(self.content if hasattr(self, "content") else None)!r}, '
                f'labeltype={(self.labeltype if hasattr(self, "labeltype") else None)!r}, '
                f'output_type={(self.output_type if hasattr(self, "output_type") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'content={(self.content if hasattr(self, "content") else None)!s}, '
                f'labeltype={(self.labeltype if hasattr(self, "labeltype") else None)!s}, '
                f'output_type={(self.output_type if hasattr(self, "output_type") else None)!s})')
