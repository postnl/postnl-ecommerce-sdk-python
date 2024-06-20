# Barcode

```python
barcode_controller = client.barcode
```

## Class Name

`BarcodeController`


# Generate Barcode

Request example:

```
curl -X GET "https://api-sandbox.postnl.nl/shipment/v1_1/barcode?CustomerCode=DEVC&amp;CustomerNumber=11223344&amp;Type=3S&amp;Serie=000000000-999999999&amp" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def generate_barcode(self,
                    customer_code,
                    customer_number,
                    mtype,
                    serie=None,
                    range=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_code` | `str` | Query, Required | The customer code for which you want a barcode to be generated |
| `customer_number` | `str` | Query, Required | The customer code for which you want a barcode to be generated |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Query, Required | The barcode type that you want to be generated |
| `serie` | `str` | Query, Optional | Barcode serie in the format '###000000-###000000', for example 100000-20000. The range must consist of a minimal difference of 100.000. It is allowed to add extra leading zeros at the beginning of the serie. See [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/send-track/barcode/guidelines) for more information. |
| `range` | `str` | Query, Optional | Only used for International Mail and Packet products (PEPS) shipments (with type LA, RI, UE). Identifying the issuing postal administration's country (NL in this case). |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`BarcodeResponse`](../../doc/models/barcode-response.md).

## Example Usage

```python
customer_code = 'DEVC'

customer_number = '11223344'

mtype = TypeEnum.ENUM_3S

serie = '100000000'

result = barcode_controller.generate_barcode(
    customer_code,
    customer_number,
    mtype,
    serie=serie
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "Barcode": "3SDEVC903942795"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid request | [`BarcodeResponseInvalidException`](../../doc/models/barcode-response-invalid-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetPostException`](../../doc/models/method-not-allowed-only-get-post-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

