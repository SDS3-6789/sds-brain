"""The plugin shares the canonical MCP schema, validation and scope checks."""
from __future__ import annotations


def definitions(server, brain):
    return server.tools_for(brain)


def invoke(server, brain, name, arguments):
    return server.call(brain, name, arguments)


def session(server, brain):
    return server.Session(brain)
