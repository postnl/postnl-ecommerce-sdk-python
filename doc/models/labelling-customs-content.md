
# Labelling Customs Content

## Structure

`LabellingCustomsContent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Description of goods<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `quantity` | `int` | Required | Fill in the total of the item(s)<br>**Constraints**: `>= 1` |
| `weight` | `int` | Required | Net weight of goods in gram(gr) |
| `value` | `float` | Required | Commercial (customs) value of goods. Fill in the value of the item(s). |
| `hs_tariff_nr` | `str` | Optional | Specify every item with the standard HS commodity code (HS-code), [more information](https://tarief.douane.nl/ite-tariff-public/#/home)<br>**Constraints**: *Minimum Length*: `6`, *Maximum Length*: `6` |
| `country_of_origin` | `str` | Optional | Fill in the code of the country where the item was produced (ISO-code), [more information](https://www.iso.org/home.html)<br>**Constraints**: *Pattern*: `^[A-Z]{2}$` |

## Example (as JSON)

```json
{
  "Description": "Powdered milk",
  "Quantity": 2,
  "Weight": 2600,
  "Value": 119.99,
  "HSTariffNr": "100878",
  "CountryOfOrigin": "NL"
}
```

