# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class ShippingstatusDimension(object):

    """Implementation of the 'shippingstatusDimension' model.

    Attributes:
        weight (str): The weight of the shipment
        height (str): The height of the shipment
        length (str): The length of the shipment
        width (str): The width of the shipment
        volume (str): The volume of the shipment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "weight": 'Weight',
        "height": 'Height',
        "length": 'Length',
        "width": 'Width',
        "volume": 'Volume'
    }

    _optionals = [
        'weight',
        'height',
        'length',
        'width',
        'volume',
    ]

    def __init__(self,
                 weight=APIHelper.SKIP,
                 height=APIHelper.SKIP,
                 length=APIHelper.SKIP,
                 width=APIHelper.SKIP,
                 volume=APIHelper.SKIP):
        """Constructor for the ShippingstatusDimension class"""

        # Initialize members of the class
        if weight is not APIHelper.SKIP:
            self.weight = weight 
        if height is not APIHelper.SKIP:
            self.height = height 
        if length is not APIHelper.SKIP:
            self.length = length 
        if width is not APIHelper.SKIP:
            self.width = width 
        if volume is not APIHelper.SKIP:
            self.volume = volume 

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
        weight = dictionary.get("Weight") if dictionary.get("Weight") else APIHelper.SKIP
        height = dictionary.get("Height") if dictionary.get("Height") else APIHelper.SKIP
        length = dictionary.get("Length") if dictionary.get("Length") else APIHelper.SKIP
        width = dictionary.get("Width") if dictionary.get("Width") else APIHelper.SKIP
        volume = dictionary.get("Volume") if dictionary.get("Volume") else APIHelper.SKIP
        # Return an object of this model
        return cls(weight,
                   height,
                   length,
                   width,
                   volume)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'weight={(self.weight if hasattr(self, "weight") else None)!r}, '
                f'height={(self.height if hasattr(self, "height") else None)!r}, '
                f'length={(self.length if hasattr(self, "length") else None)!r}, '
                f'width={(self.width if hasattr(self, "width") else None)!r}, '
                f'volume={(self.volume if hasattr(self, "volume") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'weight={(self.weight if hasattr(self, "weight") else None)!s}, '
                f'height={(self.height if hasattr(self, "height") else None)!s}, '
                f'length={(self.length if hasattr(self, "length") else None)!s}, '
                f'width={(self.width if hasattr(self, "width") else None)!s}, '
                f'volume={(self.volume if hasattr(self, "volume") else None)!s})')
