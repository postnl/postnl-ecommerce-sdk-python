
# Postalcode Check Address

## Structure

`PostalcodeCheckAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | City of requested address |
| `postal_code` | `str` | Optional | Postalcode of requested address |
| `street_name` | `str` | Optional | Street of requested address |
| `house_number` | `int` | Optional | Housenumber of requested address |
| `house_number_addition` | `str` | Optional | Housenumber addition |
| `formatted_address` | `List[str]` | Optional | Full formatted address according to PostNL standard (returns each line as a separate string) |

## Example (as JSON)

```json
{
  "city": "UTRECHT",
  "postalCode": "3571ZZ",
  "streetName": "Molengraaffplantsoen",
  "houseNumber": 74,
  "houseNumberAddition": "bis",
  "formattedAddress": [
    "Molengraaffplantsoen 74",
    "3571ZZ UTRECHT"
  ]
}
```

