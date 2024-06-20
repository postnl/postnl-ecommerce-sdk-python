
# Fault Shipping Status API

## Structure

`FaultShippingStatusAPI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `faultstring` | `str` | Optional | - |
| `detail` | [`Detail`](../../doc/models/detail.md) | Optional | - |

## Example (as JSON)

```json
{
  "faultstring": "no barcode supplied in path",
  "detail": {
    "errorcode": "errorcode6"
  }
}
```

