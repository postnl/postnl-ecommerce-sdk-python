# Labelling

```python
labelling_controller = client.labelling
```

## Class Name

`LabellingController`


# Generate Label

```python
def generate_label(self,
                  body,
                  confirm=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LabellingRequest`](../../doc/models/labelling-request.md) | Body, Required | - |
| `confirm` | `bool` | Query, Optional | With the Confirm boolean in the request, you can determine if you want to confirm the shipment in the same call or not. If the Boolean variable is true the shipment will be preannounced. If this is set to false, then an additional Confirming API request needs to be made.<br>**Default**: `True` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LabellingResponse`](../../doc/models/labelling-response.md).

## Example Usage

```python
body = LabellingRequest(
    customer=LabellingCustomer(
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
    message=LabellingCustomerMessage(
        message_id='1',
        message_time_stamp='08-09-2022 12:00:00',
        printertype='GraphicFile|PDF'
    ),
    shipments=[
        LabellingCustomerShipment(
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

result = labelling_controller.generate_label(body)
```

## Example Response *(as JSON)*

```json
{
  "MergedLabels": [],
  "ResponseShipments": [
    {
      "Barcode": "3SDEVC272730803",
      "Errors": [],
      "Warnings": [],
      "Labels": [
        {
          "Content": "JVBERi0xLjMKJeLjz9MKNSAwIG9iago8PAovQ29udGVudHMg[TRUNCATED]",
          "Labeltype": "Label",
          "OutputType": "PDF"
        }
      ],
      "ProductCodeDelivery": "3085"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error payload | [`LabellingResponseInvalidException`](../../doc/models/labelling-response-invalid-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyPostException`](../../doc/models/method-not-allowed-only-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

