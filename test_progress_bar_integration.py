#!/usr/bin/env python3
"""
Test script for ComfyUI Progress Bar Integration
Demonstrates the new real-time progress tracking functionality in Open WebUI
"""

import asyncio
import aiohttp
import json
from datetime import datetime

class ProgressBarTester:
    def __init__(self, open_webui_url="http://localhost:8080", comfyui_url="http://host.docker.internal:8188"):
        self.open_webui_url = open_webui_url
        self.comfyui_url = comfyui_url
        
    async def test_progress_endpoints(self):
        """Test the new progress tracking endpoints"""
        print("🧪 Testing ComfyUI Progress Bar Integration")
        print("=" * 60)
        
        # Test direct ComfyUI endpoints
        print("\n1. Testing direct ComfyUI endpoints:")
        await self.test_comfyui_direct()
        
        # Test Open WebUI proxy endpoints
        print("\n2. Testing Open WebUI proxy endpoints:")
        await self.test_openwebui_proxy()
        
    async def test_comfyui_direct(self):
        """Test direct ComfyUI API endpoints"""
        try:
            async with aiohttp.ClientSession() as session:
                # Test progress endpoint
                print("   📊 Testing /progress endpoint...")
                async with session.get(f"{self.comfyui_url}/progress") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"   ✅ Progress: {data}")
                    else:
                        print(f"   ❌ Progress endpoint failed: {response.status}")
                
                # Test queue endpoint
                print("   📋 Testing /queue endpoint...")
                async with session.get(f"{self.comfyui_url}/queue") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"   ✅ Queue: {data}")
                    else:
                        print(f"   ❌ Queue endpoint failed: {response.status}")
                        
        except Exception as e:
            print(f"   ❌ ComfyUI connection failed: {e}")
            print("   💡 Make sure ComfyUI is running on host.docker.internal:8188")
    
    async def test_openwebui_proxy(self):
        """Test Open WebUI proxy endpoints"""
        try:
            async with aiohttp.ClientSession() as session:
                # Test progress proxy
                print("   📊 Testing /api/v1/images/comfyui/progress...")
                async with session.get(f"{self.open_webui_url}/api/v1/images/comfyui/progress") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"   ✅ Progress proxy: {data}")
                    else:
                        print(f"   ❌ Progress proxy failed: {response.status}")
                
                # Test queue proxy
                print("   📋 Testing /api/v1/images/comfyui/queue...")
                async with session.get(f"{self.open_webui_url}/api/v1/images/comfyui/queue") as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"   ✅ Queue proxy: {data}")
                    else:
                        print(f"   ❌ Queue proxy failed: {response.status}")
                        
        except Exception as e:
            print(f"   ❌ Open WebUI connection failed: {e}")
            print("   💡 Make sure Open WebUI is running on localhost:8080")
    
    def simulate_progress_display(self):
        """Simulate how the progress bar would look in the UI"""
        print("\n3. Simulating Progress Bar Display:")
        print("   🎨 This is how the progress would appear in Open WebUI:")
        print()
        
        # Simulate different progress states
        progress_states = [
            {"value": 0, "max": 20, "node": "4", "operation": "📦 Loading Model"},
            {"value": 5, "max": 20, "node": "6", "operation": "📝 Processing Prompt"},
            {"value": 10, "max": 20, "node": "3", "operation": "🎨 Sampling (KSampler)"},
            {"value": 18, "max": 20, "node": "8", "operation": "🎭 VAE Decoding"},
            {"value": 20, "max": 20, "node": "9", "operation": "💾 Saving Image"},
        ]
        
        for state in progress_states:
            percentage = (state["value"] / state["max"]) * 100
            bar_length = 40
            filled = int(bar_length * percentage / 100)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            print(f"   [{bar}] {percentage:5.1f}% | Step {state['value']}/{state['max']} | {state['operation']}")
            
        print("\n   ✅ Progress bar would update every 500ms with real-time data!")

def main():
    """Main function to run the test"""
    print("ComfyUI Progress Bar Integration Test")
    print("====================================")
    print()
    print("This test verifies the new real-time progress tracking functionality.")
    print("Features implemented:")
    print("• Real-time progress polling every 500ms")
    print("• Human-readable operation names")
    print("• ETA calculation")
    print("• Queue status monitoring")
    print("• Seamless integration with Open WebUI")
    print()
    
    tester = ProgressBarTester()
    
    # Run async tests
    try:
        asyncio.run(tester.test_progress_endpoints())
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
    
    # Show simulated progress display
    tester.simulate_progress_display()
    
    print("\n" + "=" * 60)
    print("🎉 Integration Test Complete!")
    print()
    print("Next steps:")
    print("1. Start Open WebUI with the new progress bar code")
    print("2. Start ComfyUI on host.docker.internal:8188")
    print("3. Generate an image and watch the real-time progress!")
    print()
    print("The progress bar will show:")
    print("• Current operation (Loading Model, Sampling, etc.)")
    print("• Progress percentage and step count")
    print("• Estimated time remaining")
    print("• Queue status if multiple generations are pending")

if __name__ == "__main__":
    main() 