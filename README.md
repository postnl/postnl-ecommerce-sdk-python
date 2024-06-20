
# Getting Started with Postnl-Ecommerce

## Introduction

<div><p><b>PostNL Ecommerce APIs</b></p><p>Explore our technical documentation, test your integration and go live with PostNL service.</p><p><b>Start using PostNL APIs for e-commerce processes</b></p><p>To get to know the PostNL APIs better, read all about it in our <a href='https://developer.postnl.nl/api-overview/'>API overview</a>. Learn everything you need to about our API's before embarking on integration with PostNL.</p><p>To connect to PostNL, you can request an API key via <a href='https://mijn.postnl.nl/c/BP2_Mod_Login.app?inresponseto=&RelayState=&startURL=%2F'>Mijn PostNL</a> portal. Choose your APIs and build your integration. Explore our guides, examples, and resources to guide you through each phase of integration and start testing. Ensure that you can make successful test calls towards all endpoints used in the solution.</p><p>Contact our integrations team to have your test calls reviewed and gain access to our API production environment. Once everything is configured and validated, you'll be ready to go live and start using the PostNL service.</p><p>For help contact us via our support form: <a href='https://developer.postnl.nl/support/form/'>Need help? Submit a case | PostNL</a>.</p></div>


## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install postnl-ecommerce-sdk==1.0.5
```

You can also view the package at:
https://pypi.python.org/pypi/postnl-ecommerce-sdk/1.0.5

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION_SERVER`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 3** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `custom_header_authentication_credentials` | [`CustomHeaderAuthenticationCredentials`](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/$a/https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/custom-header-signature.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

```python
client = PostnlecommerceClient(
    custom_header_authentication_credentials=CustomHeaderAuthenticationCredentials(
        apikey='apikey'
    )
)
```

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Production server | **Default** Production server |
| Non-Production server | Sandbox environment for testing |

## Authorization

This API uses the following authentication schemes.

* [`APIKeyHeader (Custom Header Signature)`](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/$a/https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/custom-header-signature.md)

## List of APIs

* [Postalcodecheck](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/postalcodecheck.md)
* [Barcode](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/barcode.md)
* [Checkout](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/checkout.md)
* [Confirming](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/confirming.md)
* [Deliverydate](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/deliverydate.md)
* [Labelling](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/labelling.md)
* [Locations](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/locations.md)
* [Shipment](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/shipment.md)
* [Shipping Status](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/shipping-status.md)
* [Timeframes](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/controllers/timeframes.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/http-response.md)
* [HttpRequest](https://www.github.com/postnl/postnl-ecommerce-sdk-python/tree/1.0.5/doc/http-request.md)

