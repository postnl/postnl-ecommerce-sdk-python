
# Shippingstatus Response Updated Shipment

## Structure

`ShippingstatusResponseUpdatedShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | `str` | Optional | The barcode belonging to the status update |
| `creation_date` | `str` | Optional | The date of the update |
| `customer_number` | `str` | Optional | The customer number |
| `customer_code` | `str` | Optional | The customer code |
| `status` | [`UpdatedShipmentStatus`](../../doc/models/updated-shipment-status.md) | Optional | The status update. See [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values. |

## Example (as JSON)

```json
{
  "Barcode": "3SDEVC5672025",
  "CreationDate": "11/07/2022 00:00:00",
  "CustomerNumber": "11223344",
  "CustomerCode": "DEVC",
  "Status": {
    "Timestamp": "Timestamp8",
    "StatusCode": "StatusCode8",
    "StatusDescription": "StatusDescription0",
    "PhaseCode": "PhaseCode2",
    "PhaseDescription": "PhaseDescription8"
  }
}
```

