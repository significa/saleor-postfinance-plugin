from setuptools import setup

setup(
    name = "saleor-postfinance-plugin",
    version="0.0.1",
    description="Saleor PostFinance gateway plugin.",
    packages=['saleor-postfinance-plugin'],
    install_requires=["postfinancecheckout==3.1.1"],
    entry_points={
        'saleor.plugins': [
            'saleor-postfinance-plugin = saleor-postfinance-plugin.plugin:PostFinanceGatewayPlugin',
        ]
    }

)
