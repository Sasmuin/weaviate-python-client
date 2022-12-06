import warnings
from typing import Optional

import weaviate.version as version


class _Warnings:
    @staticmethod
    def auth_with_anon_weaviate():
        warnings.warn(
            message="""Auth001: The client was configured to use authentication, but weaviate is configured without
                    authentication. Are you sure this is correct?""",
            category=UserWarning,
            stacklevel=1,
        )

    @staticmethod
    def auth_no_refresh_token(auth_len: Optional[int] = None):
        if auth_len is not None:
            msg = f"The current access token is only valid for {auth_len}s."
        else:
            msg = "Also, no expiration time was given."

        warnings.warn(
            message=f"""Auth002: The token returned from you identity provider does not contain a refresh token. {msg}

            Access to your weaviate instance is not possible after expiration and this client will return an
            authentication exception.

            Things to try:
            - You might need to enable refresh tokens in the settings of your authentication provider
            - You might need to send the correct scope. For some providers it needs to include "offline_access"
            """,
            category=UserWarning,
            stacklevel=1,
        )

    @staticmethod
    def auth_negative_expiration_time(expires_in: int, refresh_expires_in: Optional[int]):
        msg = """Auth003:"""
        if expires_in < 0:
            msg += f"access token expiration time is negative: {expires_in}."
        if refresh_expires_in < 0:
            msg += f"refresh token expiration time is negative: {refresh_expires_in}."

        warnings.warn(
            message=msg,
            category=UserWarning,
            stacklevel=1,
        )

    @staticmethod
    def weaviate_server_older_than_1_14(server_version: str):
        warnings.warn(
            message=f"""Dep001: You are using the Weaviate Python Client version {version.__version__} which supports
            changes and features of Weaviate >=1.14.x, but you are connected to Weaviate {server_version}.
            If you want to make use of these new changes/features using this Python Client version, upgrade your
            Weaviate instance.""",
            category=DeprecationWarning,
            stacklevel=1,
        )

    @staticmethod
    def manual_batching():
        warnings.warn(
            message="""Dep002: You are batching manually. This means you are NOT using the client's built-in
            multi-threading. Setting `batch_size` in `client.batch.configure()`  to an int value will enabled automatic
            batching. See:
            https://weaviate.io/developers/weaviate/current/restful-api-references/batch.html#example-request-1""",
            category=DeprecationWarning,
            stacklevel=1,
        )
