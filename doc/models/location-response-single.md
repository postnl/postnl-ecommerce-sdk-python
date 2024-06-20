
# Location Response Single

## Structure

`LocationResponseSingle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `get_locations_result` | [`GetLocationsResultSingle`](../../doc/models/get-locations-result-single.md) | Optional | - |

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

