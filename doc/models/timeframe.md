
# Timeframe

## Structure

`Timeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | [`str`](../../doc/models/string-enum.md) | Optional | Format hh:mm:ss |
| `to` | [`str`](../../doc/models/string-enum.md) | Optional | Format hh:mm:ss |
| `options` | [`List[Option1Enum]`](../../doc/models/option-1-enum.md) | Optional | The delivery options applicable to the timeframe information. See [Delivery Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes) for possible values. |
| `shipping_date` | [`str`](../../doc/models/string-enum.md) | Optional | The date when you need to deliver the shipment to PostNL to ensure the expected delivery date is achieved. Will be returned as 'null' if not calculated |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes) for possible values. |

## Example (as JSON)

```json
{
  "From": "18:00:00",
  "To": "22:30:00",
  "ShippingDate": "08-07-2019",
  "Options": [
    "Today",
    "08:00-10:00",
    "08:00-12:00"
  ],
  "Sustainability": {
    "Code": "02",
    "Description": "Description4"
  }
}
```

