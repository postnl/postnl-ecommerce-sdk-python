
# Cpc Response

## Structure

`CpcResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | [`str`](../../doc/models/string-enum.md) | Optional | City of requested address |
| `postal_code` | [`str`](../../doc/models/string-enum.md) | Optional | Postalcode of requested address |
| `street_name` | [`str`](../../doc/models/string-enum.md) | Optional | Street of requested address |
| `house_number` | `int` | Optional | Housenumber of requested address |
| `formatted_address` | [`List[str]`](../../doc/models/string-enum.md) | Optional | Full formatted address according to PostNL standard (returns each line as a separate string) |

## Example (as JSON)

```json
{
  "city": "UTRECHT",
  "postalCode": "3571ZZ",
  "streetName": "Molengraaffplantsoen",
  "houseNumber": 74,
  "formattedAddress": [
    "Molengraaffplantsoen 74",
    "3571ZZ UTRECHT"
  ]
}
```

