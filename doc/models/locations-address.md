
# Locations Address

## Structure

`LocationsAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The city of the pickup location address |
| `countrycode` | `str` | Optional | The country of the pickup location address |
| `house_nr` | `int` | Optional | The house number of the pickup location address |
| `house_nr_ext` | `str` | Optional | The house number extension of the pickup location address |
| `remark` | `str` | Optional | Additional information about the pickup location |
| `street` | `str` | Optional | The street of the pickup location address |
| `zipcode` | `str` | Optional | The zipcode of the pickup location address |

## Example (as JSON)

```json
{
  "City": "Hoofddorp",
  "Countrycode": "NL",
  "HouseNr": 42,
  "HouseNrExt": "-60",
  "Remark": "Dit is een Pakketpunt. Pakketten die je op werkdagen vóór lichtingstijd afgeeft, bezorgen we binnen Nederland de volgende dag. Op zaterdag worden alléén pakketten die je afgeeft voor 15:00 uur maandag bezorgd.",
  "Street": "Siriusdreef",
  "Zipcode": "2132WT"
}
```

