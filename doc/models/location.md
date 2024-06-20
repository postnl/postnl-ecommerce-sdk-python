
# Location

## Structure

`Location`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`LocationsAddress`](../../doc/models/locations-address.md) | Optional | - |
| `delivery_options` | [`DeliveryOptions`](../../doc/models/delivery-options.md) | Optional | The options belonging to the pickup location. The delivery options RETA, UL, PU, DO, BW, RT and BWUL can be shown in the response. Please ignore these codes. These codes are internal PostNL codes. |
| `distance` | `int` | Optional | The distance from the address/coordinates provided in the request to the pickup location returned. Distance in meters. |
| `latitude` | `float` | Optional | The latitude of the pickup location |
| `location_code` | `int` | Optional | The pickup location identifier |
| `longitude` | `float` | Optional | The longitude of the pickup location |
| `name` | `str` | Optional | The name of the pickup location |
| `opening_hours` | [`LocationsOpeningHours`](../../doc/models/locations-opening-hours.md) | Optional | The standard opening times of the pickup location |
| `sustainability` | [`Sustainability`](../../doc/models/sustainability.md) | Optional | Sustainability score; see [Sustainability codes](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes) for possible values. |
| `partner_name` | `str` | Optional | The partner name belonging to the pickup location. Can be ignored, no longer used. |
| `retail_network_id` | `str` | Optional | The retail network belonging to the pickup location. Can be ignored, no longer used |

## Example (as JSON)

```json
{
  "Distance": 102,
  "Latitude": 52.10223388,
  "LocationCode": 163043,
  "Longitude": 5.13634192,
  "Name": "Tonys Tabakszaak",
  "PartnerName": "PostNL",
  "RetailNetworkID": "PNPNL-01",
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
  }
}
```

