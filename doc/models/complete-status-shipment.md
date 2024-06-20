
# Complete Status Shipment

## Structure

`CompleteStatusShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `main_barcode` | `str` | Optional | The main barcode of the shipment |
| `barcode` | `str` | Optional | The barcode of the shipment |
| `shipment_amount` | `str` | Optional | The amount of parcels in the multi-collo shipment |
| `shipment_counter` | `str` | Optional | The sequence of this parcel in the multi-collo shipment |
| `customer` | [`ShippingstatusCustomer`](../../doc/models/shippingstatus-customer.md) | Optional | - |
| `product_code` | `str` | Optional | The product code of the shipment |
| `product_description` | `str` | Optional | The description of the product code |
| `reference` | `str` | Optional | The customer reference belonging to the shipment |
| `delivery_date` | `str` | Optional | The expected delivery date of the shipment |
| `dimension` | [`ShippingstatusDimension`](../../doc/models/shippingstatus-dimension.md) | Optional | - |
| `amount` | [`ShippingstatusAmount`](../../doc/models/shippingstatus-amount.md) | Optional | The amounts belonging to the shipment |
| `address` | [`List[ShippingstatusAddress]`](../../doc/models/shippingstatus-address.md) | Optional | A list of addresses belonging to the shipment |
| `event` | [`List[Event]`](../../doc/models/event.md) | Optional | The events of the shipment. (see the [Event Codes](https://developer.postnl.nl/docs/#/http/reference-data/t-t-status-codes/event-codes) for possible values. |
| `expectation` | [`Expectation`](../../doc/models/expectation.md) | Optional | The expected delivery timeframe |
| `product_options` | [`List[ShippingstatusProductOptions]`](../../doc/models/shippingstatus-product-options.md) | Optional | A list of product options. |
| `status` | [`Status`](../../doc/models/status.md) | Optional | The current status of the shipment (see the [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/t-t-status-codes/event-codes) for possible values. |
| `old_status` | [`List[OldStatus]`](../../doc/models/old-status.md) | Optional | A list of previous status codes (see the [Status codes](https://developer.postnl.nl/docs/#/http/reference-data/t-t-status-codes/event-codes) for possible values. |

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

