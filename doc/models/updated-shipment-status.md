
# Updated Shipment Status

The status update. See [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values.

## Structure

`UpdatedShipmentStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `str` | Optional | The timestamp of the update |
| `status_code` | `str` | Optional | The status code |
| `status_description` | `str` | Optional | The status description |
| `phase_code` | `str` | Optional | The phase code |
| `phase_description` | `str` | Optional | The phase description |

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

