#!/usr/bin/env python3
"""
Test script for ComfyUI Progress Bar Integration
Placed under tests/ so pytest can auto-discover it in CI.
"""

import asyncio
import aiohttp

class ProgressBarTester:
    def __init__(self, open_webui_url="http://localhost:8080", comfyui_url="http://host.docker.internal:8188"):
        self.open_webui_url = open_webui_url
        self.comfyui_url = comfyui_url

    async def test_proxy_progress(self):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.open_webui_url}/api/v1/images/comfyui/progress") as r:
                assert r.status == 200, "/progress proxy failed"

    async def test_proxy_queue(self):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"{self.open_webui_url}/api/v1/images/comfyui/queue") as r:
                assert r.status == 200, "/queue proxy failed"


import pytest

@pytest.mark.asyncio
async def test_progress_and_queue():
    tester = ProgressBarTester()
    await tester.test_proxy_progress()
    await tester.test_proxy_queue() 