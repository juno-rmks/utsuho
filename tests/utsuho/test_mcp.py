"""
Tests for the Utsuho MCP server tools.
"""

import pytest
from fastmcp import Client

from utsuho.mcp import mcp


@pytest.mark.asyncio
async def test_mcp_lists_tools():
    """
    Verify that the MCP server exposes the expected tool set.
    """
    async with Client(mcp) as client:
        tools = await client.list_tools()
        tool_names = {tool.name for tool in tools}
        assert tool_names == {
            "half_to_full",
            "full_to_half",
            "hiragana_to_katakana",
            "katakana_to_hiragana",
        }


@pytest.mark.asyncio
async def test_mcp_half_to_full():
    """
    Verify half-width to full-width conversion via the MCP client.
    """
    async with Client(mcp) as client:
        result = await client.call_tool(
            "half_to_full",
            {"text": "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"},
        )
        assert result.data == "キョウトシ　サキョウク　ギンカクジチョウ　２"


@pytest.mark.asyncio
async def test_mcp_full_to_half():
    """
    Verify full-width to half-width conversion via the MCP client.
    """
    async with Client(mcp) as client:
        result = await client.call_tool(
            "full_to_half",
            {"text": "キョウトシ　サキョウク　ギンカクジチョウ　２"},
        )
        assert result.data == "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"


@pytest.mark.asyncio
async def test_mcp_hiragana_to_katakana():
    """
    Verify hiragana to katakana conversion via the MCP client."""
    async with Client(mcp) as client:
        result = await client.call_tool(
            "hiragana_to_katakana",
            {"text": "きょうとし　さきょうく　ぎんかくじちょう　２"},
        )
        assert result.data == "キョウトシ　サキョウク　ギンカクジチョウ　２"


@pytest.mark.asyncio
async def test_mcp_katakana_to_hiragana():
    """
    Verify katakana to hiragana conversion via the MCP client.
    """
    async with Client(mcp) as client:
        result = await client.call_tool(
            "katakana_to_hiragana",
            {"text": "キョウトシ　サキョウク　ギンカクジチョウ　２"},
        )
        assert result.data == "きょうとし　さきょうく　ぎんかくじちょう　２"
