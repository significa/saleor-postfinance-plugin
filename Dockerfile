ARG SALEOR_VERSION=latest

FROM ghcr.io/saleor/saleor:${SALEOR_VERSION}

COPY ./saleor-postfinance-plugin /app/saleor-postfinance-plugin

RUN cd /app/saleor && pip install -e /app/saleor-postfinance-plugin

RUN  sed -i 's/^EXTERNAL_PLUGINS = \[\]/EXTERNAL_PLUGINS = \[\"saleor-postfinance-plugin.plugin.PostFinanceGatewayPlugin\"\]/g' /app/saleor/settings.py
