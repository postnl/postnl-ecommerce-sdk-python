
# Labelling Customer Message

## Structure

`LabellingCustomerMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_id` | `str` | Required | ID of the message<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `12` |
| `message_time_stamp` | `str` | Required | Date/time of sending the message. Format: dd-mm-yyyy hh:mm:ss<br>**Constraints**: *Pattern*: `^[0-3]\d-[01]\d-[12]\d{3}\s[0-2]\d:[0-5]\d:[0-5]\d$` |
| `printertype` | `str` | Required | Printer type that will be used to process the label, e.g. Zebra printer or PDF See [Printer types](https://developer.postnl.nl/docs/#/http/reference-data/reference-codes/printer-types) for the available printer types. |

## Example (as JSON)

```json
{
  "MessageID": "1",
  "MessageTimeStamp": "29-06-2016 12:00:00",
  "Printertype": "GraphicFile|PDF"
}
```

