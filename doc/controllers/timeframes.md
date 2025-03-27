# Timeframes

```python
timeframes_controller = client.timeframes
```

## Class Name

`TimeframesController`


# Retrieve Delivery Timeframes

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_1/calculate/timeframes?AllowSundaySorting=false&StartDate=30-06-2022&EndDate=02-07-2022&CountryCode=NL&PostalCode=2132WT&HouseNumber=42&HouseNrExt=A&City=Hoofddorp&Street=Siriusdreef&Options=Daytime%2CEvening" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def retrieve_delivery_timeframes(self,
                                allow_sunday_sorting,
                                start_date,
                                end_date,
                                country_code,
                                postal_code,
                                house_number,
                                options,
                                house_nr_ext=None,
                                city=None,
                                street=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_sunday_sorting` | `bool` | Query, Required | Whether or not the requesting party allows for Sunday sorting (which leads to delivery on Monday). |
| `start_date` | `str` | Query, Required | Date of the beginning of the timeframe. Format: dd-MM-yyyy<br>**Constraints**: *Pattern*: `^([0-3]\d-[0-1]\d-[1-2]\d{3})$` |
| `end_date` | `str` | Query, Required | Date of the enddate of the timeframe. Format:dd-MM-yyyy. Enddate may not be before StartDate.<br>**Constraints**: *Pattern*: `^([0-3]\d-[0-1]\d-[1-2]\d{3})$` |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | The ISO2 country code of the delivery address |
| `postal_code` | `str` | Query, Required | Zipcode of the delivery address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `house_number` | `int` | Query, Required | The house number of the delivery address |
| `options` | [`List[TimeframeOptionsEnum]`](../../doc/models/timeframe-options-enum.md) | Query, Required | The delivery options for which expected timeframes should be calculated. At least one delivery option must be specified. Multiple values should be comma-separated. |
| `house_nr_ext` | `str` | Query, Optional | House number extension of the delivery address |
| `city` | `str` | Query, Optional | City of the delivery address |
| `street` | `str` | Query, Optional | The street name of the delivery address |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TimeframeResponse`](../../doc/models/timeframe-response.md).

## Example Usage

```python
allow_sunday_sorting = False

start_date = '30-06-2022'

end_date = '02-07-2022'

country_code = CountrycodeEnum.NL

postal_code = '2132WT'

house_number = 42

options = [
    TimeframeOptionsEnum.DAYTIME,
    TimeframeOptionsEnum.EVENING,
    TimeframeOptionsEnum.SUNDAY
]

house_nr_ext = 'A'

city = 'Hoofddorp'

street = 'Siriusdreef'

result = timeframes_controller.retrieve_delivery_timeframes(
    allow_sunday_sorting,
    start_date,
    end_date,
    country_code,
    postal_code,
    house_number,
    options,
    house_nr_ext=house_nr_ext,
    city=city,
    street=street
)
```

## Example Response *(as JSON)*

```json
{
  "Timeframes": {
    "Timeframe": [
      {
        "Date": "02-07-2022",
        "Timeframes": {
          "TimeframeTimeframe": [
            {
              "From": "12:30:00",
              "Options": {
                "string": "Daytime"
              },
              "To": "14:30:00",
              "Sustainability": {
                "Code": "02",
                "Description": "Sustainable option"
              }
            }
          ]
        }
      }
    ]
  },
  "ReasonNoTimeframes": {
    "ReasonNoTimeframe": [
      {
        "Code": "1",
        "Date": "02-07-2022",
        "Description": "Delivery date not allowed",
        "Options": {
          "string": "Evening"
        },
        "Sustainability": {
          "Code": "02",
          "Description": "Sustainable option"
        }
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

