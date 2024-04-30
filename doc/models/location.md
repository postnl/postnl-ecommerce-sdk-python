
# Location

## Structure

`Location`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address1`](../../doc/models/address-1.md) | Optional | The pickup location address |
| `pickup_time` | [`str`](../../doc/models/string-enum.md) | Optional | Time from when the parcel can be retrieved at the pickup location |
| `opening_hours` | [`OpeningHours`](../../doc/models/opening-hours.md) | Optional | The standard opening hours of the pickup location |
| `distance` | `int` | Optional | The calculated distance (in meters) between the location specified and the address provided in the request |
| `location_code` | [`str`](../../doc/models/string-enum.md) | Optional | The location identifier |
| `partner_id` | [`str`](../../doc/models/string-enum.md) | Optional | The partner identifier; not used anymore |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](#tag/Reference-codes/Sustainability-codes) for possible values. |

## Example (as JSON)

```json
{
  "PickupTime": "15:00",
  "Distance": 234,
  "LocationCode": "8101163043",
  "PartnerID": "PNPNL-01",
  "Address": {
    "Street": "Street6",
    "Zipcode": "Zipcode8",
    "HouseNr": 136,
    "HouseNrExt": "HouseNrExt4",
    "Countrycode": "Countrycode2"
  },
  "OpeningHours": {
    "Monday": {
      "From": "From0",
      "To": "To0"
    },
    "Tuesday": {
      "From": "From2",
      "To": "To2"
    },
    "Wednesday": {
      "From": "From4",
      "To": "To4"
    },
    "Thursday": {
      "From": "From0",
      "To": "To0"
    },
    "Friday": {
      "From": "From6",
      "To": "To4"
    }
  }
}
```

