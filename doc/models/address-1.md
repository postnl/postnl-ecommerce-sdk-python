
# Address 1

The pickup location address

## Structure

`Address1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | [`str`](../../doc/models/string-enum.md) | Optional | The pickup location street |
| `zipcode` | [`str`](../../doc/models/string-enum.md) | Optional | The pickup location zipcode |
| `house_nr` | `int` | Optional | The pickup location housenumber |
| `house_nr_ext` | [`str`](../../doc/models/string-enum.md) | Optional | The pickup location housenumber extension |
| `countrycode` | [`str`](../../doc/models/string-enum.md) | Optional | The pickup location country |
| `company_name` | [`str`](../../doc/models/string-enum.md) | Optional | The pickup location company name |

## Example (as JSON)

```json
{
  "Street": "Siriusdreef",
  "Zipcode": "2132WT",
  "HouseNr": 42,
  "HouseNrExt": "-60",
  "Countrycode": "NL",
  "CompanyName": "Pickup company BV"
}
```

