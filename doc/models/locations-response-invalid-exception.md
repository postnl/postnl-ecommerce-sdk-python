
# Locations Response Invalid Exception

## Structure

`LocationsResponseInvalidException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `datetime` | Optional | - |
| `error` | [`Error1`](../../doc/models/error-1.md) | Optional | - |
| `request_id` | [`str`](../../doc/models/string-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "09fd61fe-0099-4349-b71d-dce5c2472be9",
  "Date": "2016-03-13T12:52:32.123Z",
  "Error": {
    "ErrorCode": "ErrorCode6",
    "ErrorDescription": "ErrorDescription0"
  }
}
```

