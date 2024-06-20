# Locations

```python
locations_controller = client.locations
```

## Class Name

`LocationsController`

## Methods

* [Get Pickup Locations by Address](../../doc/controllers/locations.md#get-pickup-locations-by-address)
* [Get Pickup Locations by Coordinates](../../doc/controllers/locations.md#get-pickup-locations-by-coordinates)
* [Get Pickup Locations Within Area](../../doc/controllers/locations.md#get-pickup-locations-within-area)
* [Get Pickup Location](../../doc/controllers/locations.md#get-pickup-location)


# Get Pickup Locations by Address

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest?CountryCode=NL&PostalCode=2132WT&City=Hoofddorp&Street=Siriusdreef&HouseNumber=42&HouseNumberExtension=-60&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def get_pickup_locations_by_address(self,
                                   country_code,
                                   postal_code,
                                   city=None,
                                   street=None,
                                   house_number=None,
                                   house_number_extension=None,
                                   delivery_date=None,
                                   opening_time=None,
                                   delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | The country of the recipient's address |
| `postal_code` | `str` | Query, Required | The zipcode of the recipient's address |
| `city` | `str` | Query, Optional | The city of the recipient's address |
| `street` | `str` | Query, Optional | The street name of the recipient's address |
| `house_number` | `int` | Query, Optional | The house number of the recipient's address |
| `house_number_extension` | `str` | Query, Optional | The house number extension of the recipient's address |
| `delivery_date` | `str` | Query, Optional | The date of the earliest delivery date at the pickup location. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned. If not provided, the present day is used as a default |
| `opening_time` | `str` | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided. If no opening time is provided all locations will be returned regardless of their opening times. |
| `delivery_options` | [`List[LocationsDeliveryOptionEnum]`](../../doc/models/locations-delivery-option-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationsResponseMultiple`](../../doc/models/locations-response-multiple.md).

## Example Usage

```python
country_code = CountrycodeEnum.NL

postal_code = '2132WT'

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_number_extension = '-60'

delivery_date = '24-12-2022'

opening_time = '09:00:00'

result = locations_controller.get_pickup_locations_by_address(
    country_code,
    postal_code,
    city=city,
    street=street,
    house_number=house_number,
    house_number_extension=house_number_extension,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "GetLocationsResult": {
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
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Pickup Locations by Coordinates

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/nearest/geocode?Latitude=52.2864669620795&Longitude=4.68239055845954&CountryCode=NL&DeliveryDate=24-12-2022&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def get_pickup_locations_by_coordinates(self,
                                       latitude,
                                       longitude,
                                       country_code,
                                       delivery_date=None,
                                       opening_time=None,
                                       delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `float` | Query, Required | The latitude of the location |
| `longitude` | `float` | Query, Required | The longitude of the location |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | The coutry for which the coordinates are provided |
| `delivery_date` | `str` | Query, Optional | The date of the earliest delivery date. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned. |
| `opening_time` | `str` | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided. |
| `delivery_options` | [`List[LocationsDeliveryOptionEnum]`](../../doc/models/locations-delivery-option-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationsResponseMultiple`](../../doc/models/locations-response-multiple.md).

## Example Usage

```python
latitude = 52.2864669620795

longitude = 4.68239055845954

country_code = CountrycodeEnum.NL

delivery_date = '24-12-2022'

opening_time = '09:00:00'

result = locations_controller.get_pickup_locations_by_coordinates(
    latitude,
    longitude,
    country_code,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "GetLocationsResult": {
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
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Pickup Locations Within Area

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/area?LatitudeNorth=52.156439&LongitudeWest=5.015643&LatitudeSouth=52.017473&LongitudeEast=5.065254&CountryCode=NL&DeliveryDate=24-12-2023&OpeningTime=09%3A00%3A00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def get_pickup_locations_within_area(self,
                                    latitude_north,
                                    longitude_west,
                                    latitude_south,
                                    longitude_east,
                                    country_code,
                                    delivery_date=None,
                                    opening_time=None,
                                    delivery_options=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude_north` | `float` | Query, Required | The northmost coordinates of the area |
| `longitude_west` | `float` | Query, Required | The westmost coordinates of the area |
| `latitude_south` | `float` | Query, Required | The southmost coordinates of the area |
| `longitude_east` | `float` | Query, Required | The eastmost coordinates of the area |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | - |
| `delivery_date` | `str` | Query, Optional | The date of the earliest delivery date. Format:  dd-MM-yyyy. Note: this date cannot be in the past, otherwise an error is returned. |
| `opening_time` | `str` | Query, Optional | Opening time filter. Format: hh:mm:ss. This field will be used to filter out locations that are closed at the time provided. |
| `delivery_options` | [`List[LocationsDeliveryOptionEnum]`](../../doc/models/locations-delivery-option-enum.md) | Query, Optional | The pickup location types for which locations should be filtered. By default all location types are returned (PG = Retail points and parcel lockers). This can be used to filter on only parcel lockers (PA) or specifically exclude parcel lockers from the response (PG_EX). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationsResponseMultiple`](../../doc/models/locations-response-multiple.md).

## Example Usage

```python
latitude_north = 52.156439

longitude_west = 5.015643

latitude_south = 52.017473

longitude_east = 5.065254

country_code = CountrycodeEnum.NL

delivery_date = '24-12-2023'

opening_time = '09:00:00'

result = locations_controller.get_pickup_locations_within_area(
    latitude_north,
    longitude_west,
    latitude_south,
    longitude_east,
    country_code,
    delivery_date=delivery_date,
    opening_time=opening_time
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "GetLocationsResult": {
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
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Pickup Location

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/locations/lookup?LocationCode=216877" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def get_pickup_location(self,
                       location_code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `location_code` | `str` | Query, Required | LocationCode information |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`LocationResponseSingle`](../../doc/models/location-response-single.md).

## Example Usage

```python
location_code = '216877'

result = locations_controller.get_pickup_location(location_code)
print(result)
```

## Example Response *(as JSON)*

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

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

