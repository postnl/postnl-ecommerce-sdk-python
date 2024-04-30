
# Merged Label

## Structure

`MergedLabel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcodes` | [`List[str]`](../../doc/models/string-enum.md) | Optional | - |
| `labels` | [`List[Label]`](../../doc/models/label.md) | Optional | - |

## Example (as JSON)

```json
{
  "Barcodes": [
    "Barcodes7",
    "Barcodes8"
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
    }
  ]
}
```

