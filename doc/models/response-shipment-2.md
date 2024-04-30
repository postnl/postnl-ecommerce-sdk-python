
# Response Shipment 2

## Structure

`ResponseShipment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_code_delivery` | [`str`](../../doc/models/string-enum.md) | Optional | The product code of the shipment |
| `labels` | [`List[Label]`](../../doc/models/label.md) | Optional | All labels belonging to the selected product |
| `barcode` | [`str`](../../doc/models/string-enum.md) | Optional | The barcode used on the label |
| `warnings` | [`List[Warning1]`](../../doc/models/warning-1.md) | Optional | Possible warnings. See the [Error Codes](#tag/Error-codes) for possible values |

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
    },
    {
      "Content": "Content4",
      "Labeltype": "Labeltype2",
      "OutputType": "OutputType4"
    },
    {
      "Content": "Content4",
      "Labeltype": "Labeltype2",
      "OutputType": "OutputType4"
    }
  ],
  "Warnings": [
    {
      "Code": "Code4",
      "Description": "Description8"
    },
    {
      "Code": "Code4",
      "Description": "Description8"
    },
    {
      "Code": "Code4",
      "Description": "Description8"
    }
  ]
}
```

