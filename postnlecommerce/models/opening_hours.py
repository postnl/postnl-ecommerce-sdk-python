# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.opening_hours_per_day import OpeningHoursPerDay


class OpeningHours(object):

    """Implementation of the 'OpeningHours' model.

    The standard opening hours of the pickup location

    Attributes:
        monday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        tuesday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        wednesday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        thursday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        friday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        saturday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.
        sunday (OpeningHoursPerDay): The model property of type
            OpeningHoursPerDay.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "monday": 'Monday',
        "tuesday": 'Tuesday',
        "wednesday": 'Wednesday',
        "thursday": 'Thursday',
        "friday": 'Friday',
        "saturday": 'Saturday',
        "sunday": 'Sunday'
    }

    _optionals = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    ]

    def __init__(self,
                 monday=APIHelper.SKIP,
                 tuesday=APIHelper.SKIP,
                 wednesday=APIHelper.SKIP,
                 thursday=APIHelper.SKIP,
                 friday=APIHelper.SKIP,
                 saturday=APIHelper.SKIP,
                 sunday=APIHelper.SKIP):
        """Constructor for the OpeningHours class"""

        # Initialize members of the class
        if monday is not APIHelper.SKIP:
            self.monday = monday 
        if tuesday is not APIHelper.SKIP:
            self.tuesday = tuesday 
        if wednesday is not APIHelper.SKIP:
            self.wednesday = wednesday 
        if thursday is not APIHelper.SKIP:
            self.thursday = thursday 
        if friday is not APIHelper.SKIP:
            self.friday = friday 
        if saturday is not APIHelper.SKIP:
            self.saturday = saturday 
        if sunday is not APIHelper.SKIP:
            self.sunday = sunday 

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
        monday = OpeningHoursPerDay.from_dictionary(dictionary.get('Monday')) if 'Monday' in dictionary.keys() else APIHelper.SKIP
        tuesday = OpeningHoursPerDay.from_dictionary(dictionary.get('Tuesday')) if 'Tuesday' in dictionary.keys() else APIHelper.SKIP
        wednesday = OpeningHoursPerDay.from_dictionary(dictionary.get('Wednesday')) if 'Wednesday' in dictionary.keys() else APIHelper.SKIP
        thursday = OpeningHoursPerDay.from_dictionary(dictionary.get('Thursday')) if 'Thursday' in dictionary.keys() else APIHelper.SKIP
        friday = OpeningHoursPerDay.from_dictionary(dictionary.get('Friday')) if 'Friday' in dictionary.keys() else APIHelper.SKIP
        saturday = OpeningHoursPerDay.from_dictionary(dictionary.get('Saturday')) if 'Saturday' in dictionary.keys() else APIHelper.SKIP
        sunday = OpeningHoursPerDay.from_dictionary(dictionary.get('Sunday')) if 'Sunday' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(monday,
                   tuesday,
                   wednesday,
                   thursday,
                   friday,
                   saturday,
                   sunday)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'monday={(self.monday if hasattr(self, "monday") else None)!r}, '
                f'tuesday={(self.tuesday if hasattr(self, "tuesday") else None)!r}, '
                f'wednesday={(self.wednesday if hasattr(self, "wednesday") else None)!r}, '
                f'thursday={(self.thursday if hasattr(self, "thursday") else None)!r}, '
                f'friday={(self.friday if hasattr(self, "friday") else None)!r}, '
                f'saturday={(self.saturday if hasattr(self, "saturday") else None)!r}, '
                f'sunday={(self.sunday if hasattr(self, "sunday") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'monday={(self.monday if hasattr(self, "monday") else None)!s}, '
                f'tuesday={(self.tuesday if hasattr(self, "tuesday") else None)!s}, '
                f'wednesday={(self.wednesday if hasattr(self, "wednesday") else None)!s}, '
                f'thursday={(self.thursday if hasattr(self, "thursday") else None)!s}, '
                f'friday={(self.friday if hasattr(self, "friday") else None)!s}, '
                f'saturday={(self.saturday if hasattr(self, "saturday") else None)!s}, '
                f'sunday={(self.sunday if hasattr(self, "sunday") else None)!s})')
