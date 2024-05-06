# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Dimension(object):

    """Implementation of the 'Dimension' model.

    Note: Length, Width, Height values are about the order of the size and
    need to be filled in from the longest to the shortest value. For example:
    shipment's official height is 700mm, width 500mm, length 300mm. The
    longest side (highest value) of 700mm needs to be entered at Length. Width
    value becomes 500mm, Height value: 300mm (the lowest). Entering the
    dimensions in the wrong order may result in incorrect shipping labels and
    longer delivery times. The maximum dimensions can be found in your PostNL
    contract.

    Attributes:
        height (int): The shortest side of the shipment in millimeters (mm).
        length (int): The longest side of the shipment in millimeters (mm).
        volume (int): Volume of the shipment in centimeters (cm3). Mandatory
            for E@H-products.
        weight (int): Weight of the shipment in grams. Approximate weight
            suffices
        width (int): The second longest side of the shipment in millimeters
            (mm).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "weight": 'Weight',
        "height": 'Height',
        "length": 'Length',
        "volume": 'Volume',
        "width": 'Width'
    }

    _optionals = [
        'height',
        'length',
        'volume',
        'width',
    ]

    def __init__(self,
                 weight=None,
                 height=APIHelper.SKIP,
                 length=APIHelper.SKIP,
                 volume=APIHelper.SKIP,
                 width=APIHelper.SKIP):
        """Constructor for the Dimension class"""

        # Initialize members of the class
        if height is not APIHelper.SKIP:
            self.height = height 
        if length is not APIHelper.SKIP:
            self.length = length 
        if volume is not APIHelper.SKIP:
            self.volume = volume 
        self.weight = weight 
        if width is not APIHelper.SKIP:
            self.width = width 

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
        weight = dictionary.get("Weight") if dictionary.get("Weight") else None
        height = dictionary.get("Height") if dictionary.get("Height") else APIHelper.SKIP
        length = dictionary.get("Length") if dictionary.get("Length") else APIHelper.SKIP
        volume = dictionary.get("Volume") if dictionary.get("Volume") else APIHelper.SKIP
        width = dictionary.get("Width") if dictionary.get("Width") else APIHelper.SKIP
        # Return an object of this model
        return cls(weight,
                   height,
                   length,
                   volume,
                   width)
