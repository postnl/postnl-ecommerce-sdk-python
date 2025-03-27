# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class HazardousMaterial(object):

    """Implementation of the 'HazardousMaterial' model.

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

        if not isinstance(dictionary, dict) or dictionary is None:
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'toxic_substance_code={self.toxic_substance_code!r}, '
                f'additional_toxic_substance_code={(self.additional_toxic_substance_code if hasattr(self, "additional_toxic_substance_code") else None)!r}, '
                f'adr_points={(self.adr_points if hasattr(self, "adr_points") else None)!r}, '
                f'tunnel_code={(self.tunnel_code if hasattr(self, "tunnel_code") else None)!r}, '
                f'packaging_group_code={(self.packaging_group_code if hasattr(self, "packaging_group_code") else None)!r}, '
                f'packaging_group_description={(self.packaging_group_description if hasattr(self, "packaging_group_description") else None)!r}, '
                f'gross_weight={(self.gross_weight if hasattr(self, "gross_weight") else None)!r}, '
                f'undg_number={(self.undg_number if hasattr(self, "undg_number") else None)!r}, '
                f'transport_category_code={(self.transport_category_code if hasattr(self, "transport_category_code") else None)!r}, '
                f'chemical_technical_description={(self.chemical_technical_description if hasattr(self, "chemical_technical_description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'toxic_substance_code={self.toxic_substance_code!s}, '
                f'additional_toxic_substance_code={(self.additional_toxic_substance_code if hasattr(self, "additional_toxic_substance_code") else None)!s}, '
                f'adr_points={(self.adr_points if hasattr(self, "adr_points") else None)!s}, '
                f'tunnel_code={(self.tunnel_code if hasattr(self, "tunnel_code") else None)!s}, '
                f'packaging_group_code={(self.packaging_group_code if hasattr(self, "packaging_group_code") else None)!s}, '
                f'packaging_group_description={(self.packaging_group_description if hasattr(self, "packaging_group_description") else None)!s}, '
                f'gross_weight={(self.gross_weight if hasattr(self, "gross_weight") else None)!s}, '
                f'undg_number={(self.undg_number if hasattr(self, "undg_number") else None)!s}, '
                f'transport_category_code={(self.transport_category_code if hasattr(self, "transport_category_code") else None)!s}, '
                f'chemical_technical_description={(self.chemical_technical_description if hasattr(self, "chemical_technical_description") else None)!s})')
