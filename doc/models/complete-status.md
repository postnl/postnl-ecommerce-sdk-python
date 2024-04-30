
# Complete Status

The current status and old statuses of the shipment

## Structure

`CompleteStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shipment` | [`List[Shipment2]`](../../doc/models/shipment-2.md) | Optional | - |

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
    }
  ]
}
```

