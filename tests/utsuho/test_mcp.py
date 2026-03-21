"""
Tests for the Utsuho MCP server tools.
"""

import pytest
from fastmcp import Client

from utsuho.mcp import main, mcp


class TestMCP:
    """
    Tests for the Utsuho MCP server.
    """

    @pytest.mark.asyncio
    async def test_mcp_lists_tools(self):
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


class TestHalfToFull:
    """
    Tests for the half_to_full MCP tool.
    """

    @pytest.mark.asyncio
    async def test_mcp_half_to_full(self):
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
    async def test_mcp_half_to_full_with_config(self):
        """
        Verify half-width to full-width conversion with MCP width options.
        """
        async with Client(mcp) as client:
            result = await client.call_tool(
                "half_to_full",
                {
                    "text": "ｷﾞﾝｶｸｼﾞ 2F",
                    "ascii_digit": False,
                    "ascii_alphabet": False,
                },
            )
            assert result.data == "ギンカクジ　2F"


class TestFullToHalf:
    """
    Tests for the full_to_half MCP tool.
    """

    @pytest.mark.asyncio
    async def test_mcp_full_to_half(self):
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
    async def test_mcp_full_to_half_with_config(self):
        """
        Verify full-width to half-width conversion with MCP width options.
        """
        async with Client(mcp) as client:
            result = await client.call_tool(
                "full_to_half",
                {
                    "text": "ギンカクジ　２Ｆ〜",
                    "ascii_digit": False,
                    "ascii_alphabet": False,
                    "wave_dash": True,
                },
            )
            assert result.data == "ｷﾞﾝｶｸｼﾞ ２Ｆ~"


class TestHiragaToKatakana:
    """
    Tests for the hiragana_to_katakana MCP tool.
    """

    @pytest.mark.asyncio
    async def test_mcp_hiragana_to_katakana(self):
        """
        Verify hiragana to katakana conversion via the MCP client.
        """
        async with Client(mcp) as client:
            result = await client.call_tool(
                "hiragana_to_katakana",
                {"text": "きょうとし　さきょうく　ぎんかくじちょう　２"},
            )
            assert result.data == "キョウトシ　サキョウク　ギンカクジチョウ　２"


class TestKatakanaToHiragana:
    """
    Tests for the katakana_to_hiragana MCP tool.
    """

    @pytest.mark.asyncio
    async def test_mcp_katakana_to_hiragana(self):
        """
        Verify katakana to hiragana conversion via the MCP client.
        """
        async with Client(mcp) as client:
            result = await client.call_tool(
                "katakana_to_hiragana",
                {"text": "キョウトシ　サキョウク　ギンカクジチョウ　２"},
            )
            assert result.data == "きょうとし　さきょうく　ぎんかくじちょう　２"


class TestMCPMain:
    """
    Tests for the main function of the MCP server.
    """

    def test_mcp_main(self, mocker):
        """
        Verify that the MCP server starts with the expected stdio options.
        """
        run_mock = mocker.patch.object(mcp, "run")

        main()

        run_mock.assert_called_once_with(
            transport="stdio",
            log_level="WARNING",
            show_banner=False,
        )
