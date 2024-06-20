
# Timeframe Timeframe

## Structure

`TimeframeTimeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | `str` | Optional | The start time of the expected delivery window |
| `options` | [`Options`](../../doc/models/options.md) | Optional | The delivery option for which the timeframe is calculated. See [Delivery Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/delivery-options) for possible values. |
| `to` | `str` | Optional | The end time of the expected delivery window |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes) for possible values. |

## Example (as JSON)

```json
{
  "From": "12:30:00",
  "To": "14:30:00",
  "Options": {
    "string": "Morning"
  },
  "Sustainability": {
    "Code": "02",
    "Description": "Description4"
  }
}
```

