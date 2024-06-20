
# Timeframe

## Structure

`Timeframe`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `str` | Optional | The expected date of delivery |
| `timeframes` | [`TimeframesResponseObject`](../../doc/models/timeframes-response-object.md) | Optional | - |

## Example (as JSON)

```json
{
  "Date": "02-07-2022",
  "Timeframes": {
    "TimeframeTimeframe": [
      {
        "From": "From8",
        "Options": {
          "string": "Morning"
        },
        "To": "To2",
        "Sustainability": {
          "Code": "02",
          "Description": "Description4"
        }
      },
      {
        "From": "From8",
        "Options": {
          "string": "Morning"
        },
        "To": "To2",
        "Sustainability": {
          "Code": "02",
          "Description": "Description4"
        }
      }
    ]
  }
}
```

