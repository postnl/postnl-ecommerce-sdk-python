
# Reason No Timeframe

## Structure

`ReasonNoTimeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code |
| `date` | `str` | Optional | The date associated with the reason no timeframe was calculated |
| `description` | `str` | Optional | The description associated with the reason no timeframe was calculated |
| `options` | [`NoTimeframesOptions`](../../doc/models/no-timeframes-options.md) | Optional | The option for which no timeframe was calculated for a specific date |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes) for possible values. |

## Example (as JSON)

```json
{
  "Code": "1",
  "Date": "02-07-2022",
  "Description": "Delivery date not allowed",
  "Options": {
    "string": "Morning"
  },
  "Sustainability": {
    "Code": "02",
    "Description": "Description4"
  }
}
```

