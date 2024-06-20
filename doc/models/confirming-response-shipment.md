
# Confirming Response Shipment

## Structure

`ConfirmingResponseShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[ConfirmingError]`](../../doc/models/confirming-error.md) | Optional | Possible errors. See the [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values |
| `warnings` | [`List[Warning]`](../../doc/models/warning.md) | Optional | Possible warnings. See the [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values |
| `barcode` | `str` | Optional | The barcode used |

## Example (as JSON)

```json
{
  "Barcode": "3SDEVC281677095",
  "Errors": [
    {
      "Code": "Code4",
      "Description": "Description2"
    },
    {
      "Code": "Code4",
      "Description": "Description2"
    }
  ],
  "Warnings": [
    {
      "Code": "Code4",
      "Description": "Description8"
    }
  ]
}
```

