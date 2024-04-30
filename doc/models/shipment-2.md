
# Shipment 2

## Structure

`Shipment2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main_barcode` | [`str`](../../doc/models/string-enum.md) | Optional | The main barcode of the shipment |
| `barcode` | [`str`](../../doc/models/string-enum.md) | Optional | The barcode of the shipment |
| `shipment_amount` | [`str`](../../doc/models/string-enum.md) | Optional | The amount of parcels in the multi-collo shipment |
| `shipment_counter` | [`str`](../../doc/models/string-enum.md) | Optional | The sequence of this parcel in the multi-collo shipment |
| `customer` | [`Customer2`](../../doc/models/customer-2.md) | Optional | - |
| `product_code` | [`str`](../../doc/models/string-enum.md) | Optional | The product code of the shipment |
| `product_description` | [`str`](../../doc/models/string-enum.md) | Optional | The description of the product code |
| `reference` | [`str`](../../doc/models/string-enum.md) | Optional | The customer reference belonging to the shipment |
| `delivery_date` | [`str`](../../doc/models/string-enum.md) | Optional | The expected delivery date of the shipment |
| `dimension` | [`Dimension1`](../../doc/models/dimension-1.md) | Optional | - |
| `amount` | [`Amount1`](../../doc/models/amount-1.md) | Optional | The amounts belonging to the shipment |
| `address` | [`List[Address4]`](../../doc/models/address-4.md) | Optional | A list of addresses belonging to the shipment |
| `event` | [`List[Event]`](../../doc/models/event.md) | Optional | The events of the shipment. (see the [Event Codes](#tag/TandT-status-codes/Event-codes) for possible values. |
| `expectation` | [`Expectation`](../../doc/models/expectation.md) | Optional | The expected delivery timeframe |
| `product_options` | [`ProductOptions`](../../doc/models/product-options.md) | Optional | A list of product options. |
| `status` | [`Status`](../../doc/models/status.md) | Optional | The current status of the shipment (see the [Status codes](#tag/TandT-status-codes/Status-codes) for possible values. |
| `old_status` | [`List[OldStatus]`](../../doc/models/old-status.md) | Optional | A list of previous status codes (see the [Status codes](#tag/TandT-status-codes/Status-codes) for possible values. |

## Example (as JSON)

```json
{
  "MainBarcode": "3SDEVC6659149",
  "Barcode": "3SDEVC6659149",
  "ShipmentAmount": "2",
  "ShipmentCounter": "1",
  "ProductCode": "003085",
  "ProductDescription": "Standaard Zending",
  "Reference": "REF-1234567",
  "DeliveryDate": "2016-04-20",
  "Customer": {
    "CustomerCode": "CustomerCode8",
    "CustomerNumber": "CustomerNumber0",
    "Name": "Name8"
  }
}
```

