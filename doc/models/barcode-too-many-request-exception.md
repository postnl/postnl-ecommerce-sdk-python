
# Barcode Too Many Request Exception

## Structure

`BarcodeTooManyRequestException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | [`str`](../../doc/models/string-enum.md) | Optional | - |
| `http_status_code` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Too many requests. Rate limit exceeded!",
  "http_status_code": 429.0
}
```

