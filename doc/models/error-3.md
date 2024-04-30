
# Error 3

## Structure

`Error3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | [`str`](../../doc/models/string-enum.md) | Optional | The error reason |
| `code` | [`str`](../../doc/models/string-enum.md) | Optional | The error code |
| `description` | [`str`](../../doc/models/string-enum.md) | Optional | The description of the error |

## Example (as JSON)

```json
{
  "Error": "Validation failed for shipment: 3SDEVC949511897",
  "Code": "1280202",
  "Description": "Incorrect address specified in address type Sender"
}
```

