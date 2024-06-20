# Confirming

```python
confirming_controller = client.confirming
```

## Class Name

`ConfirmingController`


# Confirm Shipment

```python
def confirm_shipment(self,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConfirmingRequest`](../../doc/models/confirming-request.md) | Body, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ConfirmingResponse`](../../doc/models/confirming-response.md).

## Example Usage

```python
body = ConfirmingRequest(
    customer=Customer(
        customer_code='DEVC',
        customer_number='11223344',
        address=CustomerAddress(
            address_type='02',
            city='Den Haag',
            countrycode='NL',
            company_name='PostNL',
            house_nr='3',
            street='Waldorpstraat',
            zipcode='2521CA'
        ),
        collection_location='123456',
        contact_person='Janssen',
        email='email@company.com',
        name='Janssen'
    ),
    message=ConfirmingMessage(
        message_id='1',
        message_time_stamp='08-09-2022 12:00:00'
    ),
    shipments=[
        ConfirmingShipment(
            addresses=[
                Address(
                    address_type='01',
                    countrycode='NL',
                    city='Utrecht',
                    first_name='Peter',
                    house_nr='9',
                    house_nr_ext='a bis',
                    name='de Ruiter',
                    street='Bilderdijkstraat',
                    zipcode='3532VA'
                )
            ],
            barcode='3SDEVC748859096',
            dimension=Dimension(
                weight=2000
            ),
            product_code_delivery='3085',
            contacts=[
                Contact(
                    contact_type='01',
                    email='receiver@email.com',
                    sms_nr='+31612345678',
                    tel_nr='+31301234567'
                )
            ]
        )
    ]
)

result = confirming_controller.confirm_shipment(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "ResponseShipments": [
    {
      "Errors": [],
      "Warnings": [
        {
          "Code": "1280103",
          "Description": "Address is unknown"
        }
      ],
      "Barcode": "3SDEVC281677095"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error payload | [`ConfirmingResponseErrorException`](../../doc/models/confirming-response-error-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

