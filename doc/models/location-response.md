
# Location Response

## Structure

`LocationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `get_locations_result` | [`GetLocationsResult1`](../../doc/models/get-locations-result-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "GetLocationsResult": {
    "ResponseLocation": {
      "Address": {
        "City": "City6",
        "Countrycode": "Countrycode2",
        "HouseNr": 136,
        "HouseNrExt": "HouseNrExt4",
        "Remark": "Remark8"
      },
      "DeliveryOptions": {
        "string": [
          "string6",
          "string7"
        ]
      },
      "Distance": 244,
      "Latitude": 103.5,
      "LocationCode": 102
    }
  }
}
```

