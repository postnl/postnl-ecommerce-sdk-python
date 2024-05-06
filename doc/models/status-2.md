
# Status 2

The status update. See [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values.

## Structure

`Status2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | [`str`](../../doc/models/string-enum.md) | Optional | The timestamp of the update |
| `status_code` | [`str`](../../doc/models/string-enum.md) | Optional | The status code |
| `status_description` | [`str`](../../doc/models/string-enum.md) | Optional | The status description |
| `phase_code` | [`str`](../../doc/models/string-enum.md) | Optional | The phase code |
| `phase_description` | [`str`](../../doc/models/string-enum.md) | Optional | The phase description |

## Example (as JSON)

```json
{
  "Timestamp": "11/07/2022 12:36:41",
  "StatusCode": "1",
  "StatusDescription": "Zending voorgemeld",
  "PhaseCode": "1",
  "PhaseDescription": "Collectie"
}
```

