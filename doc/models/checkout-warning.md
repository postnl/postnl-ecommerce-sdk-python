
# Checkout Warning

## Structure

`CheckoutWarning`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | `str` | Optional | Deliverydate that triggered the warning |
| `code` | `str` | Optional | Warning code (for a possible list of warnings, see the generic error codes page) |
| `description` | `str` | Optional | Warning description (for a possible list of warnings, see the generic error codes page) |
| `options` | [`CheckoutWarningOptionEnum`](../../doc/models/checkout-warning-option-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "DeliveryDate": "07-07-2019",
  "Code": "5034",
  "Description": "No delivery option found on date",
  "Options": "Daytime"
}
```

