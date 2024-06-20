
# Invalid Request Exception

## Structure

`InvalidRequestException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `datetime` | Optional | - |
| `error` | [`Error`](../../doc/models/error.md) | Optional | - |
| `request_id` | `str` | Optional | - |

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

