
# Checkout Time Frame

## Structure

`CheckoutTimeFrame`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | `str` | Optional | Format hh:mm:ss |
| `to` | `str` | Optional | Format hh:mm:ss |
| `options` | [`List[CheckoutOptionEnum]`](../../doc/models/checkout-option-enum.md) | Optional | The delivery options applicable to the timeframe information. See [Delivery Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/delivery-options) for possible values. |
| `shipping_date` | `str` | Optional | The date when you need to deliver the shipment to PostNL to ensure the expected delivery date is achieved. Will be returned as 'null' if not calculated |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/sustainability-codes) for possible values. |

## Example (as JSON)

```json
{
  "From": "18:00:00",
  "To": "22:30:00",
  "ShippingDate": "08-07-2019",
  "Options": [
    "08:00-10:00",
    "Today",
    "Sameday"
  ],
  "Sustainability": {
    "Code": "02",
    "Description": "Description4"
  }
}
```

