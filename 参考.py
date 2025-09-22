#!/usr/bin/env python3
"""
自动生成的 MCP 服务器
库: plotly
工具数量: 86
"""

import asyncio
import json
import logging
import sys
from typing import Dict, Any

try:
    import plotly  # type: ignore
except ImportError:
    print("错误: 未安装 plotly 库，请运行: pip install plotly")
    sys.exit(1)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("plotly_mcp_server")

# 工具定义
TOOLS = [
    {
        "name": "plotly_basewidget_BaseFigureWidget_show",
        "description": "Show a figure using either the default renderer(s) or the renderer(s)\nspecified by the renderer argument\nParameters\n----------\nrenderer: str or None (default None)\nA string containing the names of one or more registered renderers\n(separated by '+' characters) or None.  If None, then the default\nrenderers specified in plotly.io.renderers.default are used.\nvalidate: bool (default True)\nTrue if the figure should be validated before being shown,\nFalse otherwise.\nwidth: int or float\nAn integer or float that determines the number of pixels wide the\nplot is. The default is set in plotly.js.\nheight: int or float\nAn integer or float that determines the number of pixels wide the\nplot is. The default is set in plotly.js.\nconfig: dict\nA dict of parameters to configure the figure. The defaults are set\nin plotly.js.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_observe",
        "description": "Setup a handler to be called when a trait changes.\nThis is used to setup dynamic notifications of trait changes.\nParameters\n----------\nhandler : callable\nA callable that is called when a trait changes. Its\nsignature should be ``handler(change)``, where ``change`` is a\ndictionary. The change dictionary at least holds a 'type' key.\n* ``type``: the type of notification.\nOther keys may be passed depending on the value of 'type'. In the\ncase where type is 'change', we also have the following keys:\n* ``owner`` : the HasTraits instance\n* ``old`` : the old value of the modified trait attribute\n* ``new`` : the new value of the modified trait attribute\n* ``name`` : the name of the modified trait attribute.\nnames : list, str, All\nIf names is All, the handler will apply to all traits.  If a list\nof str, handler will apply to all names in the list.  If a\nstr, the handler will apply just to that name.\ntype : str, All (default: 'change')\nThe type of notification to filter by. If equal to All, then all\nnotifications are passed to the observe handler.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "handler": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "names": {
                    "type": "string",
                    "default": "traitlets.All",
                    "description": "类型从默认值推断: Sentinel"
                },
                "type": {
                    "type": "string",
                    "default": "change",
                    "description": "类型从默认值推断: str"
                }
            },
            "required": [
                "handler"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_on_edits_completed",
        "description": "Register a function to be called after all pending trace and layout\nedit operations have completed\nIf there are no pending edit operations then function is called\nimmediately\nParameters\n----------\nfn : callable\nFunction of zero arguments to be called when all pending edit\noperations have completed",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fn": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "fn"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_trait_defaults",
        "description": "Return a trait's default value or a dictionary of them\nNotes\n-----\nDynamically generated default values may\ndepend on the current state of the object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "names": {
                    "type": "string",
                    "description": "类型从参数名推断: names"
                },
                "metadata": {
                    "type": "object",
                    "description": "类型从参数名推断: metadata"
                }
            },
            "required": [
                "names",
                "metadata"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_trace",
        "description": "Add a trace to the figure\nParameters\n----------\ntrace : BaseTraceType or dict\nEither:\n- An instances of a trace classe from the plotly.graph_objs\npackage (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)\n- or a dicts where:\n- The 'type' property specifies the trace type (e.g.\n'scatter', 'bar', 'area', etc.). If the dict has no 'type'\nproperty then 'scatter' is assumed.\n- All remaining properties are passed to the constructor\nof the specified trace type.\nrow : 'all', int or None (default)\nSubplot row index (starting from 1) for the trace to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`.\nIf 'all', addresses all rows in the specified column(s).\ncol : 'all', int or None (default)\nSubplot col index (starting from 1) for the trace to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`.\nIf 'all', addresses all columns in the specified row(s).\nsecondary_y: boolean or None (default None)\nIf True, associate this trace with the secondary y-axis of the\nsubplot at the specified row and col. Only valid if all of the\nfollowing conditions are satisfied:\n* The figure was created using `plotly.subplots.make_subplots`.\n* The row and col arguments are not None\n* The subplot at the specified row and col has type xy\n(which is the default) and secondary_y True.  These\nproperties are specified in the specs argument to\nmake_subplots. See the make_subplots docstring for more info.\n* The trace argument is a 2D cartesian trace\n(scatter, bar, etc.)\nexclude_empty_subplots: boolean\nIf True, the trace will not be added to subplots that don't already\nhave traces.\nReturns\n-------\nBaseFigure\nThe Figure that add_trace was called on\nExamples\n--------\n>>> from plotly import subplots\n>>> import plotly.graph_objs as go\nAdd two Scatter traces to a figure\n>>> fig = go.Figure()\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS\nFigure(...)\nAdd two Scatter traces to vertically stacked subplots\n>>> fig = subplots.make_subplots(rows=2)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1) # doctest: +ELLIPSIS\nFigure(...)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "trace": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "trace"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_pop",
        "description": "Remove the value associated with the specified key and return it\nParameters\n----------\nkey: str\nProperty name\ndflt\nThe default value to return if key was not found in figure\nReturns\n-------\nvalue\nThe removed value that was previously associated with key\nRaises\n------\nKeyError\nIf key is not in object and no dflt argument specified",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key",
                "args"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_batch_update",
        "description": "A context manager that batches up trace and layout assignment\noperations into a singe plotly_update message that is executed when\nthe context exits.\nExamples\n--------\nFor example, suppose we have a figure widget, `fig`, with a single\ntrace.\n>>> import plotly.graph_objs as go\n>>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])\nIf we want to update the xaxis range, the yaxis range, and the\nmarker color, we could do so using a series of three property\nassignments as follows:\n>>> fig.layout.xaxis.range = [0, 5]\n>>> fig.layout.yaxis.range = [0, 10]\n>>> fig.data[0].marker.color = 'green'\nThis will work, however it will result in three messages being\nsent to the front end (two relayout messages for the axis range\nupdates followed by one restyle message for the marker color\nupdate). This can cause the plot to appear to stutter as the\nthree updates are applied incrementally.\nWe can avoid this problem by performing these three assignments in a\n`batch_update` context as follows:\n>>> with fig.batch_update():\n...     fig.layout.xaxis.range = [0, 5]\n...     fig.layout.yaxis.range = [0, 10]\n...     fig.data[0].marker.color = 'green'\nNow, these three property updates will be sent to the frontend in a\nsingle update message, and they will be applied by the front end\nsimultaneously.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_print_grid",
        "description": "Print a visual layout of the figure's axes arrangement.\nThis is only valid for figures that are created\nwith plotly.tools.make_subplots.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_vrect",
        "description": "Add a rectangle to a plot or subplot that extends infinitely in the\ny-dimension.\nParameters\n----------\nx0: float or int\nA number representing the x coordinate of one side of the rectangle.\nx1: float or int\nA number representing the x coordinate of the other side of the rectangle.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"inside\", \"outside\"], [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the rectangle. Example positions are \"outside top left\", \"inside\nbottom\", \"right\", \"inside left\", \"inside\" (\"outside\" is not supported). If\nan annotation is added but annotation_position is not specified this\ndefaults to \"inside top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x0": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "x1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "x0",
                "x1",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_plotly_update",
        "description": "Perform a Plotly update operation on the figure.\n\nNote: This operation both mutates and returns the figure\n\nParameters\n----------\nrestyle_data : dict\nTraces update specification. See the docstring for the\n`plotly_restyle` method for details\nrelayout_data : dict\nLayout update specification. See the docstring for the\n`plotly_relayout` method for details\ntrace_indexes :\nTrace index, or list of trace indexes, that the update operation\napplies to. Defaults to all trace indexes.\n\nReturns\n-------\nBaseFigure\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "restyle_data": {
                    "type": "object",
                    "description": "类型从参数名推断: restyle_data"
                },
                "relayout_data": {
                    "type": "object",
                    "description": "类型从参数名推断: relayout_data"
                },
                "trace_indexes": {
                    "type": "integer",
                    "description": "类型从参数名推断: trace_indexes"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_on_widget_constructed",
        "description": "Registers a callback to be called when a widget is constructed.\nThe callback must have the following signature:\ncallback(widget)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "callback": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "callback"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_batch_animate",
        "description": "Context manager to animate trace / layout updates\nParameters\n----------\nduration : number\nThe duration of the transition, in milliseconds.\nIf equal to zero, updates are synchronous.\neasing : string\nThe easing function used for the transition.\nOne of:\n- linear\n- quad\n- cubic\n- sin\n- exp\n- circle\n- elastic\n- back\n- bounce\n- linear-in\n- quad-in\n- cubic-in\n- sin-in\n- exp-in\n- circle-in\n- elastic-in\n- back-in\n- bounce-in\n- linear-out\n- quad-out\n- cubic-out\n- sin-out\n- exp-out\n- circle-out\n- elastic-out\n- back-out\n- bounce-out\n- linear-in-out\n- quad-in-out\n- cubic-in-out\n- sin-in-out\n- exp-in-out\n- circle-in-out\n- elastic-in-out\n- back-in-out\n- bounce-in-out\nExamples\n--------\nSuppose we have a figure widget, `fig`, with a single trace.\n>>> import plotly.graph_objs as go\n>>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])\n1) Animate a change in the xaxis and yaxis ranges using default\nduration and easing parameters.\n>>> with fig.batch_animate():\n...     fig.layout.xaxis.range = [0, 5]\n...     fig.layout.yaxis.range = [0, 10]\n2) Animate a change in the size and color of the trace's markers\nover 2 seconds using the elastic-in-out easing method\n>>> with fig.batch_animate(duration=2000, easing='elastic-in-out'):\n...     fig.data[0].marker.color = 'green'\n...     fig.data[0].marker.size = 20",
        "inputSchema": {
            "type": "object",
            "properties": {
                "duration": {
                    "type": "integer",
                    "default": 500,
                    "description": "类型从默认值推断: int"
                },
                "easing": {
                    "type": "string",
                    "default": "cubic-in-out",
                    "description": "类型从默认值推断: str"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_trait_names",
        "description": "Get a list of all the names of this class' traits.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "metadata": {
                    "type": "object",
                    "description": "类型从参数名推断: metadata"
                }
            },
            "required": [
                "metadata"
            ]
        }
    },
    {
        "name": "plotly_matplotlylib_mplexporter_utils_get_axis_properties",
        "description": "Return the property dictionary for a matplotlib.Axis instance",
        "inputSchema": {
            "type": "object",
            "properties": {
                "axis": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "axis"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_vline",
        "description": "Add a vertical line to a plot or subplot that extends infinitely in the\ny-dimension.\nParameters\n----------\nx: float or int\nA number representing the x coordinate of the vertical line.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the line. Example positions are \"bottom left\", \"right top\",\n\"right\", \"bottom\". If an annotation is added but annotation_position is\nnot specified, this defaults to \"top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "x",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_send_state",
        "description": "Sends the widget state, or a piece of it, to the front-end, if it exists.\nParameters\n----------\nkey : unicode, or iterable (optional)\nA single property's name or iterable of property names to sync with the front-end.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_update",
        "description": "Update the properties of the figure with a dict and/or with\nkeyword arguments.\nThis recursively updates the structure of the figure\nobject with the values in the input dict / keyword arguments.\nParameters\n----------\ndict1 : dict\nDictionary of properties to be updated\noverwrite: bool\nIf True, overwrite existing properties. If False, apply updates\nto existing properties recursively, preserving existing\nproperties that are not specified in the update operation.\nkwargs :\nKeyword/value pair of properties to be updated\nExamples\n--------\n>>> import plotly.graph_objs as go\n>>> fig = go.Figure(data=[{'y': [1, 2, 3]}])\n>>> fig.update(data=[{'y': [4, 5, 6]}]) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.to_plotly_json() # doctest: +SKIP\n{'data': [{'type': 'scatter',\n'uid': 'e86a7c7a-346a-11e8-8aa8-a0999b0c017b',\n'y': array([4, 5, 6], dtype=int32)}],\n'layout': {}}\n>>> fig = go.Figure(layout={'xaxis':\n...                         {'color': 'green',\n...                          'range': [0, 1]}})\n>>> fig.update({'layout': {'xaxis': {'color': 'pink'}}}) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.to_plotly_json() # doctest: +SKIP\n{'data': [],\n'layout': {'xaxis':\n{'color': 'pink',\n'range': [0, 1]}}}\nReturns\n-------\nBaseFigure\nUpdated figure",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dict1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "overwrite": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_unobserve",
        "description": "Remove a trait change handler.\nThis is used to unregister handlers to trait change notifications.\nParameters\n----------\nhandler : callable\nThe callable called when a trait attribute changes.\nnames : list, str, All (default: All)\nThe names of the traits for which the specified handler should be\nuninstalled. If names is All, the specified handler is uninstalled\nfrom the list of notifiers corresponding to all changes.\ntype : str or All (default: 'change')\nThe type of notification to filter by. If All, the specified handler\nis uninstalled from the list of notifiers corresponding to all types.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "handler": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "names": {
                    "type": "string",
                    "default": "traitlets.All",
                    "description": "类型从默认值推断: Sentinel"
                },
                "type": {
                    "type": "string",
                    "default": "change",
                    "description": "类型从默认值推断: str"
                }
            },
            "required": [
                "handler"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_hold_sync",
        "description": "Hold syncing any state until the outermost context manager exits",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_matplotlylib_mplexporter_utils_get_marker_style",
        "description": "Get the style dictionary for matplotlib marker objects",
        "inputSchema": {
            "type": "object",
            "properties": {
                "line": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "line"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_for_each_trace",
        "description": "Apply a function to all traces that satisfy the specified selection\ncriteria\nParameters\n----------\nfn:\nFunction that inputs a single trace object.\nselector: dict, function, int, str or None (default None)\nDict to use as selection criteria.\nTraces will be selected if they contain properties corresponding\nto all of the dictionary's keys, with values that exactly match\nthe supplied values. If None (the default), all traces are\nselected. If a function, it must be a function accepting a single\nargument and returning a boolean. The function will be called on\neach trace and those for which the function returned True\nwill be in the selection. If an int N, the Nth trace matching row\nand col will be selected (N can be negative). If a string S, the selector\nis equivalent to dict(type=S).\nrow, col: int or None (default None)\nSubplot row and column index of traces to select.\nTo select traces by row and column, the Figure must have been\ncreated using plotly.subplots.make_subplots.  If None\n(the default), all traces are selected.\nsecondary_y: boolean or None (default None)\n* If True, only select traces associated with the secondary\ny-axis of the subplot.\n* If False, only select traces associated with the primary\ny-axis of the subplot.\n* If None (the default), do not filter traces based on secondary\ny-axis.\nTo select traces by secondary y-axis, the Figure must have been\ncreated using plotly.subplots.make_subplots. See the docstring\nfor the specs argument to make_subplots for more info on\ncreating subplots with secondary y-axes.\nReturns\n-------\nself\nReturns the Figure object that the method was called on",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fn": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "selector": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "fn"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_class",
        "description": "Adds a class to the top level element of the widget.\nDoesn't add the class if it already exists.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "className": {
                    "type": "string",
                    "description": "类型从参数名推断: className"
                }
            },
            "required": [
                "className"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_get_manager_state",
        "description": "Returns the full state for a widget manager for embedding",
        "inputSchema": {
            "type": "object",
            "properties": {
                "drop_defaults": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "widgets": {
                    "type": "integer",
                    "description": "类型从参数名推断: widgets"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_select_traces",
        "description": "Select traces from a particular subplot cell and/or traces\nthat satisfy custom selection criteria.\nParameters\n----------\nselector: dict, function, int, str or None (default None)\nDict to use as selection criteria.\nTraces will be selected if they contain properties corresponding\nto all of the dictionary's keys, with values that exactly match\nthe supplied values. If None (the default), all traces are\nselected. If a function, it must be a function accepting a single\nargument and returning a boolean. The function will be called on\neach trace and those for which the function returned True\nwill be in the selection. If an int N, the Nth trace matching row\nand col will be selected (N can be negative). If a string S, the selector\nis equivalent to dict(type=S).\nrow, col: int or None (default None)\nSubplot row and column index of traces to select.\nTo select traces by row and column, the Figure must have been\ncreated using plotly.subplots.make_subplots.  If None\n(the default), all traces are selected.\nsecondary_y: boolean or None (default None)\n* If True, only select traces associated with the secondary\ny-axis of the subplot.\n* If False, only select traces associated with the primary\ny-axis of the subplot.\n* If None (the default), do not filter traces based on secondary\ny-axis.\nTo select traces by secondary y-axis, the Figure must have been\ncreated using plotly.subplots.make_subplots. See the docstring\nfor the specs argument to make_subplots for more info on\ncreating subplots with secondary y-axes.\nReturns\n-------\ngenerator\nGenerator that iterates through all of the traces that satisfy\nall of the specified selection criteria",
        "inputSchema": {
            "type": "object",
            "properties": {
                "selector": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_close",
        "description": "Close method.\nCloses the underlying comm.\nWhen the comm is closed, all of the widget views are automatically\nremoved from the front-end.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_batch_animate",
        "description": "Context manager to animate trace / layout updates\nParameters\n----------\nduration : number\nThe duration of the transition, in milliseconds.\nIf equal to zero, updates are synchronous.\neasing : string\nThe easing function used for the transition.\nOne of:\n- linear\n- quad\n- cubic\n- sin\n- exp\n- circle\n- elastic\n- back\n- bounce\n- linear-in\n- quad-in\n- cubic-in\n- sin-in\n- exp-in\n- circle-in\n- elastic-in\n- back-in\n- bounce-in\n- linear-out\n- quad-out\n- cubic-out\n- sin-out\n- exp-out\n- circle-out\n- elastic-out\n- back-out\n- bounce-out\n- linear-in-out\n- quad-in-out\n- cubic-in-out\n- sin-in-out\n- exp-in-out\n- circle-in-out\n- elastic-in-out\n- back-in-out\n- bounce-in-out\nExamples\n--------\nSuppose we have a figure widget, `fig`, with a single trace.\n>>> import plotly.graph_objs as go\n>>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])\n1) Animate a change in the xaxis and yaxis ranges using default\nduration and easing parameters.\n>>> with fig.batch_animate():\n...     fig.layout.xaxis.range = [0, 5]\n...     fig.layout.yaxis.range = [0, 10]\n2) Animate a change in the size and color of the trace's markers\nover 2 seconds using the elastic-in-out easing method\n>>> with fig.batch_animate(duration=2000, easing='elastic-in-out'):\n...     fig.data[0].marker.color = 'green'\n...     fig.data[0].marker.size = 20",
        "inputSchema": {
            "type": "object",
            "properties": {
                "duration": {
                    "type": "integer",
                    "default": 500,
                    "description": "类型从默认值推断: int"
                },
                "easing": {
                    "type": "string",
                    "default": "cubic-in-out",
                    "description": "类型从默认值推断: str"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_traces",
        "description": "Add traces to the figure\nParameters\n----------\ndata : list[BaseTraceType or dict]\nA list of trace specifications to be added.\nTrace specifications may be either:\n- Instances of trace classes from the plotly.graph_objs\npackage (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)\n- Dicts where:\n- The 'type' property specifies the trace type (e.g.\n'scatter', 'bar', 'area', etc.). If the dict has no 'type'\nproperty then 'scatter' is assumed.\n- All remaining properties are passed to the constructor\nof the specified trace type.\nrows : None, list[int], or int (default None)\nList of subplot row indexes (starting from 1) for the traces to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`\nIf a single integer is passed, all traces will be added to row number\ncols : None or list[int] (default None)\nList of subplot column indexes (starting from 1) for the traces\nto be added. Only valid if figure was created using\n`plotly.tools.make_subplots`\nIf a single integer is passed, all traces will be added to column number\nsecondary_ys: None or list[boolean] (default None)\nList of secondary_y booleans for traces to be added. See the\ndocstring for `add_trace` for more info.\nexclude_empty_subplots: boolean\nIf True, the trace will not be added to subplots that don't already\nhave traces.\nReturns\n-------\nBaseFigure\nThe Figure that add_traces was called on\nExamples\n--------\n>>> from plotly import subplots\n>>> import plotly.graph_objs as go\nAdd two Scatter traces to a figure\n>>> fig = go.Figure()\n>>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),\n...                 go.Scatter(x=[1,2,3], y=[2,1,2])]) # doctest: +ELLIPSIS\nFigure(...)\nAdd two Scatter traces to vertically stacked subplots\n>>> fig = subplots.make_subplots(rows=2)\n>>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),\n...                 go.Scatter(x=[1,2,3], y=[2,1,2])],\n...                 rows=[1, 2], cols=[1, 1]) # doctest: +ELLIPSIS\nFigure(...)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "rows": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "cols": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_ys": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "data"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_get_subplot",
        "description": "Return an object representing the subplot at the specified row\nand column.  May only be used on Figures created using\nplotly.tools.make_subplots\nParameters\n----------\nrow: int\n1-based index of subplot row\ncol: int\n1-based index of subplot column\nsecondary_y: bool\nIf True, select the subplot that consists of the x-axis and the\nsecondary y-axis at the specified row/col. Only valid if the\nsubplot at row/col is an 2D cartesian subplot that was created\nwith a secondary y-axis.  See the docstring for the specs argument\nto make_subplots for more info on creating a subplot with a\nsecondary y-axis.\nReturns\n-------\nsubplot\n* None: if subplot is empty\n* plotly.graph_objs.layout.Scene: if subplot type is 'scene'\n* plotly.graph_objs.layout.Polar: if subplot type is 'polar'\n* plotly.graph_objs.layout.Ternary: if subplot type is 'ternary'\n* plotly.graph_objs.layout.Mapbox: if subplot type is 'ternary'\n* SubplotDomain namedtuple with `x` and `y` fields:\nif subplot type is 'domain'.\n- x: length 2 list of the subplot start and stop width\n- y: length 2 list of the subplot start and stop height\n* SubplotXY namedtuple with `xaxis` and `yaxis` fields:\nif subplot type is 'xy'.\n- xaxis: plotly.graph_objs.layout.XAxis instance for subplot\n- yaxis: plotly.graph_objs.layout.YAxis instance for subplot",
        "inputSchema": {
            "type": "object",
            "properties": {
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "row",
                "col"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_hline",
        "description": "Add a horizontal line to a plot or subplot that extends infinitely in the\nx-dimension.\nParameters\n----------\ny: float or int\nA number representing the y coordinate of the horizontal line.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the line. Example positions are \"bottom left\", \"right top\",\n\"right\", \"bottom\". If an annotation is added but annotation_position is\nnot specified, this defaults to \"top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "y",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_get_subplot",
        "description": "Return an object representing the subplot at the specified row\nand column.  May only be used on Figures created using\nplotly.tools.make_subplots\nParameters\n----------\nrow: int\n1-based index of subplot row\ncol: int\n1-based index of subplot column\nsecondary_y: bool\nIf True, select the subplot that consists of the x-axis and the\nsecondary y-axis at the specified row/col. Only valid if the\nsubplot at row/col is an 2D cartesian subplot that was created\nwith a secondary y-axis.  See the docstring for the specs argument\nto make_subplots for more info on creating a subplot with a\nsecondary y-axis.\nReturns\n-------\nsubplot\n* None: if subplot is empty\n* plotly.graph_objs.layout.Scene: if subplot type is 'scene'\n* plotly.graph_objs.layout.Polar: if subplot type is 'polar'\n* plotly.graph_objs.layout.Ternary: if subplot type is 'ternary'\n* plotly.graph_objs.layout.Mapbox: if subplot type is 'ternary'\n* SubplotDomain namedtuple with `x` and `y` fields:\nif subplot type is 'domain'.\n- x: length 2 list of the subplot start and stop width\n- y: length 2 list of the subplot start and stop height\n* SubplotXY namedtuple with `xaxis` and `yaxis` fields:\nif subplot type is 'xy'.\n- xaxis: plotly.graph_objs.layout.XAxis instance for subplot\n- yaxis: plotly.graph_objs.layout.YAxis instance for subplot",
        "inputSchema": {
            "type": "object",
            "properties": {
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "row",
                "col"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_on_msg",
        "description": "(Un)Register a custom msg receive callback.\nParameters\n----------\ncallback: callable\ncallback will be passed three arguments when a message arrives::\ncallback(widget, content, buffers)\nremove: bool\nTrue if the callback should be unregistered.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "callback": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "remove": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "callback"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_on_trait_change",
        "description": "DEPRECATED: Setup a handler to be called when a trait changes.\nThis is used to setup dynamic notifications of trait changes.\nStatic handlers can be created by creating methods on a HasTraits\nsubclass with the naming convention '_[traitname]_changed'.  Thus,\nto create static handler for the trait 'a', create the method\n_a_changed(self, name, old, new) (fewer arguments can be used, see\nbelow).\nIf `remove` is True and `handler` is not specified, all change\nhandlers for the specified name are uninstalled.\nParameters\n----------\nhandler : callable, None\nA callable that is called when a trait changes.  Its\nsignature can be handler(), handler(name), handler(name, new),\nhandler(name, old, new), or handler(name, old, new, self).\nname : list, str, None\nIf None, the handler will apply to all traits.  If a list\nof str, handler will apply to all names in the list.  If a\nstr, the handler will apply just to that name.\nremove : bool\nIf False (the default), then install the handler.  If True\nthen unintall it.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "handler": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "remove": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_full_figure_for_development",
        "description": "Compute default values for all attributes not specified in the input figure and\nreturns the output as a \"full\" figure. This function calls Plotly.js via Kaleido\nto populate unspecified attributes. This function is intended for interactive use\nduring development to learn more about how Plotly.js computes default values and is\nnot generally necessary or recommended for production use.\nParameters\n----------\nfig:\nFigure object or dict representing a figure\nwarn: bool\nIf False, suppress warnings about not using this in production.\nas_dict: bool\nIf True, output is a dict with some keys that go.Figure can't parse.\nIf False, output is a go.Figure with unparseable keys skipped.\nReturns\n-------\nplotly.graph_objects.Figure or dict\nThe full figure",
        "inputSchema": {
            "type": "object",
            "properties": {
                "warn": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "as_dict": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_to_image",
        "description": "Convert a figure to a static image bytes string\nParameters\n----------\nformat: str or None\nThe desired image format. One of\n- 'png'\n- 'jpg' or 'jpeg'\n- 'webp'\n- 'svg'\n- 'pdf'\n- 'eps' (Requires the poppler library to be installed)\nIf not specified, will default to `plotly.io.config.default_format`\nwidth: int or None\nThe width of the exported image in layout pixels. If the `scale`\nproperty is 1.0, this will also be the width of the exported image\nin physical pixels.\nIf not specified, will default to `plotly.io.config.default_width`\nheight: int or None\nThe height of the exported image in layout pixels. If the `scale`\nproperty is 1.0, this will also be the height of the exported image\nin physical pixels.\nIf not specified, will default to `plotly.io.config.default_height`\nscale: int or float or None\nThe scale factor to use when exporting the figure. A scale factor\nlarger than 1.0 will increase the image resolution with respect\nto the figure's layout pixel dimensions. Whereas as scale factor of\nless than 1.0 will decrease the image resolution.\nIf not specified, will default to `plotly.io.config.default_scale`\nvalidate: bool\nTrue if the figure should be validated before being converted to\nan image, False otherwise.\nengine: str\nImage export engine to use:\n- \"kaleido\": Use Kaleido for image export\n- \"orca\": Use Orca for image export\n- \"auto\" (default): Use Kaleido if installed, otherwise use orca\nReturns\n-------\nbytes\nThe image data",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_to_json",
        "description": "Convert a figure to a JSON string representation\nParameters\n----------\nvalidate: bool (default True)\nTrue if the figure should be validated before being converted to\nJSON, False otherwise.\npretty: bool (default False)\nTrue if JSON representation should be pretty-printed, False if\nrepresentation should be as compact as possible.\nremove_uids: bool (default True)\nTrue if trace UIDs should be omitted from the JSON representation\nengine: str (default None)\nThe JSON encoding engine to use. One of:\n- \"json\" for an encoder based on the built-in Python json module\n- \"orjson\" for a fast encoder the requires the orjson package\nIf not specified, the default encoder is set to the current value of\nplotly.io.json.config.default_encoder.\nReturns\n-------\nstr\nRepresentation of figure as a JSON string",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_batch_update",
        "description": "A context manager that batches up trace and layout assignment\noperations into a singe plotly_update message that is executed when\nthe context exits.\nExamples\n--------\nFor example, suppose we have a figure widget, `fig`, with a single\ntrace.\n>>> import plotly.graph_objs as go\n>>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])\nIf we want to update the xaxis range, the yaxis range, and the\nmarker color, we could do so using a series of three property\nassignments as follows:\n>>> fig.layout.xaxis.range = [0, 5]\n>>> fig.layout.yaxis.range = [0, 10]\n>>> fig.data[0].marker.color = 'green'\nThis will work, however it will result in three messages being\nsent to the front end (two relayout messages for the axis range\nupdates followed by one restyle message for the marker color\nupdate). This can cause the plot to appear to stutter as the\nthree updates are applied incrementally.\nWe can avoid this problem by performing these three assignments in a\n`batch_update` context as follows:\n>>> with fig.batch_update():\n...     fig.layout.xaxis.range = [0, 5]\n...     fig.layout.yaxis.range = [0, 10]\n...     fig.data[0].marker.color = 'green'\nNow, these three property updates will be sent to the frontend in a\nsingle update message, and they will be applied by the front end\nsimultaneously.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_for_each_trace",
        "description": "Apply a function to all traces that satisfy the specified selection\ncriteria\nParameters\n----------\nfn:\nFunction that inputs a single trace object.\nselector: dict, function, int, str or None (default None)\nDict to use as selection criteria.\nTraces will be selected if they contain properties corresponding\nto all of the dictionary's keys, with values that exactly match\nthe supplied values. If None (the default), all traces are\nselected. If a function, it must be a function accepting a single\nargument and returning a boolean. The function will be called on\neach trace and those for which the function returned True\nwill be in the selection. If an int N, the Nth trace matching row\nand col will be selected (N can be negative). If a string S, the selector\nis equivalent to dict(type=S).\nrow, col: int or None (default None)\nSubplot row and column index of traces to select.\nTo select traces by row and column, the Figure must have been\ncreated using plotly.subplots.make_subplots.  If None\n(the default), all traces are selected.\nsecondary_y: boolean or None (default None)\n* If True, only select traces associated with the secondary\ny-axis of the subplot.\n* If False, only select traces associated with the primary\ny-axis of the subplot.\n* If None (the default), do not filter traces based on secondary\ny-axis.\nTo select traces by secondary y-axis, the Figure must have been\ncreated using plotly.subplots.make_subplots. See the docstring\nfor the specs argument to make_subplots for more info on\ncreating subplots with secondary y-axes.\nReturns\n-------\nself\nReturns the Figure object that the method was called on",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fn": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "selector": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "fn"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_unobserve_all",
        "description": "Remove trait change handlers of any type for the specified name.\nIf name is not specified, removes all trait notifiers.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "default": "traitlets.All",
                    "description": "类型从默认值推断: Sentinel"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_matplotlylib_mpltools_get_axes_bounds",
        "description": "Return the entire axes space for figure.\nAn axes object in mpl is specified by its relation to the figure where\n(0,0) corresponds to the bottom-left part of the figure and (1,1)\ncorresponds to the top-right. Margins exist in matplotlib because axes\nobjects normally don't go to the edges of the figure.\nIn plotly, the axes area (where all subplots go) is always specified with\nthe domain [0,1] for both x and y. This function finds the smallest box,\nspecified by two points, that all of the mpl axes objects fit into. This\nbox is then used to map mpl axes domains to plotly axes domains.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "fig": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "fig"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_trace",
        "description": "Add a trace to the figure\nParameters\n----------\ntrace : BaseTraceType or dict\nEither:\n- An instances of a trace classe from the plotly.graph_objs\npackage (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)\n- or a dicts where:\n- The 'type' property specifies the trace type (e.g.\n'scatter', 'bar', 'area', etc.). If the dict has no 'type'\nproperty then 'scatter' is assumed.\n- All remaining properties are passed to the constructor\nof the specified trace type.\nrow : 'all', int or None (default)\nSubplot row index (starting from 1) for the trace to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`.\nIf 'all', addresses all rows in the specified column(s).\ncol : 'all', int or None (default)\nSubplot col index (starting from 1) for the trace to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`.\nIf 'all', addresses all columns in the specified row(s).\nsecondary_y: boolean or None (default None)\nIf True, associate this trace with the secondary y-axis of the\nsubplot at the specified row and col. Only valid if all of the\nfollowing conditions are satisfied:\n* The figure was created using `plotly.subplots.make_subplots`.\n* The row and col arguments are not None\n* The subplot at the specified row and col has type xy\n(which is the default) and secondary_y True.  These\nproperties are specified in the specs argument to\nmake_subplots. See the make_subplots docstring for more info.\n* The trace argument is a 2D cartesian trace\n(scatter, bar, etc.)\nexclude_empty_subplots: boolean\nIf True, the trace will not be added to subplots that don't already\nhave traces.\nReturns\n-------\nBaseFigure\nThe Figure that add_trace was called on\nExamples\n--------\n>>> from plotly import subplots\n>>> import plotly.graph_objs as go\nAdd two Scatter traces to a figure\n>>> fig = go.Figure()\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS\nFigure(...)\nAdd two Scatter traces to vertically stacked subplots\n>>> fig = subplots.make_subplots(rows=2)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1) # doctest: +ELLIPSIS\nFigure(...)\n>>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1) # doctest: +ELLIPSIS\nFigure(...)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "trace": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "trace"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_update_traces",
        "description": "Perform a property update operation on all traces that satisfy the\nspecified selection criteria\nParameters\n----------\npatch: dict or None (default None)\nDictionary of property updates to be applied to all traces that\nsatisfy the selection criteria.\nselector: dict, function, int, str or None (default None)\nDict to use as selection criteria.\nTraces will be selected if they contain properties corresponding\nto all of the dictionary's keys, with values that exactly match\nthe supplied values. If None (the default), all traces are\nselected. If a function, it must be a function accepting a single\nargument and returning a boolean. The function will be called on\neach trace and those for which the function returned True\nwill be in the selection. If an int N, the Nth trace matching row\nand col will be selected (N can be negative). If a string S, the selector\nis equivalent to dict(type=S).\nrow, col: int or None (default None)\nSubplot row and column index of traces to select.\nTo select traces by row and column, the Figure must have been\ncreated using plotly.subplots.make_subplots.  If None\n(the default), all traces are selected.\nsecondary_y: boolean or None (default None)\n* If True, only select traces associated with the secondary\ny-axis of the subplot.\n* If False, only select traces associated with the primary\ny-axis of the subplot.\n* If None (the default), do not filter traces based on secondary\ny-axis.\nTo select traces by secondary y-axis, the Figure must have been\ncreated using plotly.subplots.make_subplots. See the docstring\nfor the specs argument to make_subplots for more info on\ncreating subplots with secondary y-axes.\noverwrite: bool\nIf True, overwrite existing properties. If False, apply updates\nto existing properties recursively, preserving existing\nproperties that are not specified in the update operation.\n**kwargs\nAdditional property updates to apply to each selected trace. If\na property is specified in both patch and in **kwargs then the\none in **kwargs takes precedence.\nReturns\n-------\nself\nReturns the Figure object that the method was called on",
        "inputSchema": {
            "type": "object",
            "properties": {
                "patch": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "selector": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "overwrite": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_traits",
        "description": "Get a ``dict`` of all the traits of this class.  The dictionary\nis keyed on the name and the values are the TraitType objects.\nThe TraitTypes returned don't know anything about the values\nthat the various HasTrait's instances are holding.\nThe metadata kwargs allow functions to be passed in which\nfilter traits based on metadata values.  The functions should\ntake a single value as an argument and return a boolean.  If\nany function returns False, then the trait is not included in\nthe output.  If a metadata key doesn't exist, None will be passed\nto the function.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "metadata": {
                    "type": "object",
                    "description": "类型从参数名推断: metadata"
                }
            },
            "required": [
                "metadata"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_traces",
        "description": "Add traces to the figure\nParameters\n----------\ndata : list[BaseTraceType or dict]\nA list of trace specifications to be added.\nTrace specifications may be either:\n- Instances of trace classes from the plotly.graph_objs\npackage (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)\n- Dicts where:\n- The 'type' property specifies the trace type (e.g.\n'scatter', 'bar', 'area', etc.). If the dict has no 'type'\nproperty then 'scatter' is assumed.\n- All remaining properties are passed to the constructor\nof the specified trace type.\nrows : None, list[int], or int (default None)\nList of subplot row indexes (starting from 1) for the traces to be\nadded. Only valid if figure was created using\n`plotly.tools.make_subplots`\nIf a single integer is passed, all traces will be added to row number\ncols : None or list[int] (default None)\nList of subplot column indexes (starting from 1) for the traces\nto be added. Only valid if figure was created using\n`plotly.tools.make_subplots`\nIf a single integer is passed, all traces will be added to column number\nsecondary_ys: None or list[boolean] (default None)\nList of secondary_y booleans for traces to be added. See the\ndocstring for `add_trace` for more info.\nexclude_empty_subplots: boolean\nIf True, the trace will not be added to subplots that don't already\nhave traces.\nReturns\n-------\nBaseFigure\nThe Figure that add_traces was called on\nExamples\n--------\n>>> from plotly import subplots\n>>> import plotly.graph_objs as go\nAdd two Scatter traces to a figure\n>>> fig = go.Figure()\n>>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),\n...                 go.Scatter(x=[1,2,3], y=[2,1,2])]) # doctest: +ELLIPSIS\nFigure(...)\nAdd two Scatter traces to vertically stacked subplots\n>>> fig = subplots.make_subplots(rows=2)\n>>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),\n...                 go.Scatter(x=[1,2,3], y=[2,1,2])],\n...                 rows=[1, 2], cols=[1, 1]) # doctest: +ELLIPSIS\nFigure(...)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "description": "类型从参数名推断: data"
                },
                "rows": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "cols": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_ys": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "data"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_append_trace",
        "description": "Add a trace to the figure bound to axes at the specified row,\ncol index.\nA row, col index grid is generated for figures created with\nplotly.tools.make_subplots, and can be viewed with the `print_grid`\nmethod\nParameters\n----------\ntrace\nThe data trace to be bound\nrow: int\nSubplot row index (see Figure.print_grid)\ncol: int\nSubplot column index (see Figure.print_grid)\nExamples\n--------\n>>> from plotly import tools\n>>> import plotly.graph_objs as go\n>>> # stack two subplots vertically\n>>> fig = tools.make_subplots(rows=2)\nThis is the format of your plot grid:\n[ (1,1) x1,y1 ]\n[ (2,1) x2,y2 ]\n>>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1)\n>>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "trace": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "trace",
                "row",
                "col"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_to_json",
        "description": "Convert a figure to a JSON string representation\nParameters\n----------\nvalidate: bool (default True)\nTrue if the figure should be validated before being converted to\nJSON, False otherwise.\npretty: bool (default False)\nTrue if JSON representation should be pretty-printed, False if\nrepresentation should be as compact as possible.\nremove_uids: bool (default True)\nTrue if trace UIDs should be omitted from the JSON representation\nengine: str (default None)\nThe JSON encoding engine to use. One of:\n- \"json\" for an encoder based on the built-in Python json module\n- \"orjson\" for a fast encoder the requires the orjson package\nIf not specified, the default encoder is set to the current value of\nplotly.io.json.config.default_encoder.\nReturns\n-------\nstr\nRepresentation of figure as a JSON string",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_send",
        "description": "Sends a custom msg to the widget model in the front-end.\nParameters\n----------\ncontent : dict\nContent of the message to send.\nbuffers : list of binary buffers\nBinary buffers to send with message",
        "inputSchema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "buffers": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "content"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_hrect",
        "description": "Add a rectangle to a plot or subplot that extends infinitely in the\nx-dimension.\nParameters\n----------\ny0: float or int\nA number representing the y coordinate of one side of the rectangle.\ny1: float or int\nA number representing the y coordinate of the other side of the rectangle.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"inside\", \"outside\"], [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the rectangle. Example positions are \"outside top left\", \"inside\nbottom\", \"right\", \"inside left\", \"inside\" (\"outside\" is not supported). If\nan annotation is added but annotation_position is not specified this\ndefaults to \"inside top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "y0": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "y0",
                "y1",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_has_trait",
        "description": "Returns True if the object has a trait with the specified name.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_remove_class",
        "description": "Removes a class from the top level element of the widget.\nDoesn't remove the class if it doesn't exist.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "className": {
                    "type": "string",
                    "description": "类型从参数名推断: className"
                }
            },
            "required": [
                "className"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_write_json",
        "description": "Convert a figure to JSON and write it to a file or writeable\nobject\nParameters\n----------\nfile: str or writeable\nA string representing a local file path or a writeable object\n(e.g. an open file descriptor)\npretty: bool (default False)\nTrue if JSON representation should be pretty-printed, False if\nrepresentation should be as compact as possible.\nremove_uids: bool (default True)\nTrue if trace UIDs should be omitted from the JSON representation\nengine: str (default None)\nThe JSON encoding engine to use. One of:\n- \"json\" for an encoder based on the built-in Python json module\n- \"orjson\" for a fast encoder the requires the orjson package\nIf not specified, the default encoder is set to the current value of\nplotly.io.json.config.default_encoder.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_set_subplots",
        "description": "Add subplots to this figure. If the figure already contains subplots,\nthen this throws an error. Accepts any keyword arguments that\nplotly.subplots.make_subplots accepts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "rows": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "cols": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "make_subplots_args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "make_subplots_args"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_pop",
        "description": "Remove the value associated with the specified key and return it\nParameters\n----------\nkey: str\nProperty name\ndflt\nThe default value to return if key was not found in figure\nReturns\n-------\nvalue\nThe removed value that was previously associated with key\nRaises\n------\nKeyError\nIf key is not in object and no dflt argument specified",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "key",
                "args"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_trait_has_value",
        "description": "Returns True if the specified trait has a value.\nThis will return False even if ``getattr`` would return a\ndynamically generated default value. These default values\nwill be recognized as existing only after they have been\ngenerated.\nExample\n.. code-block:: python\nclass MyClass(HasTraits):\ni = Int()\nmc = MyClass()\nassert not mc.trait_has_value(\"i\")\nmc.i # generates a default value\nassert mc.trait_has_value(\"i\")",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                }
            },
            "required": [
                "name"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_to_html",
        "description": "Convert a figure to an HTML string representation.\nParameters\n----------\nconfig: dict or None (default None)\nPlotly.js figure config options\nauto_play: bool (default=True)\nWhether to automatically start the animation sequence on page load\nif the figure contains frames. Has no effect if the figure does not\ncontain frames.\ninclude_plotlyjs: bool or string (default True)\nSpecifies how the plotly.js library is included/loaded in the output\ndiv string.\nIf True, a script tag containing the plotly.js source code (~3MB)\nis included in the output.  HTML files generated with this option are\nfully self-contained and can be used offline.\nIf 'cdn', a script tag that references the plotly.js CDN is included\nin the output. HTML files generated with this option are about 3MB\nsmaller than those generated with include_plotlyjs=True, but they\nrequire an active internet connection in order to load the plotly.js\nlibrary.\nIf 'directory', a script tag is included that references an external\nplotly.min.js bundle that is assumed to reside in the same\ndirectory as the HTML file.\nIf 'require', Plotly.js is loaded using require.js.  This option\nassumes that require.js is globally available and that it has been\nglobally configured to know how to find Plotly.js as 'plotly'.\nThis option is not advised when full_html=True as it will result\nin a non-functional html file.\nIf a string that ends in '.js', a script tag is included that\nreferences the specified path. This approach can be used to point\nthe resulting HTML file to an alternative CDN or local bundle.\nIf False, no script tag referencing plotly.js is included. This is\nuseful when the resulting div string will be placed inside an HTML\ndocument that already loads plotly.js. This option is not advised\nwhen full_html=True as it will result in a non-functional html file.\ninclude_mathjax: bool or string (default False)\nSpecifies how the MathJax.js library is included in the output html\ndiv string.  MathJax is required in order to display labels\nwith LaTeX typesetting.\nIf False, no script tag referencing MathJax.js will be included in the\noutput.\nIf 'cdn', a script tag that references a MathJax CDN location will be\nincluded in the output.  HTML div strings generated with this option\nwill be able to display LaTeX typesetting as long as internet access\nis available.\nIf a string that ends in '.js', a script tag is included that\nreferences the specified path. This approach can be used to point the\nresulting HTML div string to an alternative CDN.\npost_script: str or list or None (default None)\nJavaScript snippet(s) to be included in the resulting div just after\nplot creation.  The string(s) may include '{plot_id}' placeholders\nthat will then be replaced by the `id` of the div element that the\nplotly.js figure is associated with.  One application for this script\nis to install custom plotly.js event handlers.\nfull_html: bool (default True)\nIf True, produce a string containing a complete HTML document\nstarting with an <html> tag.  If False, produce a string containing\na single <div> element.\nanimation_opts: dict or None (default None)\ndict of custom animation parameters to be passed to the function\nPlotly.animate in Plotly.js. See\nhttps://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js\nfor available options. Has no effect if the figure does not contain\nframes, or auto_play is False.\ndefault_width, default_height: number or str (default '100%')\nThe default figure width/height to use if the provided figure does not\nspecify its own layout.width/layout.height property.  May be\nspecified in pixels as an integer (e.g. 500), or as a css width style\nstring (e.g. '500px', '100%').\nvalidate: bool (default True)\nTrue if the figure should be validated before being converted to\nJSON, False otherwise.\ndiv_id: str (default None)\nIf provided, this is the value of the id attribute of the div tag. If None, the\nid attribute is a UUID.\nReturns\n-------\nstr\nRepresentation of figure as an HTML div string",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_full_figure_for_development",
        "description": "Compute default values for all attributes not specified in the input figure and\nreturns the output as a \"full\" figure. This function calls Plotly.js via Kaleido\nto populate unspecified attributes. This function is intended for interactive use\nduring development to learn more about how Plotly.js computes default values and is\nnot generally necessary or recommended for production use.\nParameters\n----------\nfig:\nFigure object or dict representing a figure\nwarn: bool\nIf False, suppress warnings about not using this in production.\nas_dict: bool\nIf True, output is a dict with some keys that go.Figure can't parse.\nIf False, output is a go.Figure with unparseable keys skipped.\nReturns\n-------\nplotly.graph_objects.Figure or dict\nThe full figure",
        "inputSchema": {
            "type": "object",
            "properties": {
                "warn": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "as_dict": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_hrect",
        "description": "Add a rectangle to a plot or subplot that extends infinitely in the\nx-dimension.\nParameters\n----------\ny0: float or int\nA number representing the y coordinate of one side of the rectangle.\ny1: float or int\nA number representing the y coordinate of the other side of the rectangle.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"inside\", \"outside\"], [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the rectangle. Example positions are \"outside top left\", \"inside\nbottom\", \"right\", \"inside left\", \"inside\" (\"outside\" is not supported). If\nan annotation is added but annotation_position is not specified this\ndefaults to \"inside top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "y0": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "y1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "y0",
                "y1",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_to_plotly_json",
        "description": "Convert figure to a JSON representation as a Python dict\n\nNote: May include some JSON-invalid data types, use the `PlotlyJSONEncoder` util\nor the `to_json` method to encode to a string.\n\nReturns\n-------\ndict",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_plotly_restyle",
        "description": "Perform a Plotly restyle operation on the figure's traces\nParameters\n----------\nrestyle_data : dict\nDict of trace style updates.\nKeys are strings that specify the properties to be updated.\nNested properties are expressed by joining successive keys on\n'.' characters (e.g. 'marker.color').\nValues may be scalars or lists. When values are scalars,\nthat scalar value is applied to all traces specified by the\n`trace_indexes` parameter.  When values are lists,\nthe restyle operation will cycle through the elements\nof the list as it cycles through the traces specified by the\n`trace_indexes` parameter.\nCaution: To use plotly_restyle to update a list property (e.g.\nthe `x` property of the scatter trace), the property value\nshould be a scalar list containing the list to update with. For\nexample, the following command would be used to update the 'x'\nproperty of the first trace to the list [1, 2, 3]\n>>> import plotly.graph_objects as go\n>>> fig = go.Figure(go.Scatter(x=[2, 4, 6]))\n>>> fig.plotly_restyle({'x': [[1, 2, 3]]}, 0)\ntrace_indexes : int or list of int\nTrace index, or list of trace indexes, that the restyle operation\napplies to. Defaults to all trace indexes.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "restyle_data": {
                    "type": "object",
                    "description": "类型从参数名推断: restyle_data"
                },
                "trace_indexes": {
                    "type": "integer",
                    "description": "类型从参数名推断: trace_indexes"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "restyle_data",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_matplotlylib_mplexporter_utils_get_line_style",
        "description": "Get the style dictionary for matplotlib line objects",
        "inputSchema": {
            "type": "object",
            "properties": {
                "line": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "line"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_plotly_relayout",
        "description": "Perform a Plotly relayout operation on the figure's layout\nParameters\n----------\nrelayout_data : dict\nDict of layout updates\ndict keys are strings that specify the properties to be updated.\nNested properties are expressed by joining successive keys on\n'.' characters (e.g. 'xaxis.range')\ndict values are the values to use to update the layout.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "relayout_data": {
                    "type": "object",
                    "description": "类型从参数名推断: relayout_data"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "relayout_data",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_append_trace",
        "description": "Add a trace to the figure bound to axes at the specified row,\ncol index.\nA row, col index grid is generated for figures created with\nplotly.tools.make_subplots, and can be viewed with the `print_grid`\nmethod\nParameters\n----------\ntrace\nThe data trace to be bound\nrow: int\nSubplot row index (see Figure.print_grid)\ncol: int\nSubplot column index (see Figure.print_grid)\nExamples\n--------\n>>> from plotly import tools\n>>> import plotly.graph_objs as go\n>>> # stack two subplots vertically\n>>> fig = tools.make_subplots(rows=2)\nThis is the format of your plot grid:\n[ (1,1) x1,y1 ]\n[ (2,1) x2,y2 ]\n>>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1)\n>>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "trace": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "trace",
                "row",
                "col"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_to_dict",
        "description": "Convert figure to a dictionary\n\nNote: the dictionary includes the properties explicitly set by the\nuser, it does not include default values of unspecified properties\n\nReturns\n-------\ndict",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_matplotlylib_mplexporter_utils_get_path_style",
        "description": "Get the style dictionary for matplotlib path objects",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "fill": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "path"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_set_state",
        "description": "Called when a state is received from the front-end.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "sync_data": {
                    "type": "object",
                    "description": "类型从参数名推断: sync_data"
                }
            },
            "required": [
                "sync_data"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_plotly_update",
        "description": "Perform a Plotly update operation on the figure.\n\nNote: This operation both mutates and returns the figure\n\nParameters\n----------\nrestyle_data : dict\nTraces update specification. See the docstring for the\n`plotly_restyle` method for details\nrelayout_data : dict\nLayout update specification. See the docstring for the\n`plotly_relayout` method for details\ntrace_indexes :\nTrace index, or list of trace indexes, that the update operation\napplies to. Defaults to all trace indexes.\n\nReturns\n-------\nBaseFigure\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "restyle_data": {
                    "type": "object",
                    "description": "类型从参数名推断: restyle_data"
                },
                "relayout_data": {
                    "type": "object",
                    "description": "类型从参数名推断: relayout_data"
                },
                "trace_indexes": {
                    "type": "integer",
                    "description": "类型从参数名推断: trace_indexes"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_set_trait",
        "description": "Forcibly sets trait attribute, including read-only attributes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "类型从参数名推断: name"
                },
                "value": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "name",
                "value"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_trait_metadata",
        "description": "Get metadata values for trait by key.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "traitname": {
                    "type": "string",
                    "description": "类型从参数名推断: traitname"
                },
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "default": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "traitname",
                "key"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_write_image",
        "description": "Convert a figure to a static image and write it to a file or writeable\nobject\nParameters\n----------\nfile: str or writeable\nA string representing a local file path or a writeable object\n(e.g. a pathlib.Path object or an open file descriptor)\nformat: str or None\nThe desired image format. One of\n- 'png'\n- 'jpg' or 'jpeg'\n- 'webp'\n- 'svg'\n- 'pdf'\n- 'eps' (Requires the poppler library to be installed)\nIf not specified and `file` is a string then this will default to the\nfile extension. If not specified and `file` is not a string then this\nwill default to `plotly.io.config.default_format`\nwidth: int or None\nThe width of the exported image in layout pixels. If the `scale`\nproperty is 1.0, this will also be the width of the exported image\nin physical pixels.\nIf not specified, will default to `plotly.io.config.default_width`\nheight: int or None\nThe height of the exported image in layout pixels. If the `scale`\nproperty is 1.0, this will also be the height of the exported image\nin physical pixels.\nIf not specified, will default to `plotly.io.config.default_height`\nscale: int or float or None\nThe scale factor to use when exporting the figure. A scale factor\nlarger than 1.0 will increase the image resolution with respect\nto the figure's layout pixel dimensions. Whereas as scale factor of\nless than 1.0 will decrease the image resolution.\nIf not specified, will default to `plotly.io.config.default_scale`\nvalidate: bool\nTrue if the figure should be validated before being converted to\nan image, False otherwise.\nengine: str\nImage export engine to use:\n- \"kaleido\": Use Kaleido for image export\n- \"orca\": Use Orca for image export\n- \"auto\" (default): Use Kaleido if installed, otherwise use orca\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_matplotlylib_mplexporter_utils_get_dasharray",
        "description": "Get an SVG dash array for the given matplotlib linestyle\nParameters\n----------\nobj : matplotlib object\nThe matplotlib line or path object, which must have a get_linestyle()\nmethod which returns a valid matplotlib line code\nReturns\n-------\ndasharray : string\nThe HTML/SVG dasharray code associated with the object.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "obj": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "obj"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_on_displayed",
        "description": "(Un)Register a widget displayed callback.\nParameters\n----------\ncallback: method handler\nMust have a signature of::\ncallback(widget, **kwargs)\nkwargs from display are passed through without modification.\nremove: bool\nTrue if the callback should be unregistered.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "callback": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "remove": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "callback"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_plotly_relayout",
        "description": "Perform a Plotly relayout operation on the figure's layout\nParameters\n----------\nrelayout_data : dict\nDict of layout updates\ndict keys are strings that specify the properties to be updated.\nNested properties are expressed by joining successive keys on\n'.' characters (e.g. 'xaxis.range')\ndict values are the values to use to update the layout.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "relayout_data": {
                    "type": "object",
                    "description": "类型从参数名推断: relayout_data"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "relayout_data",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_plotly_restyle",
        "description": "Perform a Plotly restyle operation on the figure's traces\nParameters\n----------\nrestyle_data : dict\nDict of trace style updates.\nKeys are strings that specify the properties to be updated.\nNested properties are expressed by joining successive keys on\n'.' characters (e.g. 'marker.color').\nValues may be scalars or lists. When values are scalars,\nthat scalar value is applied to all traces specified by the\n`trace_indexes` parameter.  When values are lists,\nthe restyle operation will cycle through the elements\nof the list as it cycles through the traces specified by the\n`trace_indexes` parameter.\nCaution: To use plotly_restyle to update a list property (e.g.\nthe `x` property of the scatter trace), the property value\nshould be a scalar list containing the list to update with. For\nexample, the following command would be used to update the 'x'\nproperty of the first trace to the list [1, 2, 3]\n>>> import plotly.graph_objects as go\n>>> fig = go.Figure(go.Scatter(x=[2, 4, 6]))\n>>> fig.plotly_restyle({'x': [[1, 2, 3]]}, 0)\ntrace_indexes : int or list of int\nTrace index, or list of trace indexes, that the restyle operation\napplies to. Defaults to all trace indexes.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "restyle_data": {
                    "type": "object",
                    "description": "类型从参数名推断: restyle_data"
                },
                "trace_indexes": {
                    "type": "integer",
                    "description": "类型从参数名推断: trace_indexes"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "restyle_data",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_open",
        "description": "Open a comm to the frontend if one isn't already open.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_hold_trait_notifications",
        "description": "Context manager for bundling trait change notifications and cross\nvalidation.\nUse this when doing multiple trait assignments (init, config), to avoid\nrace conditions in trait notifiers requesting other trait values.\nAll trait notifications will fire after all values have been assigned.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_write_html",
        "description": "Write a figure to an HTML file representation\nParameters\n----------\nfile: str or writeable\nA string representing a local file path or a writeable object\n(e.g. a pathlib.Path object or an open file descriptor)\nconfig: dict or None (default None)\nPlotly.js figure config options\nauto_play: bool (default=True)\nWhether to automatically start the animation sequence on page load\nif the figure contains frames. Has no effect if the figure does not\ncontain frames.\ninclude_plotlyjs: bool or string (default True)\nSpecifies how the plotly.js library is included/loaded in the output\ndiv string.\nIf True, a script tag containing the plotly.js source code (~3MB)\nis included in the output.  HTML files generated with this option are\nfully self-contained and can be used offline.\nIf 'cdn', a script tag that references the plotly.js CDN is included\nin the output. HTML files generated with this option are about 3MB\nsmaller than those generated with include_plotlyjs=True, but they\nrequire an active internet connection in order to load the plotly.js\nlibrary.\nIf 'directory', a script tag is included that references an external\nplotly.min.js bundle that is assumed to reside in the same\ndirectory as the HTML file. If `file` is a string to a local file path\nand `full_html` is True then\nIf 'directory', a script tag is included that references an external\nplotly.min.js bundle that is assumed to reside in the same\ndirectory as the HTML file.  If `file` is a string to a local file\npath and `full_html` is True, then the plotly.min.js bundle is copied\ninto the directory of the resulting HTML file. If a file named\nplotly.min.js already exists in the output directory then this file\nis left unmodified and no copy is performed. HTML files generated\nwith this option can be used offline, but they require a copy of\nthe plotly.min.js bundle in the same directory. This option is\nuseful when many figures will be saved as HTML files in the same\ndirectory because the plotly.js source code will be included only\nonce per output directory, rather than once per output file.\nIf 'require', Plotly.js is loaded using require.js.  This option\nassumes that require.js is globally available and that it has been\nglobally configured to know how to find Plotly.js as 'plotly'.\nThis option is not advised when full_html=True as it will result\nin a non-functional html file.\nIf a string that ends in '.js', a script tag is included that\nreferences the specified path. This approach can be used to point\nthe resulting HTML file to an alternative CDN or local bundle.\nIf False, no script tag referencing plotly.js is included. This is\nuseful when the resulting div string will be placed inside an HTML\ndocument that already loads plotly.js.  This option is not advised\nwhen full_html=True as it will result in a non-functional html file.\ninclude_mathjax: bool or string (default False)\nSpecifies how the MathJax.js library is included in the output html\ndiv string.  MathJax is required in order to display labels\nwith LaTeX typesetting.\nIf False, no script tag referencing MathJax.js will be included in the\noutput.\nIf 'cdn', a script tag that references a MathJax CDN location will be\nincluded in the output.  HTML div strings generated with this option\nwill be able to display LaTeX typesetting as long as internet access\nis available.\nIf a string that ends in '.js', a script tag is included that\nreferences the specified path. This approach can be used to point the\nresulting HTML div string to an alternative CDN.\npost_script: str or list or None (default None)\nJavaScript snippet(s) to be included in the resulting div just after\nplot creation.  The string(s) may include '{plot_id}' placeholders\nthat will then be replaced by the `id` of the div element that the\nplotly.js figure is associated with.  One application for this script\nis to install custom plotly.js event handlers.\nfull_html: bool (default True)\nIf True, produce a string containing a complete HTML document\nstarting with an <html> tag.  If False, produce a string containing\na single <div> element.\nanimation_opts: dict or None (default None)\ndict of custom animation parameters to be passed to the function\nPlotly.animate in Plotly.js. See\nhttps://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js\nfor available options. Has no effect if the figure does not contain\nframes, or auto_play is False.\ndefault_width, default_height: number or str (default '100%')\nThe default figure width/height to use if the provided figure does not\nspecify its own layout.width/layout.height property.  May be\nspecified in pixels as an integer (e.g. 500), or as a css width style\nstring (e.g. '500px', '100%').\nvalidate: bool (default True)\nTrue if the figure should be validated before being converted to\nJSON, False otherwise.\nauto_open: bool (default True)\nIf True, open the saved file in a web browser after saving.\nThis argument only applies if `full_html` is True.\ndiv_id: str (default None)\nIf provided, this is the value of the id attribute of the div tag. If None, the\nid attribute is a UUID.\nReturns\n-------\nstr\nRepresentation of figure as an HTML div string",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_vline",
        "description": "Add a vertical line to a plot or subplot that extends infinitely in the\ny-dimension.\nParameters\n----------\nx: float or int\nA number representing the x coordinate of the vertical line.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the line. Example positions are \"bottom left\", \"right top\",\n\"right\", \"bottom\". If an annotation is added but annotation_position is\nnot specified, this defaults to \"top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "x",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_add_hline",
        "description": "Add a horizontal line to a plot or subplot that extends infinitely in the\nx-dimension.\nParameters\n----------\ny: float or int\nA number representing the y coordinate of the horizontal line.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the line. Example positions are \"bottom left\", \"right top\",\n\"right\", \"bottom\". If an annotation is added but annotation_position is\nnot specified, this defaults to \"top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "y": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "y",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_trait_values",
        "description": "A ``dict`` of trait names and their values.\nThe metadata kwargs allow functions to be passed in which\nfilter traits based on metadata values.  The functions should\ntake a single value as an argument and return a boolean.  If\nany function returns False, then the trait is not included in\nthe output.  If a metadata key doesn't exist, None will be passed\nto the function.\nReturns\n-------\nA ``dict`` of trait names and their values.\nNotes\n-----\nTrait values are retrieved via ``getattr``, any exceptions raised\nby traits or the operations they may trigger will result in the\nabsence of a trait value in the result ``dict``.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "metadata": {
                    "type": "object",
                    "description": "类型从参数名推断: metadata"
                }
            },
            "required": [
                "metadata"
            ]
        }
    },
    {
        "name": "plotly_basedatatypes_BaseFigure_get_subplot",
        "description": "Return an object representing the subplot at the specified row\nand column.  May only be used on Figures created using\nplotly.tools.make_subplots\nParameters\n----------\nrow: int\n1-based index of subplot row\ncol: int\n1-based index of subplot column\nsecondary_y: bool\nIf True, select the subplot that consists of the x-axis and the\nsecondary y-axis at the specified row/col. Only valid if the\nsubplot at row/col is an 2D cartesian subplot that was created\nwith a secondary y-axis.  See the docstring for the specs argument\nto make_subplots for more info on creating a subplot with a\nsecondary y-axis.\nReturns\n-------\nsubplot\n* None: if subplot is empty\n* plotly.graph_objs.layout.Scene: if subplot type is 'scene'\n* plotly.graph_objs.layout.Polar: if subplot type is 'polar'\n* plotly.graph_objs.layout.Ternary: if subplot type is 'ternary'\n* plotly.graph_objs.layout.Mapbox: if subplot type is 'ternary'\n* SubplotDomain namedtuple with `x` and `y` fields:\nif subplot type is 'domain'.\n- x: length 2 list of the subplot start and stop width\n- y: length 2 list of the subplot start and stop height\n* SubplotXY namedtuple with `xaxis` and `yaxis` fields:\nif subplot type is 'xy'.\n- xaxis: plotly.graph_objs.layout.XAxis instance for subplot\n- yaxis: plotly.graph_objs.layout.YAxis instance for subplot",
        "inputSchema": {
            "type": "object",
            "properties": {
                "row": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "col": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "secondary_y": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": [
                "row",
                "col"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_update_layout",
        "description": "Update the properties of the figure's layout with a dict and/or with\nkeyword arguments.\nThis recursively updates the structure of the original\nlayout with the values in the input dict / keyword arguments.\nParameters\n----------\ndict1 : dict\nDictionary of properties to be updated\noverwrite: bool\nIf True, overwrite existing properties. If False, apply updates\nto existing properties recursively, preserving existing\nproperties that are not specified in the update operation.\nkwargs :\nKeyword/value pair of properties to be updated\nReturns\n-------\nBaseFigure\nThe Figure object that the update_layout method was called on",
        "inputSchema": {
            "type": "object",
            "properties": {
                "dict1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "overwrite": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_missing_ipywidgets_FigureWidget_write_json",
        "description": "Convert a figure to JSON and write it to a file or writeable\nobject\nParameters\n----------\nfile: str or writeable\nA string representing a local file path or a writeable object\n(e.g. an open file descriptor)\npretty: bool (default False)\nTrue if JSON representation should be pretty-printed, False if\nrepresentation should be as compact as possible.\nremove_uids: bool (default True)\nTrue if trace UIDs should be omitted from the JSON representation\nengine: str (default None)\nThe JSON encoding engine to use. One of:\n- \"json\" for an encoder based on the built-in Python json module\n- \"orjson\" for a fast encoder the requires the orjson package\nIf not specified, the default encoder is set to the current value of\nplotly.io.json.config.default_encoder.\nReturns\n-------\nNone",
        "inputSchema": {
            "type": "object",
            "properties": {
                "args": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "args",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_matplotlylib_mpltools_get_spine_visible",
        "description": "Return some spine parameters for the spine, `spine_key`.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "ax": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "spine_key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "ax",
                "spine_key"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_add_vrect",
        "description": "Add a rectangle to a plot or subplot that extends infinitely in the\ny-dimension.\nParameters\n----------\nx0: float or int\nA number representing the x coordinate of one side of the rectangle.\nx1: float or int\nA number representing the x coordinate of the other side of the rectangle.\nexclude_empty_subplots: Boolean\nIf True (default) do not place the shape on subplots that have no data\nplotted on them.\nrow: None, int or 'all'\nSubplot row for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\ncol: None, int or 'all'\nSubplot column for shape indexed starting at 1. If 'all', addresses all rows in\nthe specified column(s). If both row and col are None, addresses the\nfirst subplot if subplots exist, or the only plot. By default is \"all\".\nannotation: dict or plotly.graph_objects.layout.Annotation. If dict(),\nit is interpreted as describing an annotation. The annotation is\nplaced relative to the shape based on annotation_position (see\nbelow) unless its x or y value has been specified for the annotation\npassed here. xref and yref are always the same as for the added\nshape and cannot be overridden.\nannotation_position: a string containing optionally [\"inside\", \"outside\"], [\"top\", \"bottom\"]\nand [\"left\", \"right\"] specifying where the text should be anchored\nto on the rectangle. Example positions are \"outside top left\", \"inside\nbottom\", \"right\", \"inside left\", \"inside\" (\"outside\" is not supported). If\nan annotation is added but annotation_position is not specified this\ndefaults to \"inside top right\".\nannotation_*: any parameters to go.layout.Annotation can be passed as\nkeywords by prefixing them with \"annotation_\". For example, to specify the\nannotation text \"example\" you can pass annotation_text=\"example\" as a\nkeyword argument.\n**kwargs:\nAny named function parameters that can be passed to 'add_shape',\nexcept for x0, x1, y0, y1 or type.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "x0": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "x1": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "row": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "col": {
                    "type": "string",
                    "default": "all",
                    "description": "类型从默认值推断: str"
                },
                "exclude_empty_subplots": {
                    "type": "integer",
                    "default": True,
                    "description": "类型从默认值推断: bool"
                },
                "annotation": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "kwargs": {
                    "type": "object",
                    "description": "类型从参数名推断: kwargs"
                }
            },
            "required": [
                "x0",
                "x1",
                "kwargs"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_handle_comm_opened",
        "description": "Static method, called when a widget is constructed.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "comm": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "msg": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                }
            },
            "required": [
                "comm",
                "msg"
            ]
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_to_plotly_json",
        "description": "Convert figure to a JSON representation as a Python dict\n\nNote: May include some JSON-invalid data types, use the `PlotlyJSONEncoder` util\nor the `to_json` method to encode to a string.\n\nReturns\n-------\ndict",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "plotly_basewidget_BaseFigureWidget_get_state",
        "description": "Gets the widget state, or a piece of it.\nParameters\n----------\nkey : unicode or iterable (optional)\nA single property's name or iterable of property names to get.\nReturns\n-------\nstate : dict of states\nmetadata : dict\nmetadata for each field: {key: metadata}",
        "inputSchema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "description": "未知类型，默认为字符串"
                },
                "drop_defaults": {
                    "type": "integer",
                    "default": False,
                    "description": "类型从默认值推断: bool"
                }
            },
            "required": []
        }
    }
]


def handle_plotly_basewidget_BaseFigureWidget_show(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_show 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.show
        parts = "plotly.basewidget.BaseFigureWidget.show".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.show")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_show 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_observe(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_observe 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.observe
        parts = "plotly.basewidget.BaseFigureWidget.observe".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.observe")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_observe 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_on_edits_completed(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_on_edits_completed 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.on_edits_completed
        parts = "plotly.basewidget.BaseFigureWidget.on_edits_completed".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.on_edits_completed")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_on_edits_completed 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_trait_defaults(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_trait_defaults 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.trait_defaults
        parts = "plotly.basewidget.BaseFigureWidget.trait_defaults".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.trait_defaults")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_trait_defaults 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_trace 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_trace
        parts = "plotly.basewidget.BaseFigureWidget.add_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_pop(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_pop 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.pop
        parts = "plotly.basewidget.BaseFigureWidget.pop".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.pop")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_pop 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_batch_update(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_batch_update 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.batch_update
        parts = "plotly.basewidget.BaseFigureWidget.batch_update".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.batch_update")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_batch_update 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_print_grid(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_print_grid 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.print_grid
        parts = "plotly.basewidget.BaseFigureWidget.print_grid".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.print_grid")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_print_grid 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_vrect(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_vrect 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_vrect
        parts = "plotly.missing_ipywidgets.FigureWidget.add_vrect".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_vrect")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_vrect 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_plotly_update(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_plotly_update 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.plotly_update
        parts = "plotly.basewidget.BaseFigureWidget.plotly_update".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.plotly_update")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_plotly_update 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_on_widget_constructed(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_on_widget_constructed 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.on_widget_constructed
        parts = "plotly.basewidget.BaseFigureWidget.on_widget_constructed".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.on_widget_constructed")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_on_widget_constructed 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_batch_animate(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_batch_animate 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.batch_animate
        parts = "plotly.missing_ipywidgets.FigureWidget.batch_animate".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.batch_animate")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_batch_animate 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_trait_names(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_trait_names 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.trait_names
        parts = "plotly.basewidget.BaseFigureWidget.trait_names".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.trait_names")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_trait_names 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mplexporter_utils_get_axis_properties(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mplexporter_utils_get_axis_properties 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mplexporter.utils.get_axis_properties
        parts = "plotly.matplotlylib.mplexporter.utils.get_axis_properties".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mplexporter.utils.get_axis_properties")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mplexporter_utils_get_axis_properties 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_vline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_vline 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_vline
        parts = "plotly.missing_ipywidgets.FigureWidget.add_vline".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_vline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_vline 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_send_state(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_send_state 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.send_state
        parts = "plotly.basewidget.BaseFigureWidget.send_state".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.send_state")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_send_state 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_update(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_update 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.update
        parts = "plotly.basewidget.BaseFigureWidget.update".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.update")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_update 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_unobserve(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_unobserve 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.unobserve
        parts = "plotly.basewidget.BaseFigureWidget.unobserve".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.unobserve")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_unobserve 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_hold_sync(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_hold_sync 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.hold_sync
        parts = "plotly.basewidget.BaseFigureWidget.hold_sync".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.hold_sync")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_hold_sync 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mplexporter_utils_get_marker_style(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mplexporter_utils_get_marker_style 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mplexporter.utils.get_marker_style
        parts = "plotly.matplotlylib.mplexporter.utils.get_marker_style".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mplexporter.utils.get_marker_style")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mplexporter_utils_get_marker_style 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_for_each_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_for_each_trace 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.for_each_trace
        parts = "plotly.basewidget.BaseFigureWidget.for_each_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.for_each_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_for_each_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_class(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_class 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_class
        parts = "plotly.basewidget.BaseFigureWidget.add_class".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_class")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_class 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_get_manager_state(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_get_manager_state 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.get_manager_state
        parts = "plotly.basewidget.BaseFigureWidget.get_manager_state".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.get_manager_state")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_get_manager_state 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_select_traces(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_select_traces 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.select_traces
        parts = "plotly.basewidget.BaseFigureWidget.select_traces".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.select_traces")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_select_traces 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_close(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_close 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.close
        parts = "plotly.basewidget.BaseFigureWidget.close".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.close")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_close 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_batch_animate(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_batch_animate 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.batch_animate
        parts = "plotly.basewidget.BaseFigureWidget.batch_animate".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.batch_animate")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_batch_animate 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_traces(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_traces 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_traces
        parts = "plotly.missing_ipywidgets.FigureWidget.add_traces".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_traces")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_traces 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_get_subplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_get_subplot 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.get_subplot
        parts = "plotly.basewidget.BaseFigureWidget.get_subplot".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.get_subplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_get_subplot 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_hline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_hline 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_hline
        parts = "plotly.basewidget.BaseFigureWidget.add_hline".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_hline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_hline 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_get_subplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_get_subplot 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.get_subplot
        parts = "plotly.missing_ipywidgets.FigureWidget.get_subplot".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.get_subplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_get_subplot 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_on_msg(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_on_msg 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.on_msg
        parts = "plotly.basewidget.BaseFigureWidget.on_msg".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.on_msg")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_on_msg 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_on_trait_change(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_on_trait_change 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.on_trait_change
        parts = "plotly.basewidget.BaseFigureWidget.on_trait_change".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.on_trait_change")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_on_trait_change 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_full_figure_for_development(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_full_figure_for_development 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.full_figure_for_development
        parts = "plotly.missing_ipywidgets.FigureWidget.full_figure_for_development".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.full_figure_for_development")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_full_figure_for_development 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_to_image(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_to_image 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.to_image
        parts = "plotly.basewidget.BaseFigureWidget.to_image".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.to_image")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_to_image 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_to_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_to_json 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.to_json
        parts = "plotly.basewidget.BaseFigureWidget.to_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.to_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_to_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_batch_update(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_batch_update 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.batch_update
        parts = "plotly.missing_ipywidgets.FigureWidget.batch_update".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.batch_update")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_batch_update 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_for_each_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_for_each_trace 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.for_each_trace
        parts = "plotly.missing_ipywidgets.FigureWidget.for_each_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.for_each_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_for_each_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_unobserve_all(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_unobserve_all 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.unobserve_all
        parts = "plotly.basewidget.BaseFigureWidget.unobserve_all".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.unobserve_all")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_unobserve_all 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mpltools_get_axes_bounds(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mpltools_get_axes_bounds 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mpltools.get_axes_bounds
        parts = "plotly.matplotlylib.mpltools.get_axes_bounds".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mpltools.get_axes_bounds")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mpltools_get_axes_bounds 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_trace 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_trace
        parts = "plotly.missing_ipywidgets.FigureWidget.add_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_update_traces(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_update_traces 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.update_traces
        parts = "plotly.basewidget.BaseFigureWidget.update_traces".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.update_traces")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_update_traces 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_traits(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_traits 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.traits
        parts = "plotly.basewidget.BaseFigureWidget.traits".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.traits")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_traits 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_traces(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_traces 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_traces
        parts = "plotly.basewidget.BaseFigureWidget.add_traces".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_traces")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_traces 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_append_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_append_trace 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.append_trace
        parts = "plotly.basewidget.BaseFigureWidget.append_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.append_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_append_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_to_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_to_json 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.to_json
        parts = "plotly.missing_ipywidgets.FigureWidget.to_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.to_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_to_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_send(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_send 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.send
        parts = "plotly.basewidget.BaseFigureWidget.send".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.send")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_send 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_hrect(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_hrect 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_hrect
        parts = "plotly.missing_ipywidgets.FigureWidget.add_hrect".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_hrect")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_hrect 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_has_trait(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_has_trait 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.has_trait
        parts = "plotly.basewidget.BaseFigureWidget.has_trait".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.has_trait")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_has_trait 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_remove_class(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_remove_class 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.remove_class
        parts = "plotly.basewidget.BaseFigureWidget.remove_class".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.remove_class")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_remove_class 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_write_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_write_json 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.write_json
        parts = "plotly.basewidget.BaseFigureWidget.write_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.write_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_write_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_set_subplots(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_set_subplots 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.set_subplots
        parts = "plotly.basewidget.BaseFigureWidget.set_subplots".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.set_subplots")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_set_subplots 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_pop(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_pop 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.pop
        parts = "plotly.missing_ipywidgets.FigureWidget.pop".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.pop")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_pop 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_trait_has_value(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_trait_has_value 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.trait_has_value
        parts = "plotly.basewidget.BaseFigureWidget.trait_has_value".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.trait_has_value")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_trait_has_value 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_to_html(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_to_html 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.to_html
        parts = "plotly.basewidget.BaseFigureWidget.to_html".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.to_html")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_to_html 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_full_figure_for_development(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_full_figure_for_development 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.full_figure_for_development
        parts = "plotly.basewidget.BaseFigureWidget.full_figure_for_development".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.full_figure_for_development")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_full_figure_for_development 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_hrect(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_hrect 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_hrect
        parts = "plotly.basewidget.BaseFigureWidget.add_hrect".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_hrect")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_hrect 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_to_plotly_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_to_plotly_json 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.to_plotly_json
        parts = "plotly.missing_ipywidgets.FigureWidget.to_plotly_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.to_plotly_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_to_plotly_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_plotly_restyle(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_plotly_restyle 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_restyle
        parts = "plotly.missing_ipywidgets.FigureWidget.plotly_restyle".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_restyle")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_plotly_restyle 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mplexporter_utils_get_line_style(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mplexporter_utils_get_line_style 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mplexporter.utils.get_line_style
        parts = "plotly.matplotlylib.mplexporter.utils.get_line_style".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mplexporter.utils.get_line_style")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mplexporter_utils_get_line_style 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_plotly_relayout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_plotly_relayout 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_relayout
        parts = "plotly.missing_ipywidgets.FigureWidget.plotly_relayout".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_relayout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_plotly_relayout 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_append_trace(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_append_trace 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.append_trace
        parts = "plotly.missing_ipywidgets.FigureWidget.append_trace".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.append_trace")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_append_trace 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_to_dict(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_to_dict 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.to_dict
        parts = "plotly.basewidget.BaseFigureWidget.to_dict".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.to_dict")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_to_dict 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mplexporter_utils_get_path_style(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mplexporter_utils_get_path_style 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mplexporter.utils.get_path_style
        parts = "plotly.matplotlylib.mplexporter.utils.get_path_style".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mplexporter.utils.get_path_style")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mplexporter_utils_get_path_style 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_set_state(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_set_state 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.set_state
        parts = "plotly.basewidget.BaseFigureWidget.set_state".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.set_state")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_set_state 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_plotly_update(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_plotly_update 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_update
        parts = "plotly.missing_ipywidgets.FigureWidget.plotly_update".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.plotly_update")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_plotly_update 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_set_trait(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_set_trait 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.set_trait
        parts = "plotly.basewidget.BaseFigureWidget.set_trait".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.set_trait")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_set_trait 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_trait_metadata(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_trait_metadata 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.trait_metadata
        parts = "plotly.basewidget.BaseFigureWidget.trait_metadata".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.trait_metadata")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_trait_metadata 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_write_image(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_write_image 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.write_image
        parts = "plotly.basewidget.BaseFigureWidget.write_image".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.write_image")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_write_image 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mplexporter_utils_get_dasharray(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mplexporter_utils_get_dasharray 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mplexporter.utils.get_dasharray
        parts = "plotly.matplotlylib.mplexporter.utils.get_dasharray".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mplexporter.utils.get_dasharray")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mplexporter_utils_get_dasharray 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_on_displayed(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_on_displayed 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.on_displayed
        parts = "plotly.basewidget.BaseFigureWidget.on_displayed".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.on_displayed")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_on_displayed 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_plotly_relayout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_plotly_relayout 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.plotly_relayout
        parts = "plotly.basewidget.BaseFigureWidget.plotly_relayout".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.plotly_relayout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_plotly_relayout 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_plotly_restyle(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_plotly_restyle 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.plotly_restyle
        parts = "plotly.basewidget.BaseFigureWidget.plotly_restyle".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.plotly_restyle")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_plotly_restyle 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_open(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_open 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.open
        parts = "plotly.basewidget.BaseFigureWidget.open".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.open")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_open 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_hold_trait_notifications(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_hold_trait_notifications 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.hold_trait_notifications
        parts = "plotly.basewidget.BaseFigureWidget.hold_trait_notifications".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.hold_trait_notifications")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_hold_trait_notifications 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_write_html(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_write_html 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.write_html
        parts = "plotly.basewidget.BaseFigureWidget.write_html".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.write_html")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_write_html 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_vline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_vline 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_vline
        parts = "plotly.basewidget.BaseFigureWidget.add_vline".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_vline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_vline 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_add_hline(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_add_hline 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.add_hline
        parts = "plotly.missing_ipywidgets.FigureWidget.add_hline".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.add_hline")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_add_hline 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_trait_values(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_trait_values 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.trait_values
        parts = "plotly.basewidget.BaseFigureWidget.trait_values".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.trait_values")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_trait_values 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basedatatypes_BaseFigure_get_subplot(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basedatatypes_BaseFigure_get_subplot 工具调用"""
    try:
        # 解析函数路径: plotly.basedatatypes.BaseFigure.get_subplot
        parts = "plotly.basedatatypes.BaseFigure.get_subplot".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basedatatypes.BaseFigure.get_subplot")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basedatatypes_BaseFigure_get_subplot 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_update_layout(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_update_layout 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.update_layout
        parts = "plotly.basewidget.BaseFigureWidget.update_layout".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.update_layout")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_update_layout 失败: {e}")
        return {"error": str(e)}


def handle_plotly_missing_ipywidgets_FigureWidget_write_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_missing_ipywidgets_FigureWidget_write_json 工具调用"""
    try:
        # 解析函数路径: plotly.missing_ipywidgets.FigureWidget.write_json
        parts = "plotly.missing_ipywidgets.FigureWidget.write_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.missing_ipywidgets.FigureWidget.write_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_missing_ipywidgets_FigureWidget_write_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_matplotlylib_mpltools_get_spine_visible(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_matplotlylib_mpltools_get_spine_visible 工具调用"""
    try:
        # 解析函数路径: plotly.matplotlylib.mpltools.get_spine_visible
        parts = "plotly.matplotlylib.mpltools.get_spine_visible".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.matplotlylib.mpltools.get_spine_visible")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_matplotlylib_mpltools_get_spine_visible 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_add_vrect(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_add_vrect 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.add_vrect
        parts = "plotly.basewidget.BaseFigureWidget.add_vrect".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.add_vrect")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_add_vrect 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_handle_comm_opened(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_handle_comm_opened 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.handle_comm_opened
        parts = "plotly.basewidget.BaseFigureWidget.handle_comm_opened".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.handle_comm_opened")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_handle_comm_opened 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_to_plotly_json(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_to_plotly_json 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.to_plotly_json
        parts = "plotly.basewidget.BaseFigureWidget.to_plotly_json".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.to_plotly_json")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_to_plotly_json 失败: {e}")
        return {"error": str(e)}


def handle_plotly_basewidget_BaseFigureWidget_get_state(args: Dict[str, Any]) -> Dict[str, Any]:
    """处理 plotly_basewidget_BaseFigureWidget_get_state 工具调用"""
    try:
        # 解析函数路径: plotly.basewidget.BaseFigureWidget.get_state
        parts = "plotly.basewidget.BaseFigureWidget.get_state".split('.')
        
        if parts[0] != "plotly":
            raise ValueError(f"不支持的模块: {parts[0]}")
        
        # 动态导入和调用
        if len(parts) == 2:
            # plotly.function_name
            func_name = parts[1]
            func = getattr(plotly, func_name)
        elif len(parts) >= 3:
            # plotly.module.function_name
            module_path = '.'.join(parts[:-1])
            func_name = parts[-1]
            
            import importlib
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
        else:
            raise ValueError(f"无效的函数路径: plotly.basewidget.BaseFigureWidget.get_state")
        
        # 处理参数
        processed_args = {}
        processed_kwargs = {}
        
        for key, value in args.items():
            if key == 'kwargs' and isinstance(value, dict):
                processed_kwargs.update(value)
            else:
                processed_args[key] = value
        
        # 调用函数
        if processed_kwargs:
            result = func(**processed_args, **processed_kwargs)
        else:
            result = func(**processed_args)
        
        # 处理返回值
        if hasattr(result, '__dict__'):
            return vars(result)
        elif hasattr(result, '_asdict'):  # namedtuple
            return result._asdict()
        else:
            return {"result": str(result)}
            
    except Exception as e:
        logger.error(f"执行 plotly_basewidget_BaseFigureWidget_get_state 失败: {e}")
        return {"error": str(e)}


def process_mcp_request(request_line: str) -> str:
    """处理 MCP 请求"""
    try:
        request = json.loads(request_line.strip())
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")
        
        if method == "initialize":
            # MCP 初始化请求
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                        "logging": {},
                        "prompts": {},
                        "resources": {}
                    },
                    "serverInfo": {
                        "name": "plotly-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
        elif method == "notifications/initialized":
            # 初始化完成通知，不需要响应
            return ""
        elif method == "tools/list":
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"tools": TOOLS}
            }
        elif method == "tools/call":
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            
            # 调用对应的处理函数
            handler_name = f"handle_{tool_name}"
            if handler_name in globals():
                result = globals()[handler_name](arguments)
            else:
                result = {"error": f"未找到工具处理器: {tool_name}"}
            
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }
                    ]
                }
            }
        else:
            response = {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": f"未知方法: {method}"
                }
            }
        
        return json.dumps(response)
    
    except Exception as e:
        logger.error(f"处理请求失败: {e}")
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": -32603,
                "message": f"内部错误: {str(e)}"
            }
        })

async def main():
    """主函数 - MCP 服务器模式"""
    logger.info("启动 plotly MCP 服务器...")
    
    try:
        # 读取 stdin 并处理请求
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                line = line.strip()
                if line:
                    logger.debug(f"收到请求: {line}")
                    response = process_mcp_request(line)
                    if response:  # 只有当有响应时才输出
                        print(response, flush=True)
                        logger.debug(f"发送响应: {response}")
                        
            except EOFError:
                # 正常的输入结束
                break
            except Exception as e:
                logger.error(f"处理请求时出错: {e}")
                error_response = json.dumps({
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32603,
                        "message": f"内部错误: {str(e)}"
                    }
                })
                print(error_response, flush=True)
                
    except KeyboardInterrupt:
        logger.info("服务器停止")
    except Exception as e:
        logger.error(f"服务器错误: {e}")
    finally:
        logger.info("服务器关闭")

def cli_mode():
    """命令行模式 - 用于测试"""
    if len(sys.argv) < 3:
        print(json.dumps({"error": "参数不足，需要: 工具名 参数JSON"}))
        return
    
    tool_name = sys.argv[1]
    try:
        arguments = json.loads(sys.argv[2])
    except json.JSONDecodeError:
        print(json.dumps({"error": "参数格式错误"}))
        return
    
    # 调用对应的处理函数
    handler_name = f"handle_{tool_name}"
    if handler_name in globals():
        result = globals()[handler_name](arguments)
    else:
        result = {"error": f"未找到工具: {tool_name}"}
    
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        cli_mode()
    else:
        # MCP 服务器模式
        asyncio.run(main())
