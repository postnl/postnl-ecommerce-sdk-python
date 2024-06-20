# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.labelling_merged_label import LabellingMergedLabel
from postnlecommerce.models.labelling_response_shipment import LabellingResponseShipment


class LabellingResponse(object):

    """Implementation of the 'labellingResponse' model.

    TODO: type model description here.

    Attributes:
        merged_labels (List[LabellingMergedLabel]): The merged label output;
            only returned if the printer type selected in your request merges
            the pdf labels into a single file (e.g. using GraphicFile|Merge).
        response_shipments (List[LabellingResponseShipment]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "merged_labels": 'MergedLabels',
        "response_shipments": 'ResponseShipments'
    }

    _optionals = [
        'merged_labels',
        'response_shipments',
    ]

    def __init__(self,
                 merged_labels=APIHelper.SKIP,
                 response_shipments=APIHelper.SKIP):
        """Constructor for the LabellingResponse class"""

        # Initialize members of the class
        if merged_labels is not APIHelper.SKIP:
            self.merged_labels = merged_labels 
        if response_shipments is not APIHelper.SKIP:
            self.response_shipments = response_shipments 

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
        merged_labels = None
        if dictionary.get('MergedLabels') is not None:
            merged_labels = [LabellingMergedLabel.from_dictionary(x) for x in dictionary.get('MergedLabels')]
        else:
            merged_labels = APIHelper.SKIP
        response_shipments = None
        if dictionary.get('ResponseShipments') is not None:
            response_shipments = [LabellingResponseShipment.from_dictionary(x) for x in dictionary.get('ResponseShipments')]
        else:
            response_shipments = APIHelper.SKIP
        # Return an object of this model
        return cls(merged_labels,
                   response_shipments)
