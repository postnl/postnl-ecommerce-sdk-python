
# Hazardous Material

## Structure

`HazardousMaterial`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `toxic_substance_code` | `str` | Required | Toxic substance code as stated in the ADR agreement |
| `additional_toxic_substance_code` | `List[str]` | Optional | Array of additional toxic substance codes as stated in the ADR agreement |
| `adr_points` | `str` | Optional | The amount of ADR points |
| `tunnel_code` | `str` | Optional | The code indicating for which category of tunnels passage is prohibited with these goods. |
| `packaging_group_code` | `str` | Optional | Code identifying the category of the packaging material. |
| `packaging_group_description` | `str` | Optional | Description of the packaging material |
| `gross_weight` | `str` | Optional | Gross weight of the goods in grams. |
| `undg_number` | `str` | Optional | The UNDG number |
| `transport_category_code` | `str` | Optional | The transport category code |
| `chemical_technical_description` | `str` | Optional | The chemical technical description of the goods. |

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

