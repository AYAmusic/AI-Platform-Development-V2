#!/usr/bin/env python3
"""
Integration test for ComfyUI Progress Bar proxy endpoints.
Placed under tests/ so pytest auto-discovers it.
"""

import aiohttp
import pytest

class ProgressBarTester:
    def __init__(self, open_webui_url: str = "http://localhost:3000", *, comfyui_url: str = "http://host.docker.internal:8188") -> None:
        self.open_webui_url = open_webui_url
        self.comfyui_url = comfyui_url

    async def test_proxy_progress(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.open_webui_url}/api/v1/images/comfyui/progress") as resp:
                assert resp.status == 200, f"/progress proxy failed: {resp.status}"

    async def test_proxy_queue(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.open_webui_url}/api/v1/images/comfyui/queue") as resp:
                assert resp.status == 200, f"/queue proxy failed: {resp.status}"


@pytest.mark.asyncio
async def test_progress_and_queue() -> None:
    tester = ProgressBarTester()
    await tester.test_proxy_progress()
    await tester.test_proxy_queue() 