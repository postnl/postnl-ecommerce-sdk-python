
# Labelling Error

## Structure

`LabellingError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Optional | The error reason |
| `code` | `str` | Optional | The error code |
| `description` | `str` | Optional | The description of the error |

## Example (as JSON)

```json
{
  "Error": "Validation failed for shipment: 3SDEVC949511897",
  "Code": "1280202",
  "Description": "Incorrect address specified in address type Sender"
}
```

