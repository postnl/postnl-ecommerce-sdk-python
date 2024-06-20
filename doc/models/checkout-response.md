
# Checkout Response

## Structure

`CheckoutResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_options` | [`List[CheckoutDeliveryOption]`](../../doc/models/checkout-delivery-option.md) | Optional | Array of delivery options |
| `pickup_options` | [`List[CheckoutPickupOption]`](../../doc/models/checkout-pickup-option.md) | Optional | Array of possible pickup options |
| `warnings` | [`List[CheckoutWarning]`](../../doc/models/checkout-warning.md) | Optional | An array of warnings |

## Example (as JSON)

```json
{
  "DeliveryOptions": [
    {
      "DeliveryDate": "DeliveryDate8",
      "Timeframe": [
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        }
      ]
    },
    {
      "DeliveryDate": "DeliveryDate8",
      "Timeframe": [
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        }
      ]
    },
    {
      "DeliveryDate": "DeliveryDate8",
      "Timeframe": [
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        },
        {
          "From": "From0",
          "To": "To0",
          "Options": [
            "Today",
            "08:00-10:00",
            "08:00-12:00"
          ],
          "ShippingDate": "ShippingDate4",
          "Sustainability": {
            "Code": "02",
            "Description": "Description4"
          }
        }
      ]
    }
  ],
  "PickupOptions": [
    {
      "PickupDate": "PickupDate0",
      "ShippingDate": "ShippingDate8",
      "Option": "Option8",
      "Locations": [
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        }
      ]
    },
    {
      "PickupDate": "PickupDate0",
      "ShippingDate": "ShippingDate8",
      "Option": "Option8",
      "Locations": [
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        }
      ]
    },
    {
      "PickupDate": "PickupDate0",
      "ShippingDate": "ShippingDate8",
      "Option": "Option8",
      "Locations": [
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        },
        {
          "Address": {
            "Street": "Street6",
            "Zipcode": "Zipcode8",
            "HouseNr": 136,
            "HouseNrExt": "HouseNrExt4",
            "Countrycode": "Countrycode2"
          },
          "PickupTime": "PickupTime0",
          "OpeningHours": {
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
          },
          "Distance": 200,
          "LocationCode": "LocationCode8"
        }
      ]
    }
  ],
  "Warnings": [
    {
      "DeliveryDate": "DeliveryDate2",
      "Code": "Code4",
      "Description": "Description8",
      "Options": "Sameday"
    }
  ]
}
```

