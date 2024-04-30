
# Address 11

## Structure

`Address11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address_type` | [`str`](../../doc/models/string-enum.md) | Required | Type of the address. This is a code. You can find the possible values at [Address types](#tag/Reference-codes/Address-types)<br>**Default**: `'01'`<br>**Constraints**: *Pattern*: `^\d{2}$` |
| `area` | [`str`](../../doc/models/string-enum.md) | Optional | Area of the address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `buildingname` | [`str`](../../doc/models/string-enum.md) | Optional | Building name of the address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `city` | [`str`](../../doc/models/string-enum.md) | Optional | City of the address<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `company_name` | [`str`](../../doc/models/string-enum.md) | Optional | This field has a dependency with the field Name. One of both fields must be filled mandatory; using both fields is also allowed. Mandatory when AddressType is 09.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `countrycode` | [`str`](../../doc/models/string-enum.md) | Required | The ISO2 country codes<br>**Constraints**: *Pattern*: `^[A-Z]{2}$` |
| `department` | [`str`](../../doc/models/string-enum.md) | Optional | Send to specific department of a company<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `doorcode` | [`str`](../../doc/models/string-enum.md) | Optional | Door code of address. Mandatory for some international shipments.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `first_name` | [`str`](../../doc/models/string-enum.md) | Optional | Remark: please add FirstName and Name (lastname) of the receiver to improve the parcel tracking experience of your customer.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `floor` | [`str`](../../doc/models/string-enum.md) | Optional | Send to specific floor of a company<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `house_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Mandatory for shipments to Benelux. Max. length is 5 characters (only for Benelux addresses). For Benelux addresses,this field should always be numeric.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `house_nr_ext` | [`str`](../../doc/models/string-enum.md) | Optional | House number extension<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `name` | [`str`](../../doc/models/string-enum.md) | Optional | Last name of person. This field has a dependency with the field CompanyName. One of both fields must be filled mandatory; using both fields is also allowed. Remark: please add FirstName and Name (lastname) of the receiver to improve the parcel tracking experience of your customer.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `region` | [`str`](../../doc/models/string-enum.md) | Optional | Region of the address. Mandatory for Non EU destinations where a region is applicable.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `street` | [`str`](../../doc/models/string-enum.md) | Optional | This field has a dependency with the field StreetHouseNrExt. One of both fields must be filled mandatory. Using both fields simultaneously is discouraged.<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `95` |
| `street_house_nr_ext` | [`str`](../../doc/models/string-enum.md) | Optional | Combination of Street, HouseNr and HouseNrExt. Please see [Guidelines](https://developer.postnl.nl/browse-apis/send-and-track/labelling-webservice/) for the explanation. |
| `zipcode` | [`str`](../../doc/models/string-enum.md) | Optional | Zipcode of the address. Mandatory for shipments to Benelux. Max length (NL) 6 characters,(BE;LU) 4 numeric characters<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `17` |

## Example (as JSON)

```json
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
```

