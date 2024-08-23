"""
.. module:: exceptions
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains exceptions not provided by the standard python libraries.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []


from http.client import HTTPException


class AbstractMethodError(RuntimeError):
    """
        This error is raised when an abstract method has been called.
    """


class CancelledError(RuntimeError):
    """
        This error indicates that a operation or run is being cancelled.
    """


class CommandError(RuntimeError):
    """
        This error is the base error for command results errors.
    """
    def __init__(self, message, status, stdout, stderr, *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.status = status
        self.stdout = stdout
        self.stderr = stderr
        return


class CheckinError(RuntimeError):
    """
        This error is raised when an error occurs during the checking in of a resource.
    """

class CheckoutError(RuntimeError):
    """
        This error is raised when an error occurs during the checkout of a resource.
    """

class ConfigurationError(BaseException):
    """
        The base error object for errors that indicate that there is an issue related
        to improper configuration.
    """

class HaltError(RuntimeError):
    """
        This error is raised when a descendant flow control context encounters an issue and exits asking
        the parent flow control to halt its progress.
    """

class InvalidConfigurationError(ConfigurationError):
    """
        This error is raised when an IntegrationCoupling object has been passed invalid configuration parameters.
    """

class LooperError(RuntimeError):
    """
        This error is raised when an error occurs with the use of the :class:`LooperPool` or
        :class:`Looper` objects.
    """

class LooperQueueShutdownError(LooperError):
    """
        This error is raised when work is being queued on a :class:`LooperQueue` thaat has
        been shutdown and when a worker thread is attempting to wait for work on an empty
        queue.
    """

class MissingConfigurationError(ConfigurationError):
    """
        This error is raised when an IntegrationCoupling object is missing required configuration parameters.
    """


class NotOverloadedError(RuntimeError):
    """
        This error is raised when a method that must be overloaded has not been overridden.
    """

class NotSupportedError(RuntimeError):
    """
        This error is raised when a method that must be overloaded has not been overridden.
    """

class PublishError(RuntimeError):
    """
        This error is raised when the publishing of an artifact fails.
    """

class SemanticError(BaseException):
    """
        The base error object for errors that indicate that there is an issue with
        a piece of automation code and with the way the Automation Kit code is being
        utilized.
    """

class SkipError(RuntimeError):
    """
        This error is raised when a descendant flow control context, such as a testcase, wishes to exit indicating
        that its execution is being skipped.
    """

class TaskingCancelled(CancelledError):
    """
        The exception that is raised with a tasking is cancelled.
    """

class TaskingGroupAssertionError(AssertionError):
    """
        The exception that is raised when the only failures in a group of
        taskings are of type AssertionError.
    """

class TaskingGroupCancelled(CancelledError):
    """
        The exception that is raised when any of the taskings in a tasking
        group, completed with a cancelled error.
    """

class TaskingGroupRuntimeError(RuntimeError):
    """
        The exception that is raised when any of the taskings in a tasking group
        completed with a NON Assertion error or NON Cancellation error.
    """

class UnknownParameterError(RuntimeError):
    """
        This error is raised when the test framework encounters a
        reference to a well-known parameter that cannot be resolved.
    """

# ===============================================================
# Sorted by status code
# ===============================================================

# --------------- 3xx Status Code Errors-----------------

class HttpResponse3xxError(HTTPException):
    """
        The base exception type for all the 3xx class of HTTP exceptions.
    """

class HttpRedirectMultipleChoicesError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.300 status code is received and not handled.
    """

class HttpRedirectMovedPermanentlyError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.301 status code is received and not handled.
    """
class HttpRedirectMovedTemporarilyError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.302 status code is received and not handled.
    """

class HttpRedirectSeeOtherError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.303 status code is received and not handled.
    """

class HttpRedirectNotModifiedError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.304 status code is received and not handled.
    """

class HttpRedirectUseProxyError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.305 status code is received and not handled.
    """

class HttpRedirectSwitchProxyError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.306 status code is received and not handled.
    """

class HttpRedirectTemporaryError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.307 status code is received and not handled.
    """

class HttpRedirectPermanentError(HttpResponse3xxError):
    """
        Raise when the HTTPStatus.308 status code is received and not handled.
    """

# --------------- 4xx Status Code Errors-----------------

class HttpResponse4xxError(HTTPException):
    """
        The base exception type for all the 3xx class of HTTP exceptions.
    """

class HttpBadRequestError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.400 status code is received.
    """

class HttpUnAuthorizedError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.401 status code is received.
    """

class HttpPaymentRequiredError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.402 status code is received.
    """

class HttpForbiddenError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.403 status code is received.
    """

class HttpNotFoundError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.404 status code is received.
    """

class HttpMethodNotAllowedError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.405 status code is received.
    """

class HttpNotAcceptableError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.406 status code is received.
    """

class HttpProxyAuthenticationRequiredError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.407 status code is received.
    """

class HttpRequestTimeoutError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.408 status code is received.
    """

class HttpConflictError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.409 status code is received.
    """

class HttpGoneError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.410 status code is received.
    """

class HttpLengthRequiredError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.411 status code is received.
    """

class HttpPreConditionFailedError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.412 status code is received.
    """

class HttpPayloadTooLargeError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.413 status code is received.
    """

class HttpUriTooLongError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.414 status code is received.
    """

class HttpUnSupportedMediaTypeError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.415 status code is received.
    """

class HttpRangeNotSatisfiableError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.416 status code is received.
    """

class HttpExpectationFailedError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.417 status code is received.
    """

class HttpImATeapotError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.418 status code is received.
    """

class HttpMisdirectedRequestError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.421 status code is received.
    """

class HttpUnprocessableContentError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.422 status code is received.
    """

class HttpLockedError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.423 status code is received.
    """

class HttpFailedDependencyError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.424 status code is received.
    """

class HttpTooEarlyError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.425 status code is received.
    """

class HttpUpgradeRequiredError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.426 status code is received.
    """

class HttpPreconditionRequiredError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.428 status code is received.
    """

class HttpTooManyRequestsError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.429 status code is received.
    """

class HttpHeaderFieldsTooLargeError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.431 status code is received.
    """

class HttpUnavailableForLegalReasonsError(HttpResponse4xxError):
    """
        Raised when the HTTPStatus.451 status code is received.
    """

# --------------- 5xx Status Code Errors-----------------


class HttpResponse5xxError(HTTPException):
    """
        The base exception type for all the 5xx class of HTTP exceptions.
    """

class HttpInternalServerError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.500 status code is received.
    """

class HttpNotImplementedError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.501 status code is received.
    """

class HttpBadGatewayError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.502 status code is received.
    """

class HttpServiceUnavailableError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.503 status code is received.
    """

class HttpGatewayTimeoutError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.504 status code is received.
    """

class HttpVersionNotSupportedError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.505 status code is received.
    """

class HttpCircularReferenceError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.506 status code is received.
    """

class HttpInsufficientStorageError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.507 status code is received.
    """

class HttpLoopDetectedError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.508 status code is received.
    """

class HttpNotExtendedError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.510 status code is received.
    """

class HttpNetworkAuthenticationRequiredError(HttpResponse5xxError):
    """
        Raised when the HTTPStatus.511 status code is received.
    """

class HttpOtherCodeError(HTTPException):
    """
        Can be raised when a HTTP Status code is recieved that is of an unknow value.
    """