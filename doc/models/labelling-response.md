
# Labelling Response

## Structure

`LabellingResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merged_labels` | [`List[MergedLabel]`](../../doc/models/merged-label.md) | Optional | The merged label output; only returned if the printer type selected in your request merges the pdf labels into a single file (e.g. using GraphicFile\|Merge). |
| `response_shipments` | [`List[ResponseShipment1]`](../../doc/models/response-shipment-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "MergedLabels": [
    {
      "Barcodes": [
        "Barcodes9"
      ],
      "Labels": [
        {
          "Content": "Content4",
          "Labeltype": "Labeltype2",
          "OutputType": "OutputType4"
        }
      ]
    },
    {
      "Barcodes": [
        "Barcodes9"
      ],
      "Labels": [
        {
          "Content": "Content4",
          "Labeltype": "Labeltype2",
          "OutputType": "OutputType4"
        }
      ]
    }
  ],
  "ResponseShipments": [
    {
      "ProductCodeDelivery": "ProductCodeDelivery2",
      "Labels": [
        {
          "Content": "Content4",
          "Labeltype": "Labeltype2",
          "OutputType": "OutputType4"
        }
      ],
      "Barcode": "Barcode0",
      "Warnings": [
        {
          "Code": "Code4",
          "Description": "Description8"
        }
      ]
    },
    {
      "ProductCodeDelivery": "ProductCodeDelivery2",
      "Labels": [
        {
          "Content": "Content4",
          "Labeltype": "Labeltype2",
          "OutputType": "OutputType4"
        }
      ],
      "Barcode": "Barcode0",
      "Warnings": [
        {
          "Code": "Code4",
          "Description": "Description8"
        }
      ]
    }
  ]
}
```

