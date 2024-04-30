
# Label

## Structure

`Label`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | [`str`](../../doc/models/string-enum.md) | Optional | Base64 encoded label content |
| `labeltype` | [`str`](../../doc/models/string-enum.md) | Optional | Type of the label. See possible [Label types](#tag/Reference-codes/Label-types) |
| `output_type` | [`str`](../../doc/models/string-enum.md) | Optional | Content type of the label, e.g. zebra of pdf. |

## Example (as JSON)

```json
{
  "Content": "JVBERi0xLjMKJeLjz9MKNSAwIG9iago8PAovQ29udGVudHMg[TRUNCATED]",
  "Labeltype": "Label",
  "OutputType": "PDF"
}
```

