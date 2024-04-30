
# Get Locations Result

## Structure

`GetLocationsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_location` | [`List[Location1]`](../../doc/models/location-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "ResponseLocation": [
    {
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
  ]
}
```

