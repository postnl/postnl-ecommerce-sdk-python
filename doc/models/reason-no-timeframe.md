
# Reason No Timeframe

## Structure

`ReasonNoTimeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | [`str`](../../doc/models/string-enum.md) | Optional | The reason code |
| `date` | [`str`](../../doc/models/string-enum.md) | Optional | The date associated with the reason no timeframe was calculated |
| `description` | [`str`](../../doc/models/string-enum.md) | Optional | The description associated with the reason no timeframe was calculated |
| `options` | [`Options`](../../doc/models/options.md) | Optional | The option for which no timeframe was calculated for a specific date |
| `sustainability` | [`Warning1`](../../doc/models/warning-1.md) | Optional | Sustainability score |

## Example (as JSON)

```json
{
  "Code": "1",
  "Date": "02-07-2022",
  "Description": "Delivery date not allowed",
  "Options": {
    "string": "Today"
  },
  "Sustainability": {
    "Code": "Code2",
    "Description": "Description4"
  }
}
```

