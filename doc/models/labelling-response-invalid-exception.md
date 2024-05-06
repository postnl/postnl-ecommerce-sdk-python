
# Labelling Response Invalid Exception

## Structure

`LabellingResponseInvalidException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List[Error3]`](../../doc/models/error-3.md) | Optional | A list of errors returned from the webservice. See the [Error codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values. |

## Example (as JSON)

```json
{
  "Errors": [
    {
      "Error": "Error8",
      "Code": "Code4",
      "Description": "Description2"
    }
  ]
}
```

