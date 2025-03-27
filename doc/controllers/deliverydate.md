# Deliverydate

```python
deliverydate_controller = client.deliverydate
```

## Class Name

`DeliverydateController`

## Methods

* [Calculate Delivery Date](../../doc/controllers/deliverydate.md#calculate-delivery-date)
* [Calculate Shipping Date](../../doc/controllers/deliverydate.md#calculate-shipping-date)


# Calculate Delivery Date

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/delivery?ShippingDate=29-05-2022+14%3A00%3A00&amp;ShippingDuration=1&amp;CutOffTime=17%3A00%3A00&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def calculate_delivery_date(self,
                           shipping_date,
                           shipping_duration,
                           cut_off_time,
                           postal_code,
                           country_code,
                           options,
                           origin_country_code='NL',
                           city=None,
                           street=None,
                           house_number=None,
                           house_nr_ext=None,
                           cut_off_time_monday=None,
                           available_monday=None,
                           cut_off_time_tuesday=None,
                           available_tuesday=None,
                           cut_off_time_wednesday=None,
                           available_wednesday=None,
                           cut_off_time_thursday=None,
                           available_thursday=None,
                           cut_off_time_friday=None,
                           available_friday=None,
                           cut_off_time_saturday=None,
                           available_saturday=None,
                           cut_off_time_sunday=None,
                           available_sunday=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipping_date` | `str` | Query, Required | Date/time of preparing the shipment for sending. Format: dd-MM-yyyy hh:mm:ss<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}\s[0-2]\d:[0-5]\d:[0-5]\d$` |
| `shipping_duration` | `int` | Query, Required | The duration it takes for the shipment to be delivered to PostNL in days. A value of 1 means that the parcel will be delivered to PostNL on the same day as the date specified in ShippingDate. A value of 2 means the parcel will arrive at PostNL a day later etc. |
| `cut_off_time` | `str` | Query, Required | Default cutoff time<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `postal_code` | `str` | Query, Required | Zipcode of the destination address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | The ISO2 destination country code |
| `options` | [`List[DeliverydateOptionEnum]`](../../doc/models/deliverydate-option-enum.md) | Query, Required | The delivery options that you want to take into account when calculating the expected delivery date |
| `origin_country_code` | [`OriginCountryCodeEnum`](../../doc/models/origin-country-code-enum.md) | Query, Optional | The ISO2 origin country code<br>**Default**: `'NL'` |
| `city` | `str` | Query, Optional | City of the destination address |
| `street` | `str` | Query, Optional | The street name of the destination address. |
| `house_number` | `int` | Query, Optional | The house number of the destination address |
| `house_nr_ext` | `str` | Query, Optional | House number extension of the delivery address |
| `cut_off_time_monday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for mondays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_monday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on mondays |
| `cut_off_time_tuesday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for tuesdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_tuesday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on tuesdays |
| `cut_off_time_wednesday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for wednesdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_wednesday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on wednesdays |
| `cut_off_time_thursday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for thursdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_thursday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on thursdays |
| `cut_off_time_friday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for fridays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_friday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on fridays |
| `cut_off_time_saturday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for saturdays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_saturday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on saturdays |
| `cut_off_time_sunday` | `str` | Query, Optional | Overrides default cutoff time specified in the CutOffTime parameter for sundays specifically<br>**Constraints**: *Pattern*: `^[0-2]\d:[0-5]\d:[0-5]\d$` |
| `available_sunday` | `bool` | Query, Optional | Specifies if you are available to ship to PostNL on sundays |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeliverydateDeliveryResponse`](../../doc/models/deliverydate-delivery-response.md).

## Example Usage

```python
shipping_date = '29-05-2022 14:00:00'

shipping_duration = 1

cut_off_time = '17:00:00'

postal_code = '2132WT'

country_code = CountrycodeEnum.NL

options = [
    DeliverydateOptionEnum.SUNDAY,
    DeliverydateOptionEnum.TODAY,
    DeliverydateOptionEnum.AFTERNOON
]

origin_country_code = OriginCountryCodeEnum.NL

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_nr_ext = 'A'

result = deliverydate_controller.calculate_delivery_date(
    shipping_date,
    shipping_duration,
    cut_off_time,
    postal_code,
    country_code,
    options,
    origin_country_code=origin_country_code,
    city=city,
    street=street,
    house_number=house_number,
    house_nr_ext=house_nr_ext
)
```

## Example Response *(as JSON)*

```json
{
  "DeliveryDate": "30-05-2022",
  "Options": {
    "string": "Daytime"
  },
  "Sustainability": {
    "Code": "02",
    "Description": "Sustainable option"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Calculate Shipping Date

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2_2/calculate/date/shipping?DeliveryDate=30-05-2022&amp;ShippingDuration=1&amp;PostalCode=2132WT&amp;CountryCode=NL&amp;City=Hoofddorp&amp;Street=Siriusdreef&amp;HouseNumber=42&amp;HouseNrExt=A" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \

```

```python
def calculate_shipping_date(self,
                           delivery_date,
                           shipping_duration,
                           postal_code,
                           country_code,
                           origin_country_code='NL',
                           city=None,
                           street=None,
                           house_number=None,
                           house_nr_ext=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_date` | `str` | Query, Required | Date of the expected delivery (to the final destination) of the shipment.<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-[1-2]\d{3}$` |
| `shipping_duration` | `int` | Query, Required | The duration it takes for the shipment to be delivered to PostNL in days. A value of 1 means that the parcel will be delivered to PostNL on the same day as the date specified in ShippingDate. A value of 2 means the parcel will arrive at PostNL a day later etc. |
| `postal_code` | `str` | Query, Required | Zipcode of the address<br>**Constraints**: *Pattern*: `^[0-9]{4}([A-Z]{2})?$` |
| `country_code` | [`CountrycodeEnum`](../../doc/models/countrycode-enum.md) | Query, Required | The ISO2 destination country code |
| `origin_country_code` | [`OriginCountryCodeEnum`](../../doc/models/origin-country-code-enum.md) | Query, Optional | The ISO2 country code of the origin country<br>**Default**: `'NL'` |
| `city` | `str` | Query, Optional | City of the destination address |
| `street` | `str` | Query, Optional | The street name of the destination address |
| `house_number` | `int` | Query, Optional | The house number of the destination address |
| `house_nr_ext` | `str` | Query, Optional | House number extension of the destination address |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeliverydateShippingResponse`](../../doc/models/deliverydate-shipping-response.md).

## Example Usage

```python
delivery_date = '30-05-2022'

shipping_duration = 1

postal_code = '2132WT'

country_code = CountrycodeEnum.NL

origin_country_code = OriginCountryCodeEnum.NL

city = 'Hoofddorp'

street = 'Siriusdreef'

house_number = 42

house_nr_ext = 'A'

result = deliverydate_controller.calculate_shipping_date(
    delivery_date,
    shipping_duration,
    postal_code,
    country_code,
    origin_country_code=origin_country_code,
    city=city,
    street=street,
    house_number=house_number,
    house_nr_ext=house_nr_ext
)
```

## Example Response *(as JSON)*

```json
{
  "SentDate": "29-06-2022"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

