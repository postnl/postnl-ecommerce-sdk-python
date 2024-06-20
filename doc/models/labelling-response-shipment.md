
# Labelling Response Shipment

## Structure

`LabellingResponseShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_code_delivery` | `str` | Optional | The product code of the shipment |
| `labels` | [`List[LabellingLabel]`](../../doc/models/labelling-label.md) | Optional | All labels belonging to the selected product |
| `barcode` | `str` | Optional | The barcode used on the label |
| `errors` | `List[object]` | Optional | - |
| `warnings` | [`List[Warning]`](../../doc/models/warning.md) | Optional | Possible warnings. See the [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values |

## Example (as JSON)

```json
{
  "ProductCodeDelivery": "3085",
  "Barcode": "3SDEVC281677095",
  "Labels": [
    {
      "Content": "Content4",
      "Labeltype": "Labeltype2",
      "OutputType": "OutputType4"
    }
  ],
  "Errors": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
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

