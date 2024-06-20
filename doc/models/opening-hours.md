
# Opening Hours

The standard opening hours of the pickup location

## Structure

`OpeningHours`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `tuesday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `wednesday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `thursday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `friday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `saturday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |
| `sunday` | [`OpeningHoursPerDay`](../../doc/models/opening-hours-per-day.md) | Optional | - |

## Example (as JSON)

```json
{
  "Monday": {
    "From": "From0",
    "To": "To0"
  },
  "Tuesday": {
    "From": "From2",
    "To": "To2"
  },
  "Wednesday": {
    "From": "From4",
    "To": "To4"
  },
  "Thursday": {
    "From": "From0",
    "To": "To0"
  },
  "Friday": {
    "From": "From6",
    "To": "To4"
  }
}
```

