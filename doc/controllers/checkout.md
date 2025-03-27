# Checkout

```python
checkout_controller = client.checkout
```

## Class Name

`CheckoutController`


# Checkout

```python
def checkout(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CheckoutRequest`](../../doc/models/checkout-request.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CheckoutResponse`](../../doc/models/checkout-response.md).

## Example Usage

```python
body = CheckoutRequest(
    order_date='24-02-2021 12:00:00',
    cut_off_times=[
        CheckoutCutOffTime(
            day=CheckoutCutOffDayEnum.ENUM_00,
            available=True,
            mtype=CheckoutCutOffTypeEnum.REGULAR,
            time='20:00:00'
        ),
        CheckoutCutOffTime(
            day=CheckoutCutOffDayEnum.ENUM_00,
            available=True,
            mtype=CheckoutCutOffTypeEnum.TODAY,
            time='12:00:00'
        )
    ],
    options=[
        CheckoutOptionEnum.DAYTIME,
        CheckoutOptionEnum.EVENING,
        CheckoutOptionEnum.TODAY,
        CheckoutOptionEnum.SUNDAY,
        CheckoutOptionEnum.PICKUP
    ],
    locations=2,
    days=3,
    addresses=[
        CheckoutAddress(
            address_type=AddressTypeEnum.ENUM_01,
            house_nr=74,
            zipcode='3571ZZ',
            countrycode=CountrycodeEnum.NL,
            street='Molengraaffplantsoen',
            city='Utrecht'
        )
    ],
    shipping_duration=1,
    holiday_sorting=True
)

result = checkout_controller.checkout(body)
```

## Example Response *(as JSON)*

```json
{
  "DeliveryOptions": [
    {
      "DeliveryDate": "09-07-2019",
      "Timeframe": [
        {
          "From": "18:00:00",
          "To": "22:30:00",
          "Options": [
            "Daytime"
          ],
          "ShippingDate": "08-07-2019",
          "Sustainability": {
            "Code": "02",
            "Description": "Sustainable option"
          }
        }
      ]
    }
  ],
  "PickupOptions": [
    {
      "PickupDate": "09-07-2019",
      "ShippingDate": "08-07-2019",
      "Option": "Pickup",
      "Locations": [
        {
          "Address": {
            "Street": "Siriusdreef",
            "Zipcode": "2132WT",
            "HouseNr": 42,
            "HouseNrExt": "-60",
            "Countrycode": "NL",
            "CompanyName": "Pickup company BV"
          },
          "PickupTime": "15:00",
          "OpeningHours": {
            "Monday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Tuesday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Wednesday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Thursday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Friday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Saturday": {
              "From": "08:30:00",
              "To": "22:30:00"
            },
            "Sunday": {
              "From": "08:30:00",
              "To": "22:30:00"
            }
          },
          "Distance": 234,
          "LocationCode": "8101163043",
          "PartnerID": "PNPNL-01",
          "Sustainability": {
            "Code": "02",
            "Description": "Sustainable option"
          }
        }
      ]
    }
  ],
  "Warnings": [
    {
      "DeliveryDate": "07-07-2019",
      "Code": "5034",
      "Description": "No delivery option found on date",
      "Options": "Daytime"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`InvalidRequestException`](../../doc/models/invalid-request-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyPostException`](../../doc/models/method-not-allowed-only-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

