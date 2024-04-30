
# Custom

The Customs type is mandatory for non-EU shipments and not allowed for any other shipment types.

## Structure

`Custom`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `certificate` | `bool` | Optional | Fill in if applicable, for specific items a export certificate is obliged, as proof that the item complies to the sanity regulations, [more information](https://ondernemersplein.kvk.nl/fytosanitair-of-veterinair-exportcertificaat-aanvragen/). Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected) |
| `certificate_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Mandatory when Certificate is true.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `license` | `bool` | Optional | Fill in if applicable. Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected). |
| `license_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Mandatory when License is true. |
| `invoice` | `bool` | Optional | Fill in the invoice number of the shipment. For a faster customs clearing process apply the invoice on the outside of the shipment. Mandatory for Parcel shipments in the category type Commercial Goods, Commercial Sample and Returned Goods (Certificate, Invoice or License; at least 1 out of 3 must be selected). |
| `invoice_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Mandatory when Invoice is true |
| `handle_as_non_deliverable` | `bool` | Optional | Determines what to do when the shipment cannot be delivered the first time (if this is set to true,the shipment will be returned after the first failed attempt) |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Required | Currency code. only EUR, GBP, USD and CNY are allowed. |
| `shipment_type` | [`ShipmentTypeEnum`](../../doc/models/shipment-type-enum.md) | Required | Type of shipment, possible values: Gift, Documents, Commercial Goods, Commercial Sample, Returned Goods. Is used to fill in the checkbox on the customs form on the shipment label. |
| `trusted_shipper_id` | [`str`](../../doc/models/string-enum.md) | Optional | Use only when available. This is the reference of the sender. Depending on the destination with this ID, EORI, IOSS, TAX, VAT, VOEC*, the customs process can be faster. Only fill in this customs reference number if the sender is registrated as Trusted Shipper in the country of destination.  *VOEC is a Norwegian VAT number.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `importer_reference_code` | [`str`](../../doc/models/string-enum.md) | Optional | This is the reference of the recipient. Fill in a Tax Code or VAT number or Importer code. Depending on the destination with this reference the customs process can be faster. For example Brazil uses an TAXID number for natural persons, known as CPF.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `transaction_code` | [`str`](../../doc/models/string-enum.md) | Optional | See the [Reference data](#tag/Reference-codes/Transaction-codes) for possible values.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `transaction_description` | [`str`](../../doc/models/string-enum.md) | Optional | Transaction description; see [here](#tag/Reference-codes/Transaction-codes) for common examples.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `content` | [`List[Content]`](../../doc/models/content.md) | Required | The contents of the shipment. This section is mandatory (minimum once, maximum 5). Fill per unique item. |

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

