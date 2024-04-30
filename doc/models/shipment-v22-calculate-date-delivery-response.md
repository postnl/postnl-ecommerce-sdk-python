
# Shipment V22 Calculate Date Delivery Response

## Structure

`ShipmentV22CalculateDateDeliveryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Optional | - |
| `options` | [`Options`](../../doc/models/options.md) | Optional | The delivery options for which a delivery date is returned. Only one delivery option is specified. See [Delivery Options](#tag/Reference-codes/Delivery-options) for possible values. |
| `sustainability` | [`Warning1`](../../doc/models/warning-1.md) | Optional | Sustainability score; see [Sustainability codes](#tag/Reference-codes/Sustainability-codes) for possible values. |

## Example (as JSON)

```json
{
  "DeliveryDate": "30-05-2022",
  "Options": {
    "string": "Today"
  },
  "Sustainability": {
    "Code": "Code2",
    "Description": "Description4"
  }
}
```

