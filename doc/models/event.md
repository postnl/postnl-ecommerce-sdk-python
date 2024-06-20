
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The event code |
| `description` | `str` | Optional | The event description |
| `destination_location_code` | `str` | Optional | Location code of the destination |
| `location_code` | `str` | Optional | The current location code |
| `route_code` | `str` | Optional | The route code |
| `route_number` | `str` | Optional | The route number |
| `time_stamp` | `str` | Optional | Timestamp of the event |

## Example (as JSON)

```json
{
  "Code": "A01",
  "Description": "Pakket is nog niet door PostNL ontvangen of verwerkt",
  "DestinationLocationCode": "888888",
  "LocationCode": "156789",
  "RouteCode": "310",
  "RouteNumber": "310 Sittard Vrangendael",
  "TimeStamp": "07-11-2022 19:10:28"
}
```

