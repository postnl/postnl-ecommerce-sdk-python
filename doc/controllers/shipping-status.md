# Shipping Status

```python
shipping_status_controller = client.shipping_status
```

## Class Name

`ShippingStatusController`

## Methods

* [Get Status by Barcode](../../doc/controllers/shipping-status.md#get-status-by-barcode)
* [Get Status by Reference](../../doc/controllers/shipping-status.md#get-status-by-reference)
* [Get Shipment Signature](../../doc/controllers/shipping-status.md#get-shipment-signature)
* [Get Updated Status by Customer Number](../../doc/controllers/shipping-status.md#get-updated-status-by-customer-number)


# Get Status by Barcode

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/barcode/3SDEVC172649258" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def get_status_by_barcode(self,
                         barcode,
                         detail=False,
                         language=None,
                         max_days=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | `str` | Template, Required | Barcode of the shipment. This is a unique value. |
| `detail` | `bool` | Query, Optional | Option to include old statuses in the response |
| `language` | [`LanguageEnum`](../../doc/models/language-enum.md) | Query, Optional | Language of the returned shipment and status descriptions (default is Dutch). |
| `max_days` | `str` | Query, Optional | Limit the number of days that will be searched (decrease this amount for better performance). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ShippingstatusResponse`](../../doc/models/shippingstatus-response.md).

## Example Usage

```python
barcode = '3SDEVC172649258'

detail = False

language = LanguageEnum.NL

max_days = '14'

result = shipping_status_controller.get_status_by_barcode(
    barcode,
    detail=detail,
    language=language,
    max_days=max_days
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "CurrentStatus": {
    "Shipment": {
      "MainBarcode": "3SDEVC288882229",
      "Barcode": "3SDEVC288882229",
      "ShipmentAmount": "1",
      "ShipmentCounter": "1",
      "Customer": {
        "CustomerCode": "DEVC",
        "CustomerNumber": "11223344",
        "Name": "Testaccount API PNP"
      },
      "ProductCode": "002285",
      "ProductDescription": "Parcels, domestic &lt;= 10 kg",
      "Reference": "202213331635095807",
      "DeliveryDate": "2022-11-08",
      "Dimension": {
        "Height": "125",
        "Length": "250",
        "Volume": "6250",
        "Weight": "180",
        "Width": "200"
      },
      "Address": [
        {
          "AddressType": "01",
          "Building": "{}",
          "City": "Utrecht",
          "CompanyName": "{}",
          "CountryCode": "NL",
          "DepartmentName": "{}",
          "District": "{}",
          "FirstName": "Peter",
          "Floor": "{}",
          "HouseNumber": "74",
          "HouseNumberSuffix": "{}",
          "LastName": "de Ruiter",
          "Region": "{}",
          "Remark": "{}",
          "Street": "Molengraaffplantsoen",
          "Zipcode": "3571ZZ"
        },
        {
          "AddressType": "02",
          "Building": "{}",
          "City": "Hoofddorp",
          "CompanyName": "PostNL Pakketten",
          "CountryCode": "NL",
          "DepartmentName": "{}",
          "District": "{}",
          "FirstName": "{}",
          "Floor": "{}",
          "HouseNumber": "42",
          "HouseNumberSuffix": "-60",
          "LastName": "{}",
          "Region": "{}",
          "Remark": "{}",
          "Street": "Siriusdreef",
          "Zipcode": "2132WT"
        }
      ],
      "ProductOptions": [
        {
          "OptionCode": "6",
          "CharacteristicCode": "118"
        }
      ],
      "Status": {
        "TimeStamp": "08-11-2022 10:13:20",
        "StatusCode": "7",
        "StatusDescription": "Shipment out for delivery",
        "PhaseCode": "3",
        "PhaseDescription": "Distribution"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetException`](../../doc/models/method-not-allowed-only-get-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Status by Reference

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/reference?detail=true&language=NL&customerCode={{CustomerCode}}&customerNumber={{CustomerNumber}}&reference=REF98173245876329" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def get_status_by_reference(self,
                           customer_code,
                           customer_number,
                           reference_id,
                           detail=False,
                           language=None,
                           max_days=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_code` | `str` | Query, Required | Customer code as known at PostNL Pakketten |
| `customer_number` | `str` | Query, Required | Customer number as known at PostNL Pakketten |
| `reference_id` | `str` | Template, Required | The customer reference belonging to the shipment |
| `detail` | `bool` | Query, Optional | Option to include old statuses in the response |
| `language` | [`LanguageEnum`](../../doc/models/language-enum.md) | Query, Optional | Language of the returned shipment and status descriptions (default is Dutch). |
| `max_days` | `str` | Query, Optional | Limit the number of days that will be searched (decrease this amount for better performance). By default this is 90 days in the past. |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ShippingstatusResponse`](../../doc/models/shippingstatus-response.md).

## Example Usage

```python
customer_code = 'DEVC'

customer_number = '11223344'

reference_id = 'REF-12345'

detail = False

language = LanguageEnum.NL

max_days = '14'

result = shipping_status_controller.get_status_by_reference(
    customer_code,
    customer_number,
    reference_id,
    detail=detail,
    language=language,
    max_days=max_days
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "CurrentStatus": {
    "Shipment": {
      "MainBarcode": "3SDEVC288882229",
      "Barcode": "3SDEVC288882229",
      "ShipmentAmount": "1",
      "ShipmentCounter": "1",
      "Customer": {
        "CustomerCode": "DEVC",
        "CustomerNumber": "11223344",
        "Name": "Testaccount API PNP"
      },
      "ProductCode": "002285",
      "ProductDescription": "Parcels, domestic &lt;= 10 kg",
      "Reference": "202213331635095807",
      "DeliveryDate": "2022-11-08",
      "Dimension": {
        "Height": "125",
        "Length": "250",
        "Volume": "6250",
        "Weight": "180",
        "Width": "200"
      },
      "Address": [
        {
          "AddressType": "01",
          "Building": "{}",
          "City": "Utrecht",
          "CompanyName": "{}",
          "CountryCode": "NL",
          "DepartmentName": "{}",
          "District": "{}",
          "FirstName": "Peter",
          "Floor": "{}",
          "HouseNumber": "74",
          "HouseNumberSuffix": "{}",
          "LastName": "de Ruiter",
          "Region": "{}",
          "Remark": "{}",
          "Street": "Molengraaffplantsoen",
          "Zipcode": "3571ZZ"
        },
        {
          "AddressType": "02",
          "Building": "{}",
          "City": "Hoofddorp",
          "CompanyName": "PostNL Pakketten",
          "CountryCode": "NL",
          "DepartmentName": "{}",
          "District": "{}",
          "FirstName": "{}",
          "Floor": "{}",
          "HouseNumber": "42",
          "HouseNumberSuffix": "-60",
          "LastName": "{}",
          "Region": "{}",
          "Remark": "{}",
          "Street": "Siriusdreef",
          "Zipcode": "2132WT"
        }
      ],
      "ProductOptions": [
        {
          "OptionCode": "6",
          "CharacteristicCode": "118"
        }
      ],
      "Status": {
        "TimeStamp": "08-11-2022 10:13:20",
        "StatusCode": "7",
        "StatusDescription": "Shipment out for delivery",
        "PhaseCode": "3",
        "PhaseDescription": "Distribution"
      }
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetException`](../../doc/models/method-not-allowed-only-get-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Shipment Signature

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/signature/3SDEVC172649258" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def get_shipment_signature(self,
                          barcode)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | `str` | Template, Required | Barcode of the shipment |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ShippingstatusResponseSignature`](../../doc/models/shippingstatus-response-signature.md).

## Example Usage

```python
barcode = '3SDEVC172649258'

result = shipping_status_controller.get_shipment_signature(barcode)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "Signature": {
    "Barcode": "3SDEVC317858754",
    "SignatureDate": "2022-11-07T19:28:16",
    "SignatureImage": "iVBORw0KGgoAAAANSUhEUgAAAogAAAGTCAYAAACrs[TRUNCATED]"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetException`](../../doc/models/method-not-allowed-only-get-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Updated Status by Customer Number

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v2/status/11223344/updatedshipments?period=2022-12-25T10:00:00&amp;period=2022-12-25T10:12:00" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" \
```

```python
def get_updated_status_by_customer_number(self,
                                         customernumber,
                                         period=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customernumber` | `str` | Template, Required | Your customer number |
| `period` | `List[str]` | Query, Optional | Optional array which defines a specific period in which to return updated shipments. For optimal results, schedule calls at a frequency between 5-15 minutes and align the requested period accordingly to ensure complete coverage of past updates. Shorter periods yield improved response times. The API accommodates a maximum requested period of 2 hours, granting access to shipment data up to 48 hours in the past. Please use the following format: YYYY-MM-DDTHH:MM:SS and repeat this variable to define the period (e.g. /updatedshipments?period=2022-11-07T12:00:00.000&period=2022-11-07T12:05:00.000). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[ShippingstatusResponseUpdatedShipment]`](../../doc/models/shippingstatus-response-updated-shipment.md).

## Example Usage

```python
customernumber = '11223344'

period = [
    '2022-11-07T12:00:00.000',
    '2022-11-07T12:05:00.000'
]

result = shipping_status_controller.get_updated_status_by_customer_number(
    customernumber,
    period=period
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "Barcode": "3SDEVC2260332157",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T02:17:49",
      "StatusCode": "5",
      "StatusDescription": "Zending gesorteerd",
      "PhaseCode": "2",
      "PhaseDescription": "Sortering"
    }
  },
  {
    "Barcode": "3SDEVC775533088",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T04:15:00",
      "StatusCode": "13",
      "StatusDescription": "Voorgemeld: nog niet aangenomen",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  },
  {
    "Barcode": "3SDEVC563372025",
    "CreationDate": "2022-11-07T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T04:15:00",
      "StatusCode": "13",
      "StatusDescription": "Voorgemeld: nog niet aangenomen",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  },
  {
    "Barcode": "3SDEVC336510881",
    "CreationDate": "2022-11-08T00:00:00",
    "CustomerNumber": "11223344",
    "CustomerCode": "DEVC",
    "Status": {
      "Timestamp": "2022-11-08T01:01:28",
      "StatusCode": "1",
      "StatusDescription": "Zending voorgemeld",
      "PhaseCode": "1",
      "PhaseDescription": "Collectie"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetException`](../../doc/models/method-not-allowed-only-get-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

