
# Hazardous Material

## Structure

`HazardousMaterial`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `toxic_substance_code` | [`str`](../../doc/models/string-enum.md) | Required | Toxic substance code as stated in the ADR agreement |
| `additional_toxic_substance_code` | [`List[str]`](../../doc/models/string-enum.md) | Optional | Array of additional toxic substance codes as stated in the ADR agreement |
| `adr_points` | [`str`](../../doc/models/string-enum.md) | Optional | The amount of ADR points |
| `tunnel_code` | [`str`](../../doc/models/string-enum.md) | Optional | The code indicating for which category of tunnels passage is prohibited with these goods. |
| `packaging_group_code` | [`str`](../../doc/models/string-enum.md) | Optional | Code identifying the category of the packaging material. |
| `packaging_group_description` | [`str`](../../doc/models/string-enum.md) | Optional | Description of the packaging material |
| `gross_weight` | [`str`](../../doc/models/string-enum.md) | Optional | Gross weight of the goods in grams. |
| `undg_number` | [`str`](../../doc/models/string-enum.md) | Optional | The UNDG number |
| `transport_category_code` | [`str`](../../doc/models/string-enum.md) | Optional | The transport category code |
| `chemical_technical_description` | [`str`](../../doc/models/string-enum.md) | Optional | The chemical technical description of the goods. |

## Example (as JSON)

```json
{
  "ToxicSubstanceCode": "8",
  "AdditionalToxicSubstanceCode": [
    "1-11",
    "28-4"
  ],
  "ADRPoints": "30",
  "TunnelCode": "(E)",
  "PackagingGroupCode": "III",
  "PackagingGroupDescription": "Jerrycan plastic",
  "GrossWeight": "30000",
  "UNDGNumber": "UN 1760",
  "TransportCategoryCode": "3",
  "ChemicalTechnicalDescription": "FOSFORZUUR"
}
```

