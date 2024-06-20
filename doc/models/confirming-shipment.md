
# Confirming Shipment

## Structure

`ConfirmingShipment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Required | List of 1 or more Address type elements. At least 1 address type is mandatory. See [Address types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/address-types) for the available types. |
| `amounts` | [`List[Amount]`](../../doc/models/amount.md) | Optional | List of amount types. An amount represents a value of the shipment. Amount type 01 mandatory for COD-shipments, Amount type 02 mandatory for domestic insured shipments. Please see [Amount types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/amount-types) for the available types. |
| `barcode` | `str` | Required | Barcode of the shipment. This is a unique value. Note: If you leave this attribute out of your request an unique barcode will be generated automatically.<br>**Constraints**: *Minimum Length*: `11`, *Maximum Length*: `15` |
| `coding_text` | `str` | Optional | Code used for logistic purposes (usually generated by the service itself and returned in the response). Please note that this must be provided when  using the Confirm API to confirm shipments where coding texts are required (e.g. letterbox parcels).<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `collection_time_stamp_start` | `str` | Optional | Starting date/time of the collection of the shipment. Format: dd-MM-yyyy hh:mm:ss<br>**Constraints**: *Pattern*: `^([0-3]\d-[01]\d-[12]\d{3}\s+)[0-2]\d:[0-5]\d(:[0-5]\d)$` |
| `collection_time_stamp_end` | `str` | Optional | Ending date/time of the collection of the shipment. Format: dd-MM-yyyy hh:mm:ss<br>**Constraints**: *Pattern*: `^([0-3]\d-[01]\d-[12]\d{3}\s+)[0-2]\d:[0-5]\d(:[0-5]\d)$` |
| `contacts` | [`List[Contact]`](../../doc/models/contact.md) | Optional | One or more ContactType elements belonging to a shipment. Mandatory in some cases. Please refer to the available [Contact types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/contact-types) for the possible values. |
| `content` | `str` | Optional | Content of the shipment. Mandatory for Extra@Home shipments<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `cost_center` | `str` | Optional | Cost center of the shipment. This value will appear on your invoice<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `customer_order_number` | `str` | Optional | Order number of the customer<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `customs` | [`List[ConfirmingCustom]`](../../doc/models/confirming-custom.md) | Optional | The Customs type is mandatory for non-EU shipments and not allowed for any other shipment types. |
| `delivery_address` | `str` | Optional | Delivery address specification. This field is mandatory when AddressType on the Address is 09.<br>**Constraints**: *Pattern*: `^\d{2}$` |
| `delivery_date` | `str` | Optional | Mandatory when using Mailbox Parcels (for generation of the coding rule) and delivery options like Evening/Morning/Sameday delivery etc.<br>**Constraints**: *Pattern*: `^[0-3]\d-[01]\d-[12]\d{3}\s[0-2]\d:[0-5]\d:[0-5]\d$` |
| `dimension` | [`Dimension`](../../doc/models/dimension.md) | Required | Note: Length, Width, Height values are about the order of the size and need to be filled in from the longest to the shortest value. For example: shipment's official height is 700mm, width 500mm, length 300mm. The longest side (highest value) of 700mm needs to be entered at Length. Width value becomes 500mm, Height value: 300mm (the lowest). Entering the dimensions in the wrong order may result in incorrect shipping labels and longer delivery times. The maximum dimensions can be found in your PostNL contract. |
| `down_partner_barcode` | `str` | Optional | Barcode of the downstream network partner of PostNL Parcels. Madatory for requesting Parcels Non-EU combilabel product codes.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `down_partner_id` | `str` | Optional | Identification of the downstream network partner of PostNL Pakketten.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `down_partner_location` | `str` | Optional | Identification of the location of the downstream network partner of PostNL Pakketten.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `10` |
| `groups` | [`List[Group]`](../../doc/models/group.md) | Optional | List of 0 or more Group types with data, grouping multiple shipments together. Mandatory for multicollo shipments. Please see [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/send-track/confirming/guidelines) (Multiple shipments) for more information. |
| `hazardous_material` | [`List[HazardousMaterial]`](../../doc/models/hazardous-material.md) | Optional | Array of hazardous materials contained in the shipment |
| `product_code_collect` | `str` | Optional | Deprecated. Collection product code of a shipment. |
| `product_code_delivery` | `str` | Required | Product code of the shipment. See the [Products page](https://developer.postnl.nl/docs/#/http/reference-data/product-codes) for possible products.<br>**Default**: `'3085'`<br>**Constraints**: *Pattern*: `^\d{4,5}$` |
| `product_options` | [`List[ProductOption]`](../../doc/models/product-option.md) | Optional | Product options for the shipment, mandatory for certain products, see the [Products page](https://developer.postnl.nl/docs/#/http/reference-data/product-codes). |
| `receiver_date_of_birth` | `str` | Optional | Date of birth. Mandatory for Age check products<br>**Constraints**: *Pattern*: `^([0-3]\d-[01]\d-[12]\d{3})$` |
| `reference` | `str` | Optional | Your own reference of the shipment. Mandatory for Extra@Home shipments; for E@H this is used to create your order number, so this should be unique for each request. |
| `reference_collect` | `str` | Optional | Additional reference of the collect order of the shipment |
| `remark` | `str` | Optional | Remark of the shipment. |
| `return_barcode` | `str` | Optional | Return barcode of the shipment. PostNL will provide you with a separate customer code specifically for generating the returnBarcode. Mandatory for Label in the Box (return label) shipments. |
| `return_reference` | `str` | Optional | Return reference of the shipment |
| `timeslot_id` | `str` | Optional | Deprecated. ID of the chosen timeslot as returned by the timeslot webservice |

## Example (as JSON)

```json
{
  "Addresses": [
    {
      "AddressType": "01",
      "Area": "Tuindorp-Oost",
      "Buildingname": "Gebouw 1",
      "City": "Utrecht",
      "CompanyName": "Janssen B.V.",
      "Countrycode": "NL",
      "Department": "Finance",
      "Doorcode": "3345",
      "FirstName": "Henk",
      "Floor": "2nd floor",
      "HouseNr": "74",
      "HouseNrExt": "A",
      "Name": "de Graaff",
      "Region": "Utrecht",
      "Street": "Molengraaffplantsoen",
      "Zipcode": "3571ZZ"
    }
  ],
  "Barcode": "3SDEVC201611214",
  "CodingText": "#2426A3A#03#0306#",
  "CollectionTimeStampStart": "04-12-2022 17:00:00",
  "CollectionTimeStampEnd": "04-12-2022 19:00:00",
  "Content": "Media player",
  "CostCenter": "SX-GT-66",
  "CustomerOrderNumber": "8689242390",
  "DeliveryAddress": "01",
  "DeliveryDate": "30-06-2016 12:00:00",
  "Dimension": {
    "Height": 300,
    "Length": 700,
    "Volume": 30000,
    "Weight": 4300,
    "Width": 500
  },
  "DownPartnerBarcode": "CD123456785NL",
  "DownPartnerLocation": "PNPNL-01",
  "ProductCodeCollect": "3153",
  "ProductCodeDelivery": "3085",
  "ReceiverDateOfBirth": "10-12-1980",
  "Reference": "REF-2016014567",
  "ReferenceCollect": "REF-6659150",
  "Remark": "Fragile",
  "ReturnBarcode": "3SDEVR7762162",
  "ReturnReference": "REF-639265677788",
  "Amounts": [
    {
      "AmountType": "AmountType4",
      "AccountName": "AccountName0",
      "BIC": "BIC6",
      "Currency": "Currency8",
      "IBAN": "IBAN4",
      "Reference": "Reference2",
      "Value": 22.62
    },
    {
      "AmountType": "AmountType4",
      "AccountName": "AccountName0",
      "BIC": "BIC6",
      "Currency": "Currency8",
      "IBAN": "IBAN4",
      "Reference": "Reference2",
      "Value": 22.62
    },
    {
      "AmountType": "AmountType4",
      "AccountName": "AccountName0",
      "BIC": "BIC6",
      "Currency": "Currency8",
      "IBAN": "IBAN4",
      "Reference": "Reference2",
      "Value": 22.62
    }
  ],
  "Contacts": [
    {
      "ContactType": "ContactType6",
      "Email": "Email2",
      "SMSNr": "SMSNr8",
      "TelNr": "TelNr6"
    }
  ]
}
```
