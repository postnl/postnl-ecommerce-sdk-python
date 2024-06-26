
# Timeframe Response

## Structure

`TimeframeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timeframes` | [`Timeframes`](../../doc/models/timeframes.md) | Optional | - |
| `reason_no_timeframes` | [`ReasonNoTimeframes`](../../doc/models/reason-no-timeframes.md) | Optional | - |

## Example (as JSON)

```json
{
  "Timeframes": {
    "Timeframe": [
      {
        "Date": "Date2",
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
    ]
  },
  "ReasonNoTimeframes": {
    "ReasonNoTimeframe": [
      {
        "Code": "Code0",
        "Date": "Date8",
        "Description": "Description6",
        "Options": {
          "string": "Morning"
        },
        "Sustainability": {
          "Code": "02",
          "Description": "Description4"
        }
      }
    ]
  }
}
```

