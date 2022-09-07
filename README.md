# Saleor PostFinance plugin

PostFinance gateway plugin for Saleor. This is a partially implementation, it only supports PostFinance [payment page integration](https://checkout.postfinance.ch/doc/payment/payment-page) and it does not support refunds and void payments.

### Setup PostFinance Plugin

1. Navigate to Saleor Dashboard configuration and go to Plugins (Miscellaneous)
2. Select the channel where you want to activate the plugin, fill in the  settings and set the plugin as active. (Keep in mind some payment methods used in PostFinance (ex: Twint) will only support with CHF currency.)

### Steps to use the plugin

1. Create a checkout using the channel where the plugin is active.

```graphql
mutation checkoutCreate {
    checkoutCreate(
        input: {
            channel: "switzerland-channel-example",
            email: ...,
            shippingAddress: ...,
            lines: [{quantity: 1, variantId: "UHJvZHVjdFZhcmlhbnQ6Mzg0"}]
        }
    ) {
        checkout {
            id
        }
    }
}
```

2. Set checkout delivery method and set checkout billing address, for that you can use `checkoutDeliveryMethodUpdate` and `checkoutBillingAddressUpdate` mutations.

3. Create checkout payment with PostFinance gateway ("significa.payments.postfinance")

```graphql
mutation checkoutPaymentCreate {
    checkoutPaymentCreate(
        id: "Q2hlY2tvdXQ6NTE3M2ViNzAtNjMxOC00YzA3LTgwYzktY2VlNjkyMTdjZGE2",
        input: {
            gateway: "significa.payments.postfinance",
        }
    ) {
        payment {
            id
        }
    } 
}
```

4. Call `completeCheckout` mutation with the following payment data, to get the PostFinance payment url.

```graphql
mutation checkoutComplete {
  checkoutComplete(
    id: "Q2hlY2tvdXQ6NTE3M2ViNzAtNjMxOC00YzA3LTgwYzktY2VlNjkyMTdjZGE2",
    paymentData:"{\"successUrl\": \"https://example.com/success?checkout_id=Q2hlY2tvdXQ6NTE3M2ViNzAtNjMxOC00YzA3LTgwYzktY2VlNjkyMTdjZGE2\", \"failUrl\": \"https://example.com/fail?checkout_id=Q2hlY2tvdXQ6NTE3M2ViNzAtNjMxOC00YzA3LTgwYzktY2VlNjkyMTdjZGE2\"}"
  ) {
    confirmationNeeded
    confirmationData
  }
}

# Response
{
  "data": {
    "checkoutComplete": {
      "confirmationNeeded": true,
      "confirmationData": "{\"payment_page_url\": \"https://checkout.postfinance.ch/s/00000/payment/transaction/pay/10000000?securityToken=example-00000\"}",
    }
  }
}
```

5. Finally call `checkoutComplete` to confirm the payment was captured successfully.

```graphql
mutation checkoutComplete {
  checkoutComplete(
    id: "Q2hlY2tvdXQ6NTE3M2ViNzAtNjMxOC00YzA3LTgwYzktY2VlNjkyMTdjZGE2",
  ) {
    confirmationNeeded
    confirmationData
  }
}
```