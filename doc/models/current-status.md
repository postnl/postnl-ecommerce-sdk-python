
# Current Status

The current status and old statuses of the shipment

## Structure

`CurrentStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipment` | [`List[Shipment11]`](../../doc/models/shipment-11.md) | Optional | - |

## Example (as JSON)

```json
{
  "Shipment": [
    {
      "MainBarcode": "MainBarcode4",
      "Barcode": "Barcode4",
      "ShipmentAmount": "ShipmentAmount0",
      "ShipmentCounter": "ShipmentCounter6",
      "Customer": {
        "CustomerCode": "CustomerCode8",
        "CustomerNumber": "CustomerNumber0",
        "Name": "Name8"
      }
    },
    {
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
  ]
}
```

