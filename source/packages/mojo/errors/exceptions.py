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

class SemanticError(BaseException):
    """
        The base error object for errors that indicate that there is an issue with
        a piece of automation code and with the way the Automation Kit code is being
        utilized.
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



class HttpBadRequestError(HTTPException):
    """
        Raised when the HTTPStatus.400 status code is received.
    """

class HttpUnAuthorizedError(HTTPException):
    """
        Raised when the HTTPStatus.401 status code is received.
    """

class HttpPaymentRequiredError(HTTPException):
    """
        Raised when the HTTPStatus.402 status code is received.
    """

class HttpForbiddenError(HTTPException):
    """
        Raised when the HTTPStatus.403 status code is received.
    """

class HttpNotFoundError(HTTPException):
    """
        Raised when the HTTPStatus.404 status code is received.
    """

class HttpMethodNotAllowedError(HTTPException):
    """
        Raised when the HTTPStatus.405 status code is received.
    """

class HttpNotAcceptableError(HTTPException):
    """
        Raised when the HTTPStatus.406 status code is received.
    """

class HttpProxyAuthenticationRequiredError(HTTPException):
    """
        Raised when the HTTPStatus.407 status code is received.
    """

class HttpRequestTimeoutError(HTTPException):
    """
        Raised when the HTTPStatus.408 status code is received.
    """


class HttpConflictError(HTTPException):
    """
        Raised when the HTTPStatus.409 status code is received.
    """


class HttpGoneError(HTTPException):
    """
        Raised when the HTTPStatus.410 status code is received.
    """


class HttpLengthRequiredError(HTTPException):
    """
        Raised when the HTTPStatus.411 status code is received.
    """

class HttpPreConditionFailedError(HTTPException):
    """
        Raised when the HTTPStatus.412 status code is received.
    """

