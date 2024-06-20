
# Customs

The Customs type is mandatory for non-EU shipments and not allowed for any other shipment types.

## Structure

`Customs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate` | `bool` | Optional | Fill in if applicable, for specific items a export certificate is obliged, as proof that the item complies to the sanity regulations, [more information](https://ondernemersplein.kvk.nl/fytosanitair-of-veterinair-exportcertificaat-aanvragen/). Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected) |
| `certificate_nr` | `str` | Optional | Mandatory when Certificate is true.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `license` | `bool` | Optional | Fill in if applicable. Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected). |
| `license_nr` | `str` | Optional | Mandatory when License is true. |
| `invoice` | `bool` | Optional | Fill in the invoice number of the shipment. For a faster customs clearing process apply the invoice on the outside of the shipment. Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected). |
| `invoice_nr` | `str` | Optional | Mandatory when Invoice is true |
| `handle_as_non_deliverable` | `bool` | Optional | Determines what to do when the shipment cannot be delivered the first time (if this is set to true,the shipment will be returned after the first failed attempt) |
| `currency` | [`CurrencyLabellingAPIEnum`](../../doc/models/currency-labelling-api-enum.md) | Required | Currency code,only EUR and USS are allowed |
| `shipment_type` | [`ShipmentTypeEnum`](../../doc/models/shipment-type-enum.md) | Required | Type of shipment,possible values: Gift,Documents,Commercial Goods,Commercial Sample,Returned Goods |
| `trusted_shipper_id` | `str` | Optional | 'Use only when available. Depending on the destination with this ID the customs process can be faster. Only fill in this customs reference number if the sender is registrated as Trusted Shipper in the country of destination'<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `importer_reference_code` | `str` | Optional | Importer reference code. Fill in a Tax Code or VAT number or Importer code. Depending on the destination with this reference the customs process can be faster.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `transaction_code` | `str` | Optional | Code and accompanying description according to UPU Codelist 136. Codes to be used are shown below for your reference. Or see the [Reference data](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/transaction-codes).<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `transaction_description` | `str` | Optional | Transaction description; see [here](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/transaction-codes) for common examples.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `content` | [`List[LabellingCustomsContent]`](../../doc/models/labelling-customs-content.md) | Required | The contents of the shipment. This section is mandatory (minimum once, maximum 5). |

## Example (as JSON)

```json
{
  "Certificate": true,
  "CertificateNr": "CERT-1235986739",
  "License": true,
  "LicenseNr": "LIC-9847397",
  "Invoice": true,
  "InvoiceNr": "INV_0120330",
  "HandleAsNonDeliverable": false,
  "Currency": "EUR",
  "ShipmentType": "Commercial Goods",
  "TrustedShipperID": "NL862386524",
  "ImporterReferenceCode": "GB339713089011",
  "TransactionCode": "11",
  "TransactionDescription": "Sale of goods",
  "Content": [
    {
      "Description": "Powdered milk",
      "Quantity": 2,
      "Weight": 2600,
      "Value": 119.99,
      "HSTariffNr": "100878",
      "CountryOfOrigin": "NL"
    }
  ]
}
```

