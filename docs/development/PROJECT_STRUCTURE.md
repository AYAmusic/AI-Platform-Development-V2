# 🏗️ Project Structure Guide

**Complete organization of the AI Platform Development Project**

---

## 📁 **Root Directory Organization**

### **🔒 Files that MUST stay in root:**
- `README.md` - Project entry point (GitHub standard)
- `requirements.txt` - Python dependencies (pip standard)
- `.gitignore` - Git configuration (must be in root)
- `.cursorindexingignore` - Cursor IDE configuration

### **📂 Organized Folders:**

```
AI Platform Development Project/
├── 📚 docs/                           # All documentation
├── 🚀 examples/                       # Automation systems & demos
├── 🔧 setup/                          # Setup & installation utilities
├── ⚙️ config/                         # Configuration files
├── 📜 scripts/                        # Shell scripts & automation
├── 🧪 tests/                          # Test files
├── 📊 dev_assistant_reports/          # Generated reports
├── 📸 dev_assistant_screenshots/      # Generated screenshots
├── 🐍 venv/                           # Python virtual environment
└── 📋 requirements.txt                # Python dependencies
```

---

## 📚 **Documentation Structure** (`docs/`)

**Purpose**: All project documentation organized by function

```
docs/
├── 📋 README.md                       # Master documentation index
├── ⚡ AGENT_QUICK_REFERENCE.md        # Fast navigation for agents
├── 🎯 project/                        # Strategy & Planning
│   └── research-plan-ai-platform.md   # Complete project strategy
├── 🤖 automation/                     # Testing & QA
│   └── HYBRID_AUTONOMOUS_TESTING.md   # Autonomous testing system
├── 🔧 development/                    # Setup & Workflows
│   ├── DEVELOPMENT.md                 # Development progress
│   ├── QUICK_START_API_SETUP.md       # API integration guide
│   └── PROJECT_STRUCTURE.md           # This file
└── 🎓 onboarding/                     # Training & Context
    └── AGENT_ONBOARDING.md            # Agent onboarding protocol
```

**Navigation**: Start with `docs/README.md` for complete index

---

## 🚀 **Examples & Automation** (`examples/`)

**Purpose**: Working automation systems and demonstration code

```
examples/
├── 🎯 hybrid_autonomous_assistant.py  # PRIMARY: Main automation system
├── 🔧 ui_integrated_assistant.py      # Custom Playwright backend
├── 📊 autonomous_test_runner.py       # Legacy test runner
├── ⚡ optimized_ui_assistant.py       # Performance-optimized version
├── 🔄 interactive_dev_assistant.py    # Interactive development tool
├── 🌐 lightweight_api_client.py       # API client utilities
├── 📡 dev_assistant_monitor.py        # Monitoring & logging
└── 🧪 hybrid_playwright_api_demo.py   # API demonstration
```

**Main Entry Point**: `hybrid_autonomous_assistant.py`

---

## 🔧 **Setup Utilities** (`setup/`)

**Purpose**: Installation, configuration, and setup scripts

```
setup/
├── __init__.py                        # Package initialization
├── 🔑 setup_credentials.py            # Credential management
└── 🤖 setup_dev_assistant.py          # Assistant configuration
```

**Usage Examples**:
```bash
# Set up credentials
python setup/setup_credentials.py

# Configure development assistant
python setup/setup_dev_assistant.py
```

---

## ⚙️ **Configuration** (`config/`)

**Purpose**: Configuration files and settings

```
config/
├── __init__.py                        # Package initialization
└── 🔧 config.py                       # Core configuration
```

**Usage**: Import as `from config.config import ...`

---

## 📜 **Scripts** (`scripts/`)

**Purpose**: Shell scripts and system automation

```
scripts/
├── 🔧 setup-dev-env.sh               # Development environment setup
└── 🤖 background-agent-setup.sh      # Background agent configuration
```

**Usage**: Run directly with `./scripts/script-name.sh`

---

## 🧪 **Testing & Reports**

### **Test Files** (`tests/`)
- Unit tests
- Integration tests
- Test configurations

### **Generated Reports** (`dev_assistant_reports/`)
- JSON test reports
- Performance metrics
- Error analysis

### **Screenshots** (`dev_assistant_screenshots/`)
- Visual test evidence
- UI state captures
- Error screenshots

---

## 🎯 **Navigation Guide**

### **For Autonomous Agents**
```bash
# Quick reference
cat docs/AGENT_QUICK_REFERENCE.md

# Complete documentation index
cat docs/README.md

# Run main system
python examples/hybrid_autonomous_assistant.py "your command"

# Setup credentials if needed
python setup/setup_credentials.py
```

### **For Developers**
```bash
# Project overview
cat docs/project/research-plan-ai-platform.md

# Development setup
cat docs/development/DEVELOPMENT.md

# Testing system
cat docs/automation/HYBRID_AUTONOMOUS_TESTING.md

# Project structure (this file)
cat docs/development/PROJECT_STRUCTURE.md
```

### **For New Team Members**
1. **Start**: `README.md` (project overview)
2. **Understand**: `docs/project/research-plan-ai-platform.md` (strategy)
3. **Setup**: `docs/development/DEVELOPMENT.md` (environment)
4. **Learn**: `docs/onboarding/AGENT_ONBOARDING.md` (context)

---

## 🔄 **Maintenance Guidelines**

### **Adding New Files**

1. **Documentation** → `docs/[category]/`
2. **Automation/Examples** → `examples/`
3. **Setup Scripts** → `setup/`
4. **Configuration** → `config/`
5. **Shell Scripts** → `scripts/`

### **Naming Conventions**

- **Documentation**: `UPPERCASE_WITH_UNDERSCORES.md`
- **Python files**: `lowercase_with_underscores.py`
- **Shell scripts**: `lowercase-with-hyphens.sh`
- **Folders**: `lowercase` (no special characters)

### **Import Paths**

```python
# Setup utilities
from setup.setup_credentials import ...

# Configuration
from config.config import ...

# Examples (if importing between examples)
from examples.ui_integrated_assistant import ...
```

---

## 🚀 **Quick Commands Reference**

```bash
# Documentation
ls docs/                              # Browse documentation
cat docs/README.md                    # Documentation index

# Main automation
python examples/hybrid_autonomous_assistant.py "test command"

# Setup
python setup/setup_credentials.py    # Credentials
python setup/setup_dev_assistant.py  # Assistant config

# Scripts
./scripts/setup-dev-env.sh           # Environment setup

# Structure
find . -name "*.py" | head -20       # List Python files
find docs -name "*.md" | sort        # List documentation
```

---

## 📊 **Benefits of This Organization**

### **🎯 For Autonomous Agents**
- **Clear navigation** with quick reference
- **Logical grouping** by function
- **Predictable locations** for different file types
- **Easy imports** with standard Python package structure

### **👥 For Human Developers**
- **Standard conventions** (README.md in root, etc.)
- **Separation of concerns** (docs vs code vs config)
- **Scalable structure** for future growth
- **Easy onboarding** with clear documentation paths

### **🔧 For Maintenance**
- **Consistent organization** across all file types
- **Clear ownership** of different folders
- **Easy to find** what you're looking for
- **Standard Python packaging** for imports

---

**📍 Current Location**: `/docs/development/PROJECT_STRUCTURE.md`
**🔗 Documentation Index**: [`../README.md`](../README.md)
**🏠 Project Root**: [`../../README.md`](../../README.md)
**📊 Last Updated**: December 2024

*This structure is designed to scale with the project while maintaining clarity for both humans and autonomous agents.* 🤖✨
