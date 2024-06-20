
# Confirming Response Error Exception

## Structure

`ConfirmingResponseErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_shipments` | [`List[ConfirmingResponseShipment]`](../../doc/models/confirming-response-shipment.md) | Optional | - |

## Example (as JSON)

```json
{
  "ResponseShipments": [
    {
      "Errors": [
        {
          "Code": "Code4",
          "Description": "Description2"
        },
        {
          "Code": "Code4",
          "Description": "Description2"
        }
      ],
      "Warnings": [
        {
          "Code": "Code4",
          "Description": "Description8"
        }
      ],
      "Barcode": "Barcode0"
    },
    {
      "Errors": [
        {
          "Code": "Code4",
          "Description": "Description2"
        },
        {
          "Code": "Code4",
          "Description": "Description2"
        }
      ],
      "Warnings": [
        {
          "Code": "Code4",
          "Description": "Description8"
        }
      ],
      "Barcode": "Barcode0"
    },
    {
      "Errors": [
        {
          "Code": "Code4",
          "Description": "Description2"
        },
        {
          "Code": "Code4",
          "Description": "Description2"
        }
      ],
      "Warnings": [
        {
          "Code": "Code4",
          "Description": "Description8"
        }
      ],
      "Barcode": "Barcode0"
    }
  ]
}
```

