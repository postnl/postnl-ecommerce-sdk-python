
# Signature

## Structure

`Signature`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode` | `str` | Optional | The barcode of the shipment for which the signature is returned |
| `signature_date` | `str` | Optional | The date of the signature |
| `signature_image` | `str` | Optional | The signature content; base64 encoded GIF format. |

## Example (as JSON)

```json
{
  "Barcode": "3SDEVC317858754",
  "SignatureDate": "11/07/2022 19:28:16",
  "SignatureImage": "iVBORw0KGgoAAAANSUhEUgAAAogAAAGTCAYAAACrs[TRUNCATED]"
}
```

