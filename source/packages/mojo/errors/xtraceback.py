"""
.. module:: xtraceback
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains functions for enhancing and formatting exceptions and
               common exception types not provided by python.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []


from typing import Any, Dict, List, Optional

from types import ModuleType, CodeType

import inspect
import os
import re
import traceback

from collections import OrderedDict

from dataclasses import dataclass



ARG_ERROR = "<error>"

DECORATOR_EXPR = re.compile(r"^[\s]*@[\D\w]{1}[\d\w]*")

MEMBER_TRACE_POLICY = "__traceback_format_policy__"


class TracebackFormatPolicy:
    Brief = "Brief"
    Full = "Full"
    Hide = "Hide"

VALID_MEMBER_TRACE_POLICY = [
    TracebackFormatPolicy.Brief,
    TracebackFormatPolicy.Full,
    TracebackFormatPolicy.Hide
]



class TRACEBACK_CONFIG:
    TRACEBACK_POLICY_OVERRIDE = None
    TRACEBACK_MAX_FULL_DISPLAY = 5
    TRACEBACK_EXPAND_FIRST_N = 1


@dataclass
class FrameDetail:
    name: str
    line_no: str
    line_code: str
    filename: str

    co_module: ModuleType
    co_code: CodeType
    
    args: Dict[str, Any]

    first_line: Optional[int] = None
    last_line: Optional[int] = None
    code_lines: Optional[List[str]] = None


@dataclass
class OriginDetail:
    file: str
    lineno: int
    scope: str


@dataclass
class TraceDetail:
    origin: OriginDetail
    call: str
    code: List[str]
    context: Dict[str, List[str]]

@dataclass
class TracebackDetail:
    extype: str
    exargs: List[str]
    traces: List[TraceDetail]


def is_field(candidate: Any) -> bool:
    """
        Determines if a object member is a field.
    """

    if inspect.ismodule(candidate):
        return False
    if inspect.isclass(candidate):
        return False
    if inspect.isfunction(candidate):
        return False
    if inspect.isgeneratorfunction(candidate):
        return False
    if inspect.isgenerator(candidate):
        return False
    if inspect.iscoroutinefunction(candidate):
        return False
    if inspect.iscoroutine(candidate):
        return False
    if inspect.isasyncgenfunction(candidate):
        return False
    if inspect.isasyncgen(candidate):
        return False
    if inspect.istraceback(candidate):
        return False
    if inspect.isframe(candidate):
        return False
    if inspect.iscode(candidate):
        return False
    if inspect.isbuiltin(candidate):
        return False
    if inspect.isroutine(candidate):
        return False
    if inspect.isabstract(candidate):
        return False
    if inspect.ismethoddescriptor(candidate):
        return False
    if inspect.isdatadescriptor(candidate):
        return False
    if inspect.isgetsetdescriptor(candidate):
        return False
    if inspect.ismemberdescriptor(candidate):
        return False

    return True


def split_and_indent_lines(msg: str, level: int, indent: int=4, pre_strip_leading: bool=True) -> List[str]:
    """
        Takes a string and splits it into multiple lines, then indents each line
        to the specified level using 'indent' spaces for each level.

        :param msg: The text content to split into lines and then indent.
        :param level: The integer level number to indent to.
        :param indent: The number of spaces to indent for each level.
        :param pre_strip_leading: Strip any leading whitesspace before indenting the lines.

        :returns: The indenting lines
    """

    # Split msg into lines keeping the line endings
    msglines = msg.splitlines(False)

    prestrip_len = len(msg)
    if pre_strip_leading:
        for nxtline in msglines:
            stripped = nxtline.lstrip()
            striplen = len(nxtline) - len(stripped)
            if striplen < prestrip_len:
                prestrip_len = striplen

    pfx = " " * (level * indent)

    indented = None
    if pre_strip_leading and prestrip_len > 0:
        indented = [pfx + nxtline[prestrip_len:] for nxtline in msglines]
    else:
        indented = [pfx + nxtline for nxtline in msglines]

    return indented


class EnhancedErrorMixIn:
    def __init__(self, *args, **kwargs):
        self._contexts: Dict[str, Dict[str, str]] = {}
        return

    @property
    def contexts(self) -> Dict[str, Dict[str, str]]:
        return self._contexts

    def add_context(self, content: str, label: str = "CONTEXT") -> None:
        """
            Adds context to an exception and associates it with the function context
            on the stack.
        """
        caller_stack = inspect.stack()[2]
        caller_func_name = caller_stack.frame.f_code.co_name

        self._contexts[caller_func_name] = {
            "label": label,
            "content": content
        }

        return


def collect_stack_frames(calling_frame, ex_inst) -> List[FrameDetail]:

    tb_code = None
    tb_lineno = None

    context_frames = []

    for tb_frame, tb_lineno in traceback.walk_stack(calling_frame):
        context_frames.insert(0, (tb_frame, tb_lineno))
        if tb_frame.f_code.co_name == '<module>':
            break 

    context_frames.pop()

    traceback_frames = []

    for tb_frame, tb_lineno in traceback.walk_tb(ex_inst.__traceback__):
        traceback_frames.append((tb_frame, tb_lineno))

    full_stack_frames = context_frames + traceback_frames
    full_stack_frames.reverse()

    frame_details_list = []

    for tb_frame, tb_lineno in full_stack_frames:
        tb_code: CodeType = tb_frame.f_code
        co_filename: str = tb_code.co_filename
        co_name: str = tb_code.co_name
        co_arg_names = tb_code.co_varnames[:tb_code.co_argcount]
        co_argcount = tb_code.co_argcount
        co_locals = tb_frame.f_locals
        co_module: ModuleType = inspect.getmodule(tb_code)
        
        code_args = OrderedDict()
        for argidx in range(0, co_argcount):
            argname = co_arg_names[argidx]
            # We cannot count on argname always being present in co_locals at the
            # time we might be processing an exception.  It could be that it has
            # already been cleaned up because it is no longer used.
            if argname in co_locals:
                argval = co_locals[argname]
                code_args[argname] = argval
            else:
                code_args[argname] = "<not found>"

        code_lines = None
        code_startline = None
        code_lastline = None
        trace_line = "<obfuscated>"

        if co_name != "<module>" and os.path.exists(co_filename) and co_filename.endswith(".py"):
            code_lines, code_startline = inspect.getsourcelines(tb_code)
            if code_lines is not None and len(code_lines) > 0:
                code_lastline = code_startline + len(code_lines)

                fmt_len = len(str(code_lastline))

                fmt_code_lines = []
                for lidx, cline in enumerate(code_lines):
                    lineno = str(code_startline + lidx).zfill(fmt_len)
                    cline = f"{lineno}: {cline.rstrip()}"
                    fmt_code_lines.append(cline)
                
                trace_line_index = tb_lineno - code_startline
                trace_line = code_lines[trace_line_index].strip()

        fdetail = FrameDetail(co_name, tb_lineno, trace_line, co_filename, co_module, tb_code, code_args, code_startline, code_lastline, fmt_code_lines)
        frame_details_list.append(fdetail)

    return frame_details_list


def create_traceback_detail(ex_inst: BaseException) -> TracebackDetail:

    max_full_display = TRACEBACK_CONFIG.TRACEBACK_MAX_FULL_DISPLAY
    expand_first_n = TRACEBACK_CONFIG.TRACEBACK_EXPAND_FIRST_N

    etypename = type(ex_inst).__name__
    eargs = [repr(a) for a in ex_inst.args]
    etraces = []

    calling_frame = inspect.currentframe().f_back

    stack_frames = collect_stack_frames(calling_frame, ex_inst)

    for frame in stack_frames:
        co_module = frame.co_module

        co_format_policy = TracebackFormatPolicy.Brief
        if expand_first_n > 0 and max_full_display > 0:
            co_format_policy = TracebackFormatPolicy.Full

        if TRACEBACK_CONFIG.TRACEBACK_POLICY_OVERRIDE is None:
            if co_module is not None and hasattr(co_module, MEMBER_TRACE_POLICY):
                cand_format_policy = getattr(co_module, MEMBER_TRACE_POLICY)
                if cand_format_policy in VALID_MEMBER_TRACE_POLICY:
                    co_format_policy = cand_format_policy
        else:
            co_format_policy = TRACEBACK_CONFIG.TRACEBACK_POLICY_OVERRIDE

        ntorigin = OriginDetail(file=frame.filename, lineno=frame.line_no, scope=frame.name)

        nt_context = None
        if hasattr(ex_inst, "context") and frame.name in ex_inst.context:
            nt_context = ex_inst.context[frame.name]

        rep_args_parts = []
        for aname, aval in frame.args.items():
            arep = ARG_ERROR

            try:
                if hasattr(aval, "moniker"):
                    arep = aval.moniker
                else:
                    try:
                        arep = repr(aval)
                    except:
                        arep = f"<{type(aval)}>"
            except:
                # We might be trying to handle a remote type or something we
                # cannot even talk to any more.  If so, just leave the representation
                # as an error
                pass

            apart = f"{aname}={arep}"
            rep_args_parts.append(apart)

        rep_args = ", ".join(rep_args_parts)

        ntcall = f"{frame.name}({rep_args})"
        ntcode = []

        if co_format_policy == TracebackFormatPolicy.Full:
            if frame.code_lines is not None:
                ntcode = frame.code_lines

                max_full_display -= 1
                expand_first_n -= 1


        nttrace = TraceDetail(origin=ntorigin, call=ntcall, code=ntcode, context=nt_context)
        etraces.append(nttrace)

    tb_detail = TracebackDetail(extype=etypename, exargs=eargs, traces=etraces)

    return tb_detail


def enhance_exception(xcpt: BaseException, content, label="CONTEXT") -> None:
    """
        Allows for the enhancing of exceptions.
    """

    # EnhancedErrorMixIn just uses Duck typing so it should be safe to dynamically
    # append any exception that does not already inherit include EnhancedErrorMixIn
    # in its base clases list.
    xcpt_type = type(xcpt)

    if EnhancedErrorMixIn not in xcpt_type.__bases__:
        xcpt_type.__bases__ += (EnhancedErrorMixIn,)

    enh_xcpt: EnhancedErrorMixIn = xcpt

    if not hasattr(xcpt, "_context"):
        setattr(enh_xcpt, "_context", {})

    enh_xcpt.add_context(content, label=label)

    return


def format_exc_lines():
    """
        Gets a 'format_exc' result and splits it into mutliple lines.
    """
    rtn_lines = traceback.format_exc().splitlines()
    return rtn_lines


def format_exception(ex_inst: BaseException):

    tbdetail = create_traceback_detail(ex_inst)

    exmsg_lines = format_traceback_detail(tbdetail)

    return exmsg_lines


def format_traceback_detail(tbdetail: TracebackDetail) -> List[str]:
    
    detail_lines = [
        f"{tbdetail.extype}: {','.join(tbdetail.exargs)}",
        "Traceback (most recent call first):"
    ]

    ntrace: TraceDetail
    for ntrace in tbdetail.traces:

        detail_lines.append(f"  File {ntrace.origin.file}, line {ntrace.origin.lineno}, in {ntrace.origin.scope}")
        
        if len(ntrace.call) > 0:
            detail_lines.append(f"    Call {ntrace.call}")

            if len(ntrace.code) > 0:
                detail_lines.append("")

                for nline in ntrace.code:
                    detail_lines.append(f"    {nline}")

        detail_lines.append("")
    
    return detail_lines


