# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class HazardousMaterial(object):

    """Implementation of the 'HazardousMaterial' model.

    TODO: type model description here.

    Attributes:
        toxic_substance_code (str): Toxic substance code as stated in the ADR
            agreement
        additional_toxic_substance_code (List[str]): Array of additional toxic
            substance codes as stated in the ADR agreement
        adr_points (str): The amount of ADR points
        tunnel_code (str): The code indicating for which category of tunnels
            passage is prohibited with these goods.
        packaging_group_code (str): Code identifying the category of the
            packaging material.
        packaging_group_description (str): Description of the packaging
            material
        gross_weight (str): Gross weight of the goods in grams.
        undg_number (str): The UNDG number
        transport_category_code (str): The transport category code
        chemical_technical_description (str): The chemical technical
            description of the goods.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "toxic_substance_code": 'ToxicSubstanceCode',
        "additional_toxic_substance_code": 'AdditionalToxicSubstanceCode',
        "adr_points": 'ADRPoints',
        "tunnel_code": 'TunnelCode',
        "packaging_group_code": 'PackagingGroupCode',
        "packaging_group_description": 'PackagingGroupDescription',
        "gross_weight": 'GrossWeight',
        "undg_number": 'UNDGNumber',
        "transport_category_code": 'TransportCategoryCode',
        "chemical_technical_description": 'ChemicalTechnicalDescription'
    }

    _optionals = [
        'additional_toxic_substance_code',
        'adr_points',
        'tunnel_code',
        'packaging_group_code',
        'packaging_group_description',
        'gross_weight',
        'undg_number',
        'transport_category_code',
        'chemical_technical_description',
    ]

    def __init__(self,
                 toxic_substance_code=None,
                 additional_toxic_substance_code=APIHelper.SKIP,
                 adr_points=APIHelper.SKIP,
                 tunnel_code=APIHelper.SKIP,
                 packaging_group_code=APIHelper.SKIP,
                 packaging_group_description=APIHelper.SKIP,
                 gross_weight=APIHelper.SKIP,
                 undg_number=APIHelper.SKIP,
                 transport_category_code=APIHelper.SKIP,
                 chemical_technical_description=APIHelper.SKIP):
        """Constructor for the HazardousMaterial class"""

        # Initialize members of the class
        self.toxic_substance_code = toxic_substance_code 
        if additional_toxic_substance_code is not APIHelper.SKIP:
            self.additional_toxic_substance_code = additional_toxic_substance_code 
        if adr_points is not APIHelper.SKIP:
            self.adr_points = adr_points 
        if tunnel_code is not APIHelper.SKIP:
            self.tunnel_code = tunnel_code 
        if packaging_group_code is not APIHelper.SKIP:
            self.packaging_group_code = packaging_group_code 
        if packaging_group_description is not APIHelper.SKIP:
            self.packaging_group_description = packaging_group_description 
        if gross_weight is not APIHelper.SKIP:
            self.gross_weight = gross_weight 
        if undg_number is not APIHelper.SKIP:
            self.undg_number = undg_number 
        if transport_category_code is not APIHelper.SKIP:
            self.transport_category_code = transport_category_code 
        if chemical_technical_description is not APIHelper.SKIP:
            self.chemical_technical_description = chemical_technical_description 

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
        toxic_substance_code = dictionary.get("ToxicSubstanceCode") if dictionary.get("ToxicSubstanceCode") else None
        additional_toxic_substance_code = dictionary.get("AdditionalToxicSubstanceCode") if dictionary.get("AdditionalToxicSubstanceCode") else APIHelper.SKIP
        adr_points = dictionary.get("ADRPoints") if dictionary.get("ADRPoints") else APIHelper.SKIP
        tunnel_code = dictionary.get("TunnelCode") if dictionary.get("TunnelCode") else APIHelper.SKIP
        packaging_group_code = dictionary.get("PackagingGroupCode") if dictionary.get("PackagingGroupCode") else APIHelper.SKIP
        packaging_group_description = dictionary.get("PackagingGroupDescription") if dictionary.get("PackagingGroupDescription") else APIHelper.SKIP
        gross_weight = dictionary.get("GrossWeight") if dictionary.get("GrossWeight") else APIHelper.SKIP
        undg_number = dictionary.get("UNDGNumber") if dictionary.get("UNDGNumber") else APIHelper.SKIP
        transport_category_code = dictionary.get("TransportCategoryCode") if dictionary.get("TransportCategoryCode") else APIHelper.SKIP
        chemical_technical_description = dictionary.get("ChemicalTechnicalDescription") if dictionary.get("ChemicalTechnicalDescription") else APIHelper.SKIP
        # Return an object of this model
        return cls(toxic_substance_code,
                   additional_toxic_substance_code,
                   adr_points,
                   tunnel_code,
                   packaging_group_code,
                   packaging_group_description,
                   gross_weight,
                   undg_number,
                   transport_category_code,
                   chemical_technical_description)
