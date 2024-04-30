
# Group

## Structure

`Group`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_type` | [`str`](../../doc/models/string-enum.md) | Required | Group sort that determines the type of group that is indicated. This is a code. For possible values, please see [here](#tag/Reference-codes/Group-types)<br>**Constraints**: *Pattern*: `^\d{2}$` |
| `group_sequence` | `int` | Optional | Sequence number of the collo within the complete shipment (e.g. collo 2 of 4) Mandatory for multicollo shipments |
| `group_count` | `int` | Optional | Total number of colli in the shipment (in case of multicolli shipments) Mandatory for multicollo shipments |
| `main_barcode` | [`str`](../../doc/models/string-enum.md) | Required | Main barcode for the shipment (in case of multicolli shipments) Mandatory for multicollo shipments<br>**Constraints**: *Minimum Length*: `11`, *Maximum Length*: `15` |

## Example (as JSON)

```json
{
  "GroupType": "03",
  "GroupSequence": 1,
  "GroupCount": 2,
  "MainBarcode": "3SDEVC7239264"
}
```

