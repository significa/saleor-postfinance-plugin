FROM ghcr.io/saleor/saleor:3.6.7

RUN pip install -r requirements.txt

RUN  sed -i 's/EXTERNAL_PLUGINS = \[\]/EXTERNAL_PLUGINS = \[\"saleor.payment.gateways.postfinance.plugin.PostFinanceGatewayPlugin\"\]/g' /app/saleor/settings.py

COPY ./postfinance /app/saleor/payment/gateways/postfinance