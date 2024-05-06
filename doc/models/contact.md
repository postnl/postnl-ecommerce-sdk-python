
# Contact

## Structure

`Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contact_type` | [`str`](../../doc/models/string-enum.md) | Required | Type of the contact. This is a code. Please refer to the available [Contact types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/contact-types) for the possible values.<br>**Constraints**: *Pattern*: `^\d{2}$` |
| `email` | [`str`](../../doc/models/string-enum.md) | Optional | Email address of the contact. Mandatory in some cases. Either the Email or Telnr needs to be filled in for Non EU destinations. Please see [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/send-track/confirming/guidelines).<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `50` |
| `sms_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Mobile phone number of the contact. Mandatory in some cases. Please see [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/send-track/confirming/guidelines).<br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `17` |
| `tel_nr` | [`str`](../../doc/models/string-enum.md) | Optional | Phone number of the contact. Either the Email or Telnr needs to be filled in for Non EU destinations. Preferably prefixed with “+” and the international dialling code.<br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `17` |

## Example (as JSON)

```json
{
  "ContactType": "01",
  "Email": "receiver@email.com",
  "SMSNr": "+31612345678",
  "TelNr": "+31301234567"
}
```

