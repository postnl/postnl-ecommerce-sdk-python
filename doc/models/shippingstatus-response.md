
# Shippingstatus Response

## Structure

`ShippingstatusResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complete_status` | [`CompleteStatus`](../../doc/models/complete-status.md) | Optional | The current status and old statuses of the shipment |
| `current_status` | [`CurrentStatus`](../../doc/models/current-status.md) | Optional | The current status and old statuses of the shipment |
| `warnings` | [`List[ShippingstatusWarning]`](../../doc/models/shippingstatus-warning.md) | Optional | Possible warnings (see [Error Codes](https://developer.postnl.nl/docs/#/http/reference-data/error-codes) for possible values) |

## Example (as JSON)

```json
{
  "CompleteStatus": {
    "Shipment": {
      "MainBarcode": "MainBarcode4",
      "Barcode": "Barcode4",
      "ShipmentAmount": "ShipmentAmount0",
      "ShipmentCounter": "ShipmentCounter6",
      "Customer": {
        "CustomerCode": "CustomerCode8",
        "CustomerNumber": "CustomerNumber0",
        "Name": "Name8"
      }
    }
  },
  "CurrentStatus": {
    "Shipment": {
      "MainBarcode": "MainBarcode4",
      "Barcode": "Barcode4",
      "ShipmentAmount": "ShipmentAmount0",
      "ShipmentCounter": "ShipmentCounter6",
      "Customer": {
        "CustomerCode": "CustomerCode8",
        "CustomerNumber": "CustomerNumber0",
        "Name": "Name8"
      }
    }
  },
  "Warnings": [
    {
      "Message": "Message0",
      "Code": "Code4"
    },
    {
      "Message": "Message0",
      "Code": "Code4"
    },
    {
      "Message": "Message0",
      "Code": "Code4"
    }
  ]
}
```

