
# Deliverydate Delivery Response

## Structure

`DeliverydateDeliveryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | `str` | Optional | - |
| `options` | [`DeliverydateOptions`](../../doc/models/deliverydate-options.md) | Optional | The delivery options for which a delivery date is returned. Only one delivery option is specified. See [Delivery Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/delivery-options) for possible values. |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/sustainability-codes) for possible values. |

## Example (as JSON)

```json
{
  "DeliveryDate": "30-05-2022",
  "Options": {
    "string": "Today"
  },
  "Sustainability": {
    "Code": "02",
    "Description": "Description4"
  }
}
```

