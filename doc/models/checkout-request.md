
# Checkout Request

## Structure

`CheckoutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_date` | [`str`](../../doc/models/string-enum.md) | Required | The order date of the shipment. Format dd-MM-YYYY HH:mm:ss<br>**Constraints**: *Pattern*: `^[0-3]\d-[0-1]\d-20\d{2}\s[0-2]\d:[0-5]\d:[0-5]\d$` |
| `shipping_duration` | `int` | Optional | The amount of days it takes for a parcel to be received by PostN. If you delivery the parcel the same day as the order is placed on the webshop, please use the value of 1. A value of 2 means the parcel will arrive at PostNL a day later etc. |
| `cut_off_times` | [`List[CutOffTime]`](../../doc/models/cut-off-time.md) | Required | Array of CutOffTimes |
| `holiday_sorting` | `bool` | Optional | Specifies whether you are available to ship parcels to PostNL during holidays |
| `options` | [`List[OptionEnum]`](../../doc/models/option-enum.md) | Required | Specifies the delivery and pickup options. |
| `locations` | `int` | Required | Specifies the number of locations you want returned. This can be a value of 1-3<br>**Constraints**: `>= 1`, `<= 3` |
| `days` | `int` | Required | Specifies the number of days for which the timeframes are returned. This can be a value of 1-9<br>**Constraints**: `>= 1`, `<= 9` |
| `addresses` | [`List[Address]`](../../doc/models/address.md) | Required | Array of addresses |

## Example (as JSON)

```json
{
  "OrderDate": "11-07-2019 12:34:54",
  "ShippingDuration": 1,
  "CutOffTimes": [
    {
      "Day": "00",
      "Available": true,
      "Type": "Regular",
      "Time": "23:00:00"
    }
  ],
  "HolidaySorting": true,
  "Options": [
    "Daytime",
    "Evening",
    "Pickup"
  ],
  "Locations": 2,
  "Days": 3,
  "Addresses": [
    {
      "AddressType": "01",
      "Street": "Molengraaffplantsoen",
      "HouseNr": 74,
      "HouseNrExt": "bis",
      "Zipcode": "3571ZZ",
      "City": "Utrecht",
      "Countrycode": "NL"
    }
  ]
}
```

