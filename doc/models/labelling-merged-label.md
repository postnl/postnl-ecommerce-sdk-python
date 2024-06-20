
# Labelling Merged Label

## Structure

`LabellingMergedLabel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcodes` | `List[str]` | Optional | - |
| `labels` | [`List[LabellingLabel]`](../../doc/models/labelling-label.md) | Optional | - |

## Example (as JSON)

```json
{
  "Barcodes": [
    "Barcodes9",
    "Barcodes0",
    "Barcodes1"
  ],
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
  ]
}
```

