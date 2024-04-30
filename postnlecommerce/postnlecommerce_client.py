# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from postnlecommerce.configuration import Configuration
from postnlecommerce.controllers.base_controller import BaseController
from postnlecommerce.configuration import Environment
from postnlecommerce.http.auth.custom_header_authentication import CustomHeaderAuthentication
from postnlecommerce.controllers.barcode_controller import BarcodeController
from postnlecommerce.controllers.checkout_controller import CheckoutController
from postnlecommerce.controllers.confirming_controller\
    import ConfirmingController
from postnlecommerce.controllers.deliverydate_controller\
    import DeliverydateController
from postnlecommerce.controllers.labelling_controller\
    import LabellingController
from postnlecommerce.controllers.locations_controller\
    import LocationsController
from postnlecommerce.controllers.postalcode_check_controller\
    import PostalcodeCheckController
from postnlecommerce.controllers.shipment_controller import ShipmentController
from postnlecommerce.controllers.shipping_status_controller\
    import ShippingStatusController
from postnlecommerce.controllers.timeframes_controller\
    import TimeframesController


class PostnlecommerceClient(object):
    @LazyProperty
    def barcode(self):
        return BarcodeController(self.global_configuration)

    @LazyProperty
    def checkout(self):
        return CheckoutController(self.global_configuration)

    @LazyProperty
    def confirming(self):
        return ConfirmingController(self.global_configuration)

    @LazyProperty
    def deliverydate(self):
        return DeliverydateController(self.global_configuration)

    @LazyProperty
    def labelling(self):
        return LabellingController(self.global_configuration)

    @LazyProperty
    def locations(self):
        return LocationsController(self.global_configuration)

    @LazyProperty
    def postalcode_check(self):
        return PostalcodeCheckController(self.global_configuration)

    @LazyProperty
    def shipment(self):
        return ShipmentController(self.global_configuration)

    @LazyProperty
    def shipping_status(self):
        return ShippingStatusController(self.global_configuration)

    @LazyProperty
    def timeframes(self):
        return TimeframesController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=3, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment=Environment.PRODUCTION_SERVER, apikey=None,
                 custom_header_authentication_credentials=None, config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, apikey=apikey,
            custom_header_authentication_credentials=custom_header_authentication_credentials)

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())

        self.auth_managers = {key: None for key in ['APIKeyHeader']}
        self.auth_managers['APIKeyHeader'] = CustomHeaderAuthentication(
            self.config.custom_header_authentication_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

