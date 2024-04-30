
# Amount 1

The amounts belonging to the shipment

## Structure

`Amount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rembours_bedrag` | [`str`](../../doc/models/string-enum.md) | Optional | The cash-on-delivery (COD) amount |
| `verzekerd_bedrag` | [`str`](../../doc/models/string-enum.md) | Optional | The insurance amount of the shipment |

## Example (as JSON)

```json
{
  "RemboursBedrag": "EUR1079.00",
  "VerzekerdBedrag": "EUR500.00"
}
```

