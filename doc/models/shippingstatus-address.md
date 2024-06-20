
# Shippingstatus Address

## Structure

`ShippingstatusAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name |
| `last_name` | `str` | Optional | The last name |
| `company_name` | `str` | Optional | The company name |
| `department_name` | `str` | Optional | The department name |
| `country_code` | `str` | Optional | The ISO2 country code |
| `zipcode` | `str` | Optional | The zipcode |
| `region` | `str` | Optional | The region name |
| `district` | `str` | Optional | The district name |
| `city` | `str` | Optional | The city name |
| `street` | `str` | Optional | The street name |
| `house_number` | `str` | Optional | The house number |
| `house_number_suffix` | `str` | Optional | The house number suffix |
| `building` | `str` | Optional | The building name |
| `floor` | `str` | Optional | The floor of the building |
| `remark` | `str` | Optional | An additional remark |

## Example (as JSON)

```json
{
  "FirstName": "Peter",
  "LastName": "de Ruiter",
  "CompanyName": "PostNL",
  "DepartmentName": "IT",
  "CountryCode": "NL",
  "Zipcode": "2132WT",
  "Region": "Noord-Holland",
  "District": "Beukenhorst",
  "City": "Hoofddorp",
  "Street": "Siriusdreef",
  "HouseNumber": "42",
  "HouseNumberSuffix": "-60",
  "Building": "AA",
  "Floor": "4",
  "Remark": "No doorbell"
}
```

