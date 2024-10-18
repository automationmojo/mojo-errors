
from typing import Optional

import os

from http.client import HTTPException

from mojo.errors import exceptions


STATUS_TO_EXCEPTION_TABLE = {
    300: exceptions.HttpRedirectMultipleChoicesError,
    301: exceptions.HttpRedirectMovedPermanentlyError,
    302: exceptions.HttpRedirectMovedTemporarilyError,
    303: exceptions.HttpRedirectSeeOtherError,
    304: exceptions.HttpRedirectNotModifiedError,
    305: exceptions.HttpRedirectUseProxyError,
    306: exceptions.HttpRedirectSwitchProxyError,
    307: exceptions.HttpRedirectTemporaryError,
    308: exceptions.HttpRedirectPermanentError,
    400: exceptions.HttpBadRequestError,
    401: exceptions.HttpUnAuthorizedError,
    402: exceptions.HttpPaymentRequiredError,
    403: exceptions.HttpForbiddenError,
    404: exceptions.HttpNotFoundError,
    405: exceptions.HttpMethodNotAllowedError,
    406: exceptions.HttpNotAcceptableError,
    407: exceptions.HttpProxyAuthenticationRequiredError,
    408: exceptions.HttpRequestTimeoutError,
    409: exceptions.HttpConflictError,
    410: exceptions.HttpGoneError,
    411: exceptions.HttpLengthRequiredError,
    412: exceptions.HttpPreconditionRequiredError,
    413: exceptions.HttpPayloadTooLargeError,
    414: exceptions.HttpUriTooLongError,
    415: exceptions.HttpUnSupportedMediaTypeError,
    416: exceptions.HttpRangeNotSatisfiableError,
    417: exceptions.HttpExpectationFailedError,
    418: exceptions.HttpImATeapotError,
    421: exceptions.HttpMisdirectedRequestError,
    422: exceptions.HttpUnprocessableContentError,
    423: exceptions.HttpLockedError,
    424: exceptions.HttpFailedDependencyError,
    425: exceptions.HttpTooEarlyError,
    426: exceptions.HttpUpgradeRequiredError,
    428: exceptions.HttpPreconditionRequiredError,
    429: exceptions.HttpTooManyRequestsError,
    431: exceptions.HttpHeaderFieldsTooLargeError,
    451: exceptions.HttpUnavailableForLegalReasonsError,
    500: exceptions.HttpInternalServerError,
    501: exceptions.HttpNotImplementedError,
    502: exceptions.HttpBadGatewayError,
    503: exceptions.HttpServiceUnavailableError,
    504: exceptions.HttpGatewayTimeoutError,
    505: exceptions.HttpVersionNotSupportedError,
    506: exceptions.HttpCircularReferenceError,
    507: exceptions.HttpInsufficientStorageError,
    508: exceptions.HttpLoopDetectedError,
    510: exceptions.HttpNotExtendedError,
    511: exceptions.HttpNetworkAuthenticationRequiredError
}


def format_http_error_message(resp_code: int, resp_msg: str, url: Optional[str] = None, context: Optional[str] = None) -> str:
    
    err_msg_lines = [
        f"HTTP Error: code={resp_code} message={resp_msg}."
    ]

    if url is not None:
        err_msg_lines.append(f"URL: {url}")

    if context is not None:
        err_msg_lines.append(f"CONTEXT: {context}")
    
    err_msg = os.linesep.join(err_msg_lines)
    
    return err_msg


def raise_for_http_status(resp_code: int, resp_msg: str,  url: Optional[str] = None, context: Optional[str] = None) -> None:

    if resp_code >= 300:
        if resp_code in STATUS_TO_EXCEPTION_TABLE:
            error_type = STATUS_TO_EXCEPTION_TABLE[resp_code]
        elif resp_code >= 300 and resp_code <= 399:
            error_type = exceptions.HttpResponse3xxError
        elif resp_code >= 400 and resp_code <= 499:
            error_type = exceptions.HttpResponse4xxError
        elif resp_code >= 500 and resp_code <= 599:
            error_type = exceptions.HttpResponse5xxError
        else:
            error_type = HTTPException

        msg = format_http_error_message(resp_code, resp_msg, url=url, context=context)

        raise error_type(msg)

    return