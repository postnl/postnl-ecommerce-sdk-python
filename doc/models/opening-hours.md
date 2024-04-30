
# Opening Hours

The standard opening hours of the pickup location

## Structure

`OpeningHours`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `monday` | [`Monday`](../../doc/models/monday.md) | Optional | - |
| `tuesday` | [`Tuesday`](../../doc/models/tuesday.md) | Optional | - |
| `wednesday` | [`Wednesday`](../../doc/models/wednesday.md) | Optional | - |
| `thursday` | [`Thursday`](../../doc/models/thursday.md) | Optional | - |
| `friday` | [`Friday`](../../doc/models/friday.md) | Optional | - |
| `saturday` | [`Saturday`](../../doc/models/saturday.md) | Optional | - |
| `sunday` | [`Sunday`](../../doc/models/sunday.md) | Optional | - |

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

