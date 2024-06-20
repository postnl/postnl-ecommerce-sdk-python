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
| `postalcode` | `str` | Query, Required | - |
| `housenumber` | `str` | Query, Required | - |
| `housenumberaddition` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[PostalcodeCheckAddress]`](../../doc/models/postalcode-check-address.md).

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
| 400 | Bad request | [`PostalcodeCheckResponseInvalidException`](../../doc/models/postalcode-check-response-invalid-exception.md) |
| 401 | Invalid apikey | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 405 | Method not allowed | [`MethodNotAllowedOnlyGetException`](../../doc/models/method-not-allowed-only-get-exception.md) |
| 429 | Too many requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal server error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

