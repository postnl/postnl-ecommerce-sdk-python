
# Response Shipment

## Structure

`ResponseShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[Error2]`](../../doc/models/error-2.md) | Optional | Possible errors. See the [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values |
| `warnings` | [`List[Warning1]`](../../doc/models/warning-1.md) | Optional | Possible warnings. See the [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values |
| `barcode` | [`str`](../../doc/models/string-enum.md) | Optional | The barcode used |

## Example (as JSON)

```json
{
  "Barcode": "3SDEVC281677095",
  "Errors": [
    {
      "code": "code2",
      "description": "description6"
    },
    {
      "code": "code2",
      "description": "description6"
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

