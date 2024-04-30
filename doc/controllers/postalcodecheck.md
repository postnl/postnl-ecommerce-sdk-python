# Postalcodecheck

```python
postalcodecheck_controller = client.postalcodecheck
```

## Class Name

`PostalcodecheckController`


# Checkout Postalcode Check

Please note that this API is not available on the sandbox environment.

Request example:

```
curl -X GET "https://api.postnl.nl/shipment/checkout/v1/postalcodecheck?postalcode=3571ZZ&amp;housenumber=74&amp;housenumberaddition=bis" \
 -H "Accept: application/json" \
 -H "apikey: APIKEY-HERE" 
```

```python
def checkout_postalcode_check(self,
                             postalcode,
                             housenumber,
                             housenumberaddition=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `postalcode` | [`str`](../../doc/models/string-enum.md) | Query, Required | - |
| `housenumber` | [`str`](../../doc/models/string-enum.md) | Query, Required | - |
| `housenumberaddition` | [`str`](../../doc/models/string-enum.md) | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[CpcResponse]`](../../doc/models/cpc-response.md).

## Example Usage

```python
postalcode = '3571ZZ'

housenumber = '74'

housenumberaddition = 'bis'

result = postalcode_check_controller.checkout_postalcode_check(
    postalcode,
    housenumber,
    housenumberaddition=housenumberaddition
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "city": "UTRECHT",
    "postalCode": "3571ZZ",
    "streetName": "Molengraaffplantsoen",
    "houseNumber": 74,
    "houseNumberAddition": "bis",
    "formattedAddress": [
      "Molengraaffplantsoen 74 bis",
      "3571ZZ UTRECHT"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`BarcodeResponseInvalidException`](../../doc/models/barcode-response-invalid-exception.md) |
| 401 | Invalid apikey | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 405 | Method not allowed | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 429 | Too many requests | [`BarcodeMethodNotAllowedException`](../../doc/models/barcode-method-not-allowed-exception.md) |
| 500 | Internal server error | [`BarcodeResponseErrorException`](../../doc/models/barcode-response-error-exception.md) |

