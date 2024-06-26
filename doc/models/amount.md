
# Amount

## Structure

`Amount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_type` | `str` | Required | Amount type. Please see [Amount types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/amount-types) for the available types.<br>**Constraints**: *Pattern*: `^\d{2}$` |
| `account_name` | `str` | Optional | Name of bank account owner<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `bic` | `str` | Optional | BIC number,optional for COD shipments (mandatory for bank account number other than originating in The Netherlands)<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |
| `currency` | `str` | Optional | Currency code. only EUR, GBP, USD and CNY are allowed.<br>**Constraints**: *Pattern*: `^[A-Z]{3}$` |
| `iban` | `str` | Optional | IBAN bank account number,mandatory for COD shipments. Dutch IBAN numbers are 18 characters<br>**Constraints**: *Minimum Length*: `15`, *Maximum Length*: `31` |
| `reference` | `str` | Optional | Personal payment reference<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `transaction_number` | `str` | Optional | Transaction number<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `35` |
| `value` | `float` | Required | Money value in EUR (unless value Currency is specified for another currency). Value format (N6.2): #####0.00 (2 digits behind decimal dot). Mandatory for COD, Insured products (with the exception of certain productcodes with a standard insured amount).<br>**Constraints**: `>= 0` |

## Example (as JSON)

```json
{
  "AmountType": "01",
  "AccountName": "C. de Ruiter",
  "BIC": "RABONL2UXXX",
  "Currency": "EUR",
  "IBAN": "NL00RABO0123456789",
  "Reference": "1234-5678",
  "TransactionNumber": "1234",
  "Value": 20.35
}
```

