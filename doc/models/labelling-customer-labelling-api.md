
# Labelling Customer Labelling API

## Structure

`LabellingCustomerLabellingAPI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`CustomerAddress`](../../doc/models/customer-address.md) | Optional | - |
| `collection_location` | `str` | Optional | Code of delivery location at PostNL Pakketten<br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `contact_person` | `str` | Optional | Name of customer contact person |
| `customer_code` | `str` | Required | Customer code as known at PostNL Pakketten<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `6` |
| `customer_number` | `str` | Required | Name of customer contact person<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `8` |
| `email` | `str` | Optional | E-mail address of the customer<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `name` | `str` | Optional | Customer name<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "CollectionLocation": "123456",
  "ContactPerson": "Janssen",
  "CustomerCode": "DEVC",
  "CustomerNumber": "11223344",
  "Email": "email@company.com",
  "Name": "Janssen",
  "Address": {
    "AddressType": "AddressType6",
    "Area": "Area2",
    "Buildingname": "Buildingname6",
    "City": "City6",
    "CompanyName": "CompanyName8",
    "Countrycode": "Countrycode2",
    "Department": "Department2",
    "Doorcode": "Doorcode8"
  }
}
```

