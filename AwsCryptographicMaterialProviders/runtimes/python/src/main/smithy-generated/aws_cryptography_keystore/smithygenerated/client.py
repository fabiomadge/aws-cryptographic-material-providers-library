# Code generated by smithy-python-codegen DO NOT EDIT.

from asyncio import sleep
from copy import deepcopy
from typing import Awaitable, Callable, TypeVar, cast

from .dafny_protocol import DafnyRequest, DafnyResponse
from .plugin import set_config_impl
from smithy_python.exceptions import SmithyRetryException
from smithy_python.interfaces.interceptor import Interceptor, InterceptorContext
from smithy_python.interfaces.retries import RetryErrorInfo, RetryErrorType

from ..config import Config, Plugin
from ..deserialize import (
    _deserialize_create_key,
    _deserialize_create_key_store,
    _deserialize_decrypt_materials,
    _deserialize_delete_cache_entry,
    _deserialize_get_active_branch_key,
    _deserialize_get_beacon_key,
    _deserialize_get_branch_key_id,
    _deserialize_get_branch_key_version,
    _deserialize_get_cache_entry,
    _deserialize_get_client,
    _deserialize_get_encryption_materials,
    _deserialize_get_key_store_info,
    _deserialize_on_decrypt,
    _deserialize_on_encrypt,
    _deserialize_put_cache_entry,
    _deserialize_update_usage_metadata,
    _deserialize_version_key,
)
from ..errors import ServiceError
from ..models import (
    CreateKeyInput,
    CreateKeyOutput,
    CreateKeyStoreInput,
    CreateKeyStoreOutput,
    DecryptMaterialsInput,
    DecryptMaterialsOutput,
    DeleteCacheEntryInput,
    GetActiveBranchKeyInput,
    GetActiveBranchKeyOutput,
    GetBeaconKeyInput,
    GetBeaconKeyOutput,
    GetBranchKeyIdInput,
    GetBranchKeyIdOutput,
    GetBranchKeyVersionInput,
    GetBranchKeyVersionOutput,
    GetCacheEntryInput,
    GetCacheEntryOutput,
    GetClientInput,
    GetClientOutput,
    GetEncryptionMaterialsInput,
    GetEncryptionMaterialsOutput,
    GetKeyStoreInfoOutput,
    OnDecryptInput,
    OnDecryptOutput,
    OnEncryptInput,
    OnEncryptOutput,
    PutCacheEntryInput,
    Unit,
    UpdateUsageMetadataInput,
    VersionKeyInput,
    VersionKeyOutput,
)
from ..serialize import (
    _serialize_create_key,
    _serialize_create_key_store,
    _serialize_decrypt_materials,
    _serialize_delete_cache_entry,
    _serialize_get_active_branch_key,
    _serialize_get_beacon_key,
    _serialize_get_branch_key_id,
    _serialize_get_branch_key_version,
    _serialize_get_cache_entry,
    _serialize_get_client,
    _serialize_get_encryption_materials,
    _serialize_get_key_store_info,
    _serialize_on_decrypt,
    _serialize_on_encrypt,
    _serialize_put_cache_entry,
    _serialize_update_usage_metadata,
    _serialize_version_key,
)


Input = TypeVar("Input")
Output = TypeVar("Output")

