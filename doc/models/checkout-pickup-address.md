
# Checkout Pickup Address

The pickup location address

## Structure

`CheckoutPickupAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | The pickup location street |
| `zipcode` | `str` | Optional | The pickup location zipcode |
| `house_nr` | `int` | Optional | The pickup location housenumber |
| `house_nr_ext` | `str` | Optional | The pickup location housenumber extension |
| `countrycode` | `str` | Optional | The pickup location country |
| `company_name` | `str` | Optional | The pickup location company name |

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

