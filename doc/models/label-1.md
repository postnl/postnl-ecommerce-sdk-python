
# Label 1

## Structure

`Label1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | [`str`](../../doc/models/string-enum.md) | Optional | Base64 encoded label content |
| `labeltype` | [`str`](../../doc/models/string-enum.md) | Optional | Type of the label. See Guidelines |
| `output_type` | [`str`](../../doc/models/string-enum.md) | Optional | Content type of the label, e.g. zebra of pdf. Note: It is not recommended to send .PDF files/labels directly to a Zebra printer. See Guidelines. |

## Example (as JSON)

```json
{
  "Content": "JVBERi0xLjMKJeLjz9MKNSAwIG9iago8PAovQ29udGVudHMg[TRUNCATED]",
  "Labeltype": "Label",
  "OutputType": "PDF"
}
```

