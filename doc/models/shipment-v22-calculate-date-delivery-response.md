
# Shipment V22 Calculate Date Delivery Response

## Structure

`ShipmentV22CalculateDateDeliveryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Optional | - |
| `options` | [`Options`](../../doc/models/options.md) | Optional | The delivery options for which a delivery date is returned. Only one delivery option is specified. See [Delivery Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/delivery-options) for possible values. |
| `sustainability` | [`Warning1`](../../doc/models/warning-1.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/delivery-options) for possible values. |

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

