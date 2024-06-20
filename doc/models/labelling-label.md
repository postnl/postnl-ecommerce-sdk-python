
# Labelling Label

## Structure

`LabellingLabel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Optional | Base64 encoded label content |
| `labeltype` | `str` | Optional | Type of the label. See possible [Label types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/label-types) |
| `output_type` | `str` | Optional | Content type of the label, e.g. zebra of pdf. |

## Example (as JSON)

```json
{
  "Content": "JVBERi0xLjMKJeLjz9MKNSAwIG9iago8PAovQ29udGVudHMg[TRUNCATED]",
  "Labeltype": "Label",
  "OutputType": "PDF"
}
```

