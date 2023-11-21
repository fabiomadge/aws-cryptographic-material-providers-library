# Code generated by smithy-python-codegen DO NOT EDIT.

from .config import Config, Plugin, smithy_config_to_dafny_config
from smithy_python.interfaces.retries import RetryStrategy
from smithy_python.exceptions import SmithyRetryException
from .dafnyImplInterface import DafnyImplInterface

def set_config_impl(config: Config):
    '''
    Set the Dafny-compiled implementation in the Smithy-Python client Config
    and load our custom NoRetriesStrategy.
    '''
    from software_amazon_cryptography_materialproviders_internaldafny import MaterialProvidersClient
    config.dafnyImplInterface = DafnyImplInterface()
    config.dafnyImplInterface.impl = MaterialProvidersClient()
    config.dafnyImplInterface.impl.ctor__(smithy_config_to_dafny_config(config))
    config.retry_strategy = NoRetriesStrategy()

class ZeroRetryDelayToken:
    '''
    Placeholder class required by Smithy-Python client implementation.
    Do not wait to retry.
    '''
    retry_delay = 0

class NoRetriesStrategy(RetryStrategy):
    '''
    Placeholder class required by Smithy-Python client implementation.
    Do not retry calling Dafny code.
    '''
    def acquire_initial_retry_token(self):
        return ZeroRetryDelayToken()

    def refresh_retry_token_for_retry(self, token_to_renew, error_info):
        # Do not retry
        raise SmithyRetryException()
