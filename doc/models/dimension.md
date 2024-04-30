
# Dimension

Note: Length, Width, Height values are about the order of the size and need to be filled in from the longest to the shortest value. For example: shipment’s official height is 700mm, width 500mm, length 300mm. The longest side (highest value) of 700mm needs to be entered at Length. Width value becomes 500mm, Height value: 300mm (the lowest). Entering the dimensions in the wrong order may result in incorrect shipping labels and longer delivery times. The maximum dimensions can be found in your PostNL contract.

## Structure

`Dimension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `height` | `int` | Optional | The shortest side of the shipment in millimeters (mm).<br>**Constraints**: `>= 1` |
| `length` | `int` | Optional | The longest side of the shipment in millimeters (mm).<br>**Constraints**: `>= 1` |
| `volume` | `int` | Optional | Volume of the shipment in centimeters (cm3). Mandatory for E@H-products.<br>**Constraints**: `>= 1` |
| `weight` | `int` | Required | Weight of the shipment in grams. Approximate weight suffices<br>**Constraints**: `>= 1` |
| `width` | `int` | Optional | The second longest side of the shipment in millimeters (mm).<br>**Constraints**: `>= 1` |

## Example (as JSON)

```json
{
  "Height": 300,
  "Length": 700,
  "Volume": 30000,
  "Weight": 4300,
  "Width": 500
}
```

