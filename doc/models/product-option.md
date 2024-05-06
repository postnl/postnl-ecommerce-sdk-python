
# Product Option

## Structure

`ProductOption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `characteristic` | [`str`](../../doc/models/string-enum.md) | Required | The characteristic of the ProductOption. Mandatory for some products, please see the [Products page](https://developer.postnl.nl/docs/#/http/reference-data/product-codes)<br>**Default**: `'118'`<br>**Constraints**: *Pattern*: `^\d{3}$` |
| `option` | [`str`](../../doc/models/string-enum.md) | Required | The product option code for this ProductOption. Mandatory for some products, please see the [Products page](https://developer.postnl.nl/docs/#/http/reference-data/product-codes)<br>**Default**: `'006'`<br>**Constraints**: *Pattern*: `^\d{3}$` |

## Example (as JSON)

```json
{
  "Characteristic": "118",
  "Option": "006"
}
```