class KeyStore:
    """Client for KeyStore

    :param config: Optional configuration for the client. Here you can set things like the
    endpoint for HTTP services or auth credentials.

    :param plugins: A list of callables that modify the configuration dynamically. These
    can be used to set defaults, for example.
    """
    def __init__(self, config: Config | None = None, plugins: list[Plugin] | None = None):
        self._config = config or Config()

        client_plugins: list[Plugin] = [
            set_config_impl,
        ]
        if plugins:
            client_plugins.extend(plugins)

        for plugin in client_plugins:
            plugin(self._config)

    async def create_key(self, input: CreateKeyInput, plugins: list[Plugin] | None = None):
        """Invokes the CreateKey operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_create_key,
            deserialize=_deserialize_create_key,
            config=self._config,
            operation_name="CreateKey",
        )

    async def create_key_store(self, input: CreateKeyStoreInput, plugins: list[Plugin] | None = None):
        """Invokes the CreateKeyStore operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_create_key_store,
            deserialize=_deserialize_create_key_store,
            config=self._config,
            operation_name="CreateKeyStore",
        )

    async def get_active_branch_key(self, input: GetActiveBranchKeyInput, plugins: list[Plugin] | None = None):
        """Invokes the GetActiveBranchKey operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_active_branch_key,
            deserialize=_deserialize_get_active_branch_key,
            config=self._config,
            operation_name="GetActiveBranchKey",
        )

    async def get_beacon_key(self, input: GetBeaconKeyInput, plugins: list[Plugin] | None = None):
        """Invokes the GetBeaconKey operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_beacon_key,
            deserialize=_deserialize_get_beacon_key,
            config=self._config,
            operation_name="GetBeaconKey",
        )

    async def get_branch_key_version(self, input: GetBranchKeyVersionInput, plugins: list[Plugin] | None = None):
        """Invokes the GetBranchKeyVersion operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_branch_key_version,
            deserialize=_deserialize_get_branch_key_version,
            config=self._config,
            operation_name="GetBranchKeyVersion",
        )

    async def get_key_store_info(self, input: Unit, plugins: list[Plugin] | None = None):
        """Invokes the GetKeyStoreInfo operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_key_store_info,
            deserialize=_deserialize_get_key_store_info,
            config=self._config,
            operation_name="GetKeyStoreInfo",
        )

    async def version_key(self, input: VersionKeyInput, plugins: list[Plugin] | None = None):
        """Invokes the VersionKey operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_version_key,
            deserialize=_deserialize_version_key,
            config=self._config,
            operation_name="VersionKey",
        )

    async def decrypt_materials(self, input: DecryptMaterialsInput, plugins: list[Plugin] | None = None):
        """Invokes the DecryptMaterials operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_decrypt_materials,
            deserialize=_deserialize_decrypt_materials,
            config=self._config,
            operation_name="DecryptMaterials",
        )

    async def delete_cache_entry(self, input: DeleteCacheEntryInput, plugins: list[Plugin] | None = None):
        """Invokes the DeleteCacheEntry operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_delete_cache_entry,
            deserialize=_deserialize_delete_cache_entry,
            config=self._config,
            operation_name="DeleteCacheEntry",
        )

    async def get_branch_key_id(self, input: GetBranchKeyIdInput, plugins: list[Plugin] | None = None):
        """Invokes the GetBranchKeyId operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_branch_key_id,
            deserialize=_deserialize_get_branch_key_id,
            config=self._config,
            operation_name="GetBranchKeyId",
        )

    async def get_cache_entry(self, input: GetCacheEntryInput, plugins: list[Plugin] | None = None):
        """Invokes the GetCacheEntry operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_cache_entry,
            deserialize=_deserialize_get_cache_entry,
            config=self._config,
            operation_name="GetCacheEntry",
        )

    async def get_client(self, input: GetClientInput, plugins: list[Plugin] | None = None):
        """Invokes the GetClient operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_client,
            deserialize=_deserialize_get_client,
            config=self._config,
            operation_name="GetClient",
        )

    async def get_encryption_materials(self, input: GetEncryptionMaterialsInput, plugins: list[Plugin] | None = None):
        """//////////////

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_encryption_materials,
            deserialize=_deserialize_get_encryption_materials,
            config=self._config,
            operation_name="GetEncryptionMaterials",
        )

    async def on_decrypt(self, input: OnDecryptInput, plugins: list[Plugin] | None = None):
        """Invokes the OnDecrypt operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_on_decrypt,
            deserialize=_deserialize_on_decrypt,
            config=self._config,
            operation_name="OnDecrypt",
        )

    async def on_encrypt(self, input: OnEncryptInput, plugins: list[Plugin] | None = None):
        """//////////////////

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_on_encrypt,
            deserialize=_deserialize_on_encrypt,
            config=self._config,
            operation_name="OnEncrypt",
        )

    async def put_cache_entry(self, input: PutCacheEntryInput, plugins: list[Plugin] | None = None):
        """Invokes the PutCacheEntry operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_put_cache_entry,
            deserialize=_deserialize_put_cache_entry,
            config=self._config,
            operation_name="PutCacheEntry",
        )

    async def update_usage_metadata(self, input: UpdateUsageMetadataInput, plugins: list[Plugin] | None = None):
        """Invokes the UpdateUsageMetadata operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_update_usage_metadata,
            deserialize=_deserialize_update_usage_metadata,
            config=self._config,
            operation_name="UpdateUsageMetadata",
        )

    async def _execute_operation(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], Awaitable[DafnyRequest]],
        deserialize: Callable[[DafnyResponse, Config], Awaitable[Output]],
        config: Config,
        operation_name: str,
    ):
        try:
            return await self._handle_execution(
                input, plugins, serialize, deserialize, config, operation_name
            )
        except Exception as e:
            # Make sure every exception that we throw is an instance of ServiceError so
            # customers can reliably catch everything we throw.
            if not isinstance(e, ServiceError):
                raise ServiceError(e) from e
            raise e

    async def _handle_execution(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], Awaitable[DafnyRequest]],
        deserialize: Callable[[DafnyResponse, Config], Awaitable[Output]],
        config: Config,
        operation_name: str,
    ):
        context: InterceptorContext[Input, None, None, None] = InterceptorContext(
            request=input,
            response=None,
            transport_request=None,
            transport_response=None,
        )
        _client_interceptors = config.interceptors
        client_interceptors = cast(
            list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]], _client_interceptors
        )
        interceptors = client_interceptors

        try:
            # Step 1a: Invoke read_before_execution on client-level interceptors
            for interceptor in client_interceptors:
                interceptor.read_before_execution(context)

            # Step 1b: Run operation-level plugins
            config = deepcopy(config)
            for plugin in plugins:
                plugin(config)

            _client_interceptors = config.interceptors
            interceptors = cast(
                list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
                _client_interceptors,
            )

            # Step 1c: Invoke the read_before_execution hooks on newly added
            # interceptors.
            for interceptor in interceptors:
                if interceptor not in client_interceptors:
                    interceptor.read_before_execution(context)

            # Step 2: Invoke the modify_before_serialization hooks
            for interceptor in interceptors:
                context._request = interceptor.modify_before_serialization(context)

            # Step 3: Invoke the read_before_serialization hooks
            for interceptor in interceptors:
                interceptor.read_before_serialization(context)

            # Step 4: Serialize the request
            context_with_transport_request = cast(
                InterceptorContext[Input, None, DafnyRequest, None], context
            )
            context_with_transport_request._transport_request = await serialize(
                context_with_transport_request.request, config
            )

            # Step 5: Invoke read_after_serialization
            for interceptor in interceptors:
                interceptor.read_after_serialization(context_with_transport_request)

            # Step 6: Invoke modify_before_retry_loop
            for interceptor in interceptors:
                context_with_transport_request._transport_request = (
                    interceptor.modify_before_retry_loop(context_with_transport_request)
                )

            # Step 7: Acquire the retry token.
            retry_strategy = config.retry_strategy
            retry_token = retry_strategy.acquire_initial_retry_token()

            while True:
                # Make an attempt, creating a copy of the context so we don't pass
                # around old data.
                context_with_response = await self._handle_attempt(
                    deserialize,
                    interceptors,
                    context_with_transport_request.copy(),
                    config,
                    operation_name,
                )

                # We perform this type-ignored re-assignment because `context` needs
                # to point at the latest context so it can be generically handled
                # later on. This is only an issue here because we've created a copy,
                # so we're no longer simply pointing at the same object in memory
                # with different names and type hints. It is possible to address this
                # without having to fall back to the type ignore, but it would impose
                # unnecessary runtime costs.
                context = context_with_response  # type: ignore

                if isinstance(context_with_response.response, Exception):
                    # Step 7u: Reacquire retry token if the attempt failed
                    try:
                        retry_token = retry_strategy.refresh_retry_token_for_retry(
                            token_to_renew=retry_token,
                            error_info=RetryErrorInfo(
                                # TODO: Determine the error type.
                                error_type=RetryErrorType.CLIENT_ERROR,
                            )
                        )
                    except SmithyRetryException:
                        raise context_with_response.response
                    await sleep(retry_token.retry_delay)
                else:
                    # Step 8: Invoke record_success
                    retry_strategy.record_success(token=retry_token)
                    break
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # At this point, the context's request will have been definitively set, and
        # The response will be set either with the modeled output or an exception. The
        # transport_request and transport_response may be set or None.
        execution_context = cast(
            InterceptorContext[Input, Output, DafnyRequest | None, DafnyResponse | None], context
        )
        return await self._finalize_execution(interceptors, execution_context)

    async def _handle_attempt(
        self,
        deserialize: Callable[[DafnyResponse, Config], Awaitable[Output]],
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, None, DafnyRequest, None],
        config: Config,
        operation_name: str,
    ):
        try:
            # assert config.interceptors is not None
            # Step 7a: Invoke read_before_attempt
            for interceptor in interceptors:
                interceptor.read_before_attempt(context)

            # Step 7g: Invoke modify_before_signing
            for interceptor in interceptors:
                context._transport_request = interceptor.modify_before_signing(context)

            # Step 7h: Invoke read_before_signing
            for interceptor in interceptors:
                interceptor.read_before_signing(context)

            # Step 7j: Invoke read_after_signing
            for interceptor in interceptors:
                interceptor.read_after_signing(context)

            # Step 7k: Invoke modify_before_transmit
            for interceptor in interceptors:
                context._transport_request = interceptor.modify_before_transmit(context)

            # Step 7l: Invoke read_before_transmit
            for interceptor in interceptors:
                interceptor.read_before_transmit(context)

            # Step 7m: Invoke http_client.send
            if config.dafnyImplInterface.impl is None:
                raise Exception("No impl found on the operation config.")

            context_with_response = cast(
                InterceptorContext[Input, None, DafnyRequest, DafnyResponse], context
            )

            context_with_response._transport_response = config.dafnyImplInterface.handle_request(
                input=context_with_response.transport_request
            )

            # Step 7n: Invoke read_after_transmit
            for interceptor in interceptors:
                interceptor.read_after_transmit(context_with_response)

            # Step 7o: Invoke modify_before_deserialization
            for interceptor in interceptors:
                context_with_response._transport_response = (
                    interceptor.modify_before_deserialization(context_with_response)
                )

            # Step 7p: Invoke read_before_deserialization
            for interceptor in interceptors:
                interceptor.read_before_deserialization(context_with_response)

            # Step 7q: deserialize
            context_with_output = cast(
                InterceptorContext[Input, Output, DafnyRequest, DafnyResponse],
                context_with_response,
            )
            context_with_output._response = await deserialize(
                context_with_output._transport_response, config
            )

            # Step 7r: Invoke read_after_deserialization
            for interceptor in interceptors:
                interceptor.read_after_deserialization(context_with_output)
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # At this point, the context's request and transport_request have definitively been set,
        # the response is either set or an exception, and the transport_resposne is either set or
        # None. This will also be true after _finalize_attempt because there is no opportunity
        # there to set the transport_response.
        attempt_context = cast(
            InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None], context
        )
        return await self._finalize_attempt(interceptors, attempt_context)

    async def _finalize_attempt(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, Output, DafnyRequest, DafnyResponse | None],
    ):
        # Step 7s: Invoke modify_before_attempt_completion
        try:
            for interceptor in interceptors:
                context._response = interceptor.modify_before_attempt_completion(
                    context
                )
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # Step 7t: Invoke read_after_attempt
        for interceptor in interceptors:
            try:
                interceptor.read_after_attempt(context)
            except Exception as e:
                if context.response is not None:
                    # config.logger.exception(f"Exception occurred while handling: {context.response}")
                    pass
                context._response = e

        return context

    async def _finalize_execution(
        self,
        interceptors: list[Interceptor[Input, Output, DafnyRequest, DafnyResponse]],
        context: InterceptorContext[Input, Output, DafnyRequest | None, DafnyResponse | None],
    ):
        try:
            # Step 9: Invoke modify_before_completion
            for interceptor in interceptors:
                context._response = interceptor.modify_before_completion(context)

            # Step 10: Invoke trace_probe.dispatch_events
            try:
                pass
            except Exception as e:
                # log and ignore exceptions
                # config.logger.exception(f"Exception occurred while dispatching trace events: {e}")
                pass
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # Step 11: Invoke read_after_execution
        for interceptor in interceptors:
            try:
                interceptor.read_after_execution(context)
            except Exception as e:
                if context.response is not None:
                    # config.logger.exception(f"Exception occurred while handling: {context.response}")
                    pass
                context._response = e

        # Step 12: Return / throw
        if isinstance(context.response, Exception):
            raise context.response

        # We may want to add some aspects of this context to the output types so we can
        # return it to the end-users.
        return context.response
