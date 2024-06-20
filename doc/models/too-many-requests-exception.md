
# Too Many Requests Exception

## Structure

`TooManyRequestsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `http_status_code` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "message": "Too many requests. Rate limit exceeded!",
  "http_status_code": 429.0
}
```

