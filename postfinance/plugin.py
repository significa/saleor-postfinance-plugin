from typing import TYPE_CHECKING

from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

from ..utils import get_supported_currencies, require_active_plugin
from . import GatewayConfig, confirm, process_payment

GATEWAY_NAME = "PostFinance"

if TYPE_CHECKING:
    from . import GatewayResponse, PaymentData

class PostFinanceGatewayPlugin(BasePlugin):
    PLUGIN_NAME = GATEWAY_NAME
    PLUGIN_ID = "significa.payments.postfinance"
    DEFAULT_CONFIGURATION = [
        {"name": "Supported currencies", "value": "CHF"},
        {"name": "Space ID", "value": None},
        {"name": "User ID", "value": None},
        {"name": "User Secret Key", "value": None},
    ]
    # Some examples
    CONFIG_STRUCTURE = {
        "Space ID": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "PostFinance Space ID",
            "label": "Space ID",
        },
        "User ID": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "PostFinance Application User ID",
            "label": "User ID",
        },
        "User Secret Key": {
            "type": ConfigurationTypeField.SECRET,
            "help_text": "PostFinance Application User Secret Key",
            "label": "Secret Key",
        },
        "Supported currencies": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Determines currencies supported by gateway."
            " Please enter currency codes separated by a comma.",
            "label": "Supported currencies",
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        configuration = {item["name"]: item["value"] for item in self.configuration}

        self.config = GatewayConfig(
            gateway_name=GATEWAY_NAME,
            auto_capture=None,
            supported_currencies=configuration["Supported currencies"],
            connection_params={
                "space_id":  int(configuration["Space ID"]) if configuration["Space ID"] else None,
                "user_id": int(configuration["User ID"]) if configuration["User ID"] else None,
                "user_secret":  configuration["User Secret Key"],
            }
        )

        print(self.config)


    def _get_gateway_config(self):
        return self.config

    # @require_active_plugin
    # def authorize_payment(
    #     self, payment_information: "PaymentData", previous_value
    # ) -> "GatewayResponse":
    #     print("AUTHORIZE")
    #     return authorize(payment_information, self._get_gateway_config())

    # @require_active_plugin
    # def capture_payment(
    #     self, payment_information: "PaymentData", previous_value
    # ) -> "GatewayResponse":
    #     return capture(payment_information, self._get_gateway_config())

    @require_active_plugin
    def confirm_payment(
        self, payment_information: "PaymentData", previous_value
    ) -> "GatewayResponse":
        print("AUTHORIZE2")
        # After setting TransactionKind.ACTION_TO_CONFIRM 
        return confirm(payment_information, self._get_gateway_config())

    # @require_active_plugin
    # def refund_payment(
    #     self, payment_information: "PaymentData", previous_value
    # ) -> "GatewayResponse":
    #     print("AUTHORIZE3")

    #     return refund(payment_information, self._get_gateway_config())

    # @require_active_plugin
    # def void_payment(
    #     self, payment_information: "PaymentData", previous_value
    # ) -> "GatewayResponse":
    #     print("AUTHORIZE4")

    #     return void(payment_information, self._get_gateway_config())

    @require_active_plugin
    def process_payment(
        self, payment_information: "PaymentData", previous_value
    ) -> "GatewayResponse":
        print("AUTHORIZE5")
        print(payment_information)
        return process_payment(payment_information, self._get_gateway_config())

    # @require_active_plugin
    # def get_client_token(self, token_config: "TokenConfig", previous_value):
    #     print("AUTHORIZE6")

    #     return get_client_token()

    @require_active_plugin
    def get_supported_currencies(self, previous_value):
        print("AUTHORIZE7")

        config = self._get_gateway_config()
        return get_supported_currencies(config, GATEWAY_NAME)

    # talvez remover
    @require_active_plugin
    def get_payment_config(self, previous_value):
        print("AUTHORIZE8")

        config = self._get_gateway_config()
        return [{"field": "store_customer_card", "value": config.store_customer}]
