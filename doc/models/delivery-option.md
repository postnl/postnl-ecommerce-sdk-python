
# Delivery Option

## Structure

`DeliveryOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Optional | The possible delivery date |
| `timeframe` | [`List[Timeframe]`](../../doc/models/timeframe.md) | Optional | Array of timeframes |

## Example (as JSON)

```json
{
  "DeliveryDate": "09-07-2019",
  "Timeframe": [
    {
      "From": "From0",
      "To": "To0",
      "Options": [
        "Today",
        "08:00-10:00",
        "08:00-12:00"
      ],
      "ShippingDate": "ShippingDate4",
      "Sustainability": {
        "Code": "02",
        "Description": "Description4"
      }
    }
  ]
}
```

