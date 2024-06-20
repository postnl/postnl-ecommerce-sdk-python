
# Checkout Cut Off Time

## Structure

`CheckoutCutOffTime`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day` | [`CheckoutCutOffDayEnum`](../../doc/models/checkout-cut-off-day-enum.md) | Required | The day for which the cutoff time applies. 00 is your default cutoff that applies to all otherwise not specified days, 01 to 07 is Monday to Sunday. |
| `available` | `bool` | Optional | Specifies whether you are available to process shipments during the selected day |
| `mtype` | [`CheckoutCutOffTypeEnum`](../../doc/models/checkout-cut-off-type-enum.md) | Optional | Specifies the type belonging to the cutoff time. |
| `time` | `str` | Optional | Specifies the cutoff time (mandatory when Available is true)<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |

## Example (as JSON)

```json
{
  "Day": "00",
  "Available": true,
  "Type": "Regular",
  "Time": "23:00:00"
}
```

