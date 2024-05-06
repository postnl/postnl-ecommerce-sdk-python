
# Barcode Response Invalid Exception

## Structure

`BarcodeResponseInvalidException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[Error]`](../../doc/models/error.md) | Optional | A list of errors. See [Error codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values. |

## Example (as JSON)

```json
{
  "errors": [
    {
      "ErrorMsg": "ErrorMsg2",
      "ErrorNumber": "ErrorNumber0"
    }
  ]
}
```

