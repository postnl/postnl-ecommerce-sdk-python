
# Status

The current status of the shipment (see the [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/t-t-status-codes/event-codes) for possible values.

## Structure

`Status`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_stamp` | [`str`](../../doc/models/string-enum.md) | Optional | The status timestamp |
| `status_code` | [`str`](../../doc/models/string-enum.md) | Optional | The status code |
| `status_description` | [`str`](../../doc/models/string-enum.md) | Optional | The status description |
| `phase_code` | [`str`](../../doc/models/string-enum.md) | Optional | The phase code |
| `phase_description` | [`str`](../../doc/models/string-enum.md) | Optional | The phase description |

## Example (as JSON)

```json
{
  "TimeStamp": "07-11-2022 19:10:28",
  "StatusCode": "1",
  "StatusDescription": "Zending voorgemeld",
  "PhaseCode": "1",
  "PhaseDescription": "Collectie"
}
```

