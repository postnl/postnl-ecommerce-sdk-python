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

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CheckoutResponse`](../../doc/models/checkout-response.md).

## Example Usage

```python
body = CheckoutRequest(
    order_date='24-02-2021 12:00:00',
    cut_off_times=[
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=Type1Enum.REGULAR,
            time='20:00:00'
        ),
        CutOffTime(
            day=DayEnum.ENUM_00,
            available=True,
            mtype=Type1Enum.TODAY,
            time='12:00:00'
        )
    ],
    options=[
        OptionEnum.DAYTIME,
        OptionEnum.EVENING,
        OptionEnum.TODAY,
        OptionEnum.SUNDAY,
        OptionEnum.PICKUP
    ],
    locations=2,
    days=3,
    addresses=[
        Address(
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
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`CheckoutResponseInvalidException`](../../doc/models/checkout-response-invalid-exception.md) |
| 401 | Invalid apikey | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 405 | Method not allowed | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 429 | Too many requests | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 500 | Internal server error | [`BarcodeResponseErrorException`](../../doc/models/barcode-response-error-exception.md) |

