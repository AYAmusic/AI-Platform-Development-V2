# 🔑 Quick Start: API Key Setup & Development Assistant

## ✅ **What We Accomplished**

1. **✅ Found API Key Settings** - Located in Settings → Account → API Keys
2. **✅ Generated New API Key** - Successfully created: `sk-a73f6a84251745deb8611d0c744ede08`
3. **✅ Built Development Assistant** - Complete monitoring system ready to use

---

## 🚀 **Next Steps: Set Up Environment Variable**

### **Option 1: Terminal Session (Quick Test)**
Open your terminal and run:
```bash
export OPENWEBUI_API_KEY="sk-a73f6a84251745deb8611d0c744ede08"
```

### **Option 2: Permanent Setup (Recommended)**

#### **For Zsh (your shell):**
```bash
echo 'export OPENWEBUI_API_KEY="sk-a73f6a84251745deb8611d0c744ede08"' >> ~/.zshrc
source ~/.zshrc
```

#### **For Bash:**
```bash
echo 'export OPENWEBUI_API_KEY="sk-a73f6a84251745deb8611d0c744ede08"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🧪 **Test the Setup**

### **1. Run the Setup Script:**
```bash
cd "Open WebUI + Playwright"
python setup/setup_dev_assistant.py
```

### **2. Quick Test:**
```bash
python -c "
import os
print('API Key:', os.getenv('OPENWEBUI_API_KEY', 'NOT FOUND'))
"
```

### **3. Run Development Assistant:**
```bash
python examples/dev_assistant_monitor.py
```

---

## 🎯 **What the Development Assistant Does**

### **Your "Eyes and Ears" System:**

1. **🔍 UI Monitoring**
   - Takes screenshots at each step
   - Analyzes page elements and layout
   - Monitors console logs and errors
   - Tracks performance metrics

2. **🤖 AI Interaction Testing**
   - Executes prompts via reliable API calls
   - Measures response times
   - Analyzes response quality
   - No browser crashes (uses API instead of UI)

3. **📊 Comprehensive Reporting**
   - Detailed JSON reports with all data
   - Human-readable summaries
   - Screenshot collections
   - Performance analytics

4. **🔄 Development Feedback Loop**
   - Monitors UI improvements as you develop
   - Tests functionality automatically
   - Provides feedback for faster iteration
   - Helps identify issues early

### **Output Locations:**
- **Screenshots**: `dev_assistant_screenshots/`
- **Reports**: `dev_assistant_reports/`
- **Console**: Real-time feedback

---

## 🛠 **Usage Examples**

### **Interactive Mode:**
```bash
python examples/dev_assistant_monitor.py
```

### **Programmatic Usage:**
```python
from examples.dev_assistant_monitor import quick_development_check

# Quick test with custom prompt
report = await quick_development_check("Test the new feature I just built")
```

### **Custom Monitoring:**
```python
async with DevAssistantMonitor() as monitor:
    # Navigate and analyze
    result = await monitor.navigate_and_analyze()

    # Test specific functionality
    result = await monitor.execute_prompt_via_api("Your test prompt")

    # Generate report
    report = await monitor.generate_comprehensive_report()
```

---

## 🎉 **Benefits for Development**

✅ **Faster Iteration** - See exactly how your changes affect the UI
✅ **Reliable Testing** - No more browser crashes during AI interactions
✅ **Comprehensive Feedback** - Full visibility into what's happening
✅ **Performance Insights** - Track load times and response speeds
✅ **Error Detection** - Catch issues before they become problems
✅ **Development History** - Track improvements over time

---

## 🚨 **Troubleshooting**

### **API Key Issues:**
```bash
# Check if set correctly
echo $OPENWEBUI_API_KEY

# Should show: sk-a73f6a84251745deb8611d0c744ede08
```

### **Open WebUI Not Running:**
```bash
# Make sure Open WebUI is accessible at:
curl http://localhost:3000
```

### **Dependencies Missing:**
```bash
pip install playwright aiohttp
playwright install chromium
```

---

## 📝 **Your API Key (Save This!):**
```
sk-a73f6a84251745deb8611d0c744ede08
```

**⚠️ Keep this secure - treat it like a password!**

---

Ready to give your development process "eyes and ears"? Run the setup script and let's see your Open WebUI through AI assistant eyes! 🤖👀
