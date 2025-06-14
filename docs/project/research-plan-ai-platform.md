# Research Plan: Architecting a Tailored Local AI Platform with Advanced Capabilities

**Date Created:** Thursday, June 5, 2025
**Last Updated:** Thursday, June 5, 2025
**Status:** Phase 1 - Planning & Research

## Table of Contents

1. [Project Vision & Purpose](#project-vision--purpose)
2. [Phase 1: Foundational Analysis & Architectural Blueprint](#phase-1-foundational-analysis--architectural-blueprint)
3. [Phase 2: UI/UX Design and Frontend Strategy](#phase-2-uiux-design-and-frontend-strategy)
4. [Phase 3: Custom Advanced AI Capabilities](#phase-3-researching-and-planning-custom-advanced-ai-capabilities)
5. [Phase 4: Development, Integration, and Testing Strategy](#phase-4-development-integration-and-testing-strategy)
6. [Technology Stack & Decisions](#technology-stack--decisions)
7. [Key Deliverables](#key-deliverables)
8. [Risk Assessment](#risk-assessment)
9. [Current Research Findings](#current-research-findings)
10. [Next Steps](#next-steps)

---

## Project Vision & Purpose

### Core Objective
Transform the Open WebUI platform into a bespoke, locally hosted AI application with custom-developed advanced AI capabilities, drawing inspiration from Langbase's "AI primitives" and agent architectures.

### Design Philosophy
- **"Primitives over Frameworks"** - Build with flexible, composable blocks rather than rigid frameworks
- **Local-First** - Operate entirely offline with user privacy and control
- **Modular Architecture** - Composable, interoperable services
- **Developer-Friendly** - API-first, zero-config where possible

### Target User Experience
Create a user interface achieving excellence comparable to leading commercial AI platforms (Gemini, Claude, ChatGPT) while maintaining full local control.

### Development Environment
- **Primary IDE:** Cursor with multiple LLM assistance like Claude 4 Gemini 2.5 etc.
- **Testing:** Playwright for UI automation & MCP integration
- **Version Control:** GitHub with Bug Bot integration
- **Architecture:** SvelteKit frontend + FastAPI backend (existing Open WebUI structure)

---

## Phase 1: Foundational Analysis & Architectural Blueprint
*Weeks 1-4*

### 1.1 Deconstructing Open WebUI: Understanding the Existing Canvas

#### Current Architecture Assessment (Based on Recent Research)

**Backend (Python/FastAPI):**
- **Entry Point:** `main.py` - sets up middleware and mounts API routers
- **Routers:** `routers/` directory handles specific functionalities (ollama.py, chats.py, users.py)
- **Data Models:** SQLAlchemy models in `models/` directory
- **Utilities:** Core logic in `utils/` for auth, chat processing, RAG, etc.
- **Database:** Local SQLite (webui.db) for user configs, chat histories, RAG data
- **WebSockets:** Real-time communication via `socket/` directory

**Frontend (Svelte/SvelteKit):**
- **Structure:** `src/routes/` for pages, `src/lib/` for reusable components
- **API Communication:** Direct fetch API calls to FastAPI backend
- **State Management:** Svelte stores for application state
- **Current UI:** Tailwind CSS styling

#### Key Extension Points Identified
1. **Function/Tool Integration:** Native Python Function Calling Tool + Pipelines Framework
2. **RAG System:** Built-in document processing and retrieval
3. **Model Management:** Support for Ollama + OpenAI-compatible APIs
4. **Authentication:** JWT, OAuth, LDAP support with RBAC

### 1.2 Langbase Concepts Translation

#### AI Primitives Mapping

| Langbase Primitive | Custom Platform Component | Core Functionality | Design Considerations |
|-------------------|---------------------------|-------------------|---------------------|
| **Pipe (Agent)** | Custom Agent Core | Manages LLM interactions, state, orchestrates calls to tools and memory | API for invocation, state persistence, integration with tool executor and memory service |
| **Memory (RAG)** | Knowledge Base Service | Handles data ingestion, vectorization, storage, and retrieval | Choice of local vector DB (ChromaDB, FAISS), chunking strategy, embedding model selection |
| **Tools (Function Calling)** | Tool Execution Engine | Securely defines, registers, and executes custom Python tools callable by LLM | Secure execution environment, schema definition, integration with Playwright MCP |
| **Threads** | Conversation State Manager | Persists and retrieves conversation history and context | Database schema for messages, efficient retrieval, user session management |
| **Workflows** | Dynamic Task Orchestrator | Implements complex multi-step AI workflows | LLM-based task decomposition, sub-task management, parallel execution capabilities |

#### Agent Architectures to Implement
1. **Augmented LLM** - Basic enhanced LLM with tools and memory
2. **Prompt Chaining** - Sequential workflow execution
3. **Agentic Routing** - Task routing to specialized agents
4. **Agent Parallelization** - Concurrent task execution
5. **Orchestration-Workers** - Dynamic task decomposition
6. **Evaluator-Optimizer** - Iterative refinement loops

### 1.3 Target Platform Architecture

#### Modular Backend Services
- **KnowledgeBaseService** - RAG functionalities
- **WorkflowEngine** - Agentic task orchestration
- **ToolExecutionService** - LLM function calls
- **AnalyticsService** - Usage and performance tracking
- **AgentCore** - LLM interaction management

#### Communication Strategy
- **WebSockets** - Real-time LLM responses and progress updates
- **REST APIs** - Standard request-response interactions
- **Local-First Data** - All user data stored locally (SQLite + local vector store)

---

## Phase 2: UI/UX Design and Frontend Strategy
*Weeks 3-6*

### 2.1 UI/UX Design Principles

#### Core UX Principles
- Problem-solving over personality
- Simplify first interactions
- Clear feedback loops
- Context-appropriate UI
- Always provide exit options
- Design for interruptions

#### Visual Design Language
- **Typography:** Clean, readable sans-serif with consistent hierarchy
- **Color Palette:** Minimalist with robust dark mode support
- **Iconography:** Clear, simple, universally understood icons
- **Layout:** Balanced with ample white space, logical grouping
- **Micro-interactions:** Subtle animations for feedback and engagement

### 2.2 Feature UI Design Requirements

#### Model Selection & Parameter Controls
- Retain sliders with numerical inputs
- Add tooltips explaining parameter effects
- Implement presets for different use cases (Factual, Creative, Code Generation)

#### Knowledge Base (RAG) Interaction
- Document upload with drag-and-drop and progress indicators
- Dedicated "Knowledge Base" management section
- Visual dropdown for document/collection selection
- Clear indicators when RAG is active

#### Workflow Builder Interface
- **Node-based editor** with canvas and draggable nodes
- Palette of nodes (LLM calls, tool executions, RAG queries, conditional logic)
- Contextual configuration panel for selected nodes
- Visual data flow representation

#### Model Output Comparison
- Side-by-side view for different models/parameters
- Clear labeling with model and parameter information
- Options to rate responses and select preferred output
- Diff visualization for detailed comparisons

#### Analytics Dashboard
- Combination of charts (line, bar, pie) for different metrics
- KPI cards for key figures
- Customizable views with drill-down capabilities
- Clear, actionable visualizations

### 2.3 Frontend Technology Decision

#### Frontend Framework Analysis

| Framework | Ecosystem Size | Performance | Learning Curve | Component Availability | Customization Ease | Suitability for Open WebUI | Suitability for Sleek UI |
|-----------|----------------|-------------|----------------|----------------------|------------------|---------------------------|------------------------|
| **Svelte/SvelteKit (Current)** | Growing | Excellent | Low | Moderate | High | High (direct modification) | Good |
| **React/Next.js** | Very Large | Excellent | Moderate | High | Very High | Moderate (integration/rewrite) | Excellent |

#### Decision Factors
- **Svelte Advantages:** Current codebase, excellent performance, direct modification path
- **React Advantages:** Vast ecosystem (Shadcn UI, assistant-ui), better component availability
- **Recommendation:** Evaluate scope of UI changes to determine modification vs. rewrite approach

---

## Phase 3: Researching and Planning Custom Advanced AI Capabilities
*Weeks 5-10*

### 3.1 Custom Tooling and Function Calling Implementation

#### Current Open WebUI Capabilities
- Native Python Function Calling Tool
- Pipelines Plugin Framework
- Tools class with callable methods
- UI-based function addition (need to move to file-based for developer workflow)

#### Playwright MCP Integration
**Model Context Protocol Setup:**
- Playwright configured as MCP server for browser automation
- Integration with Cursor IDE enabling Claude 4 to interact with browsers
- Capabilities: navigation, form filling, testing, UI interaction

**Benefits:**
- AI can "see" and interact with its own UI
- Advanced agentic behaviors beyond typical LLM tool use
- Seamless browser automation for testing and interaction

### 3.2 Custom RAG System Design

#### RAG Pipeline Components

| Component | Implementation Choice | Rationale |
|-----------|---------------------|-----------|
| **Document Loaders** | LangChain/LlamaIndex modular components | Extensive file type support (PDF, TXT, MD, DOCX) |
| **Text Splitters** | Custom chunking strategies | Langbase chunking parameter insights + RAG best practices |
| **Embedding Models** | Local open-source models | Privacy-first, no external dependencies |
| **Vector Stores** | ChromaDB or FAISS | Lightweight, local deployment suitable |
| **Retrievers** | Custom algorithms | Efficient chunk retrieval based on query embedding |

#### Integration Requirements
- **Knowledge Base Management UI:** Document upload, management, in-chat selection
- **Clear RAG Indicators:** Visual feedback when RAG is augmenting responses
- **Modular Design:** Use specific library components without adopting entire frameworks

### 3.3 Multimodal Feature Integration

#### Local Multimodal Models (Research Findings)
- **LLaVA Models:** Available through Ollama (7B, 13B, 34B variants)
  - Higher image resolution support (4x more pixels)
  - Improved text recognition and reasoning
  - Apache 2.0 license
- **Gemma 3:** Vision capabilities with local inference
- **Qwen 2.5 VL:** Strong vision-language model

#### Implementation Strategy
- **Primary:** Ollama for robust local serving of vision models
- **Secondary:** WebLLM for potential client-side offloading
- **UI Components:** Image upload, multimodal content display, audio playback controls

### 3.4 Agentic Systems Architecture

#### Workflow Implementation Patterns
1. **Sequential Workflows** (Prompt Chaining)
2. **Conditional Routing** (Agentic Routing)
3. **Parallel Execution** (Agent Parallelization)
4. **Dynamic Orchestration** (Orchestration-Workers)
5. **Iterative Refinement** (Evaluator-Optimizer)

#### Memory Management
- **Conversation State:** Persistent thread management
- **Agent Memory:** Cross-workflow knowledge retention
- **Tool Results:** Caching and reuse of tool outputs

---

## Phase 4: Development, Integration, and Testing Strategy
*Weeks 11-12+*

### 4.1 Development Workflow

#### AI-Assisted Development with Cursor + Claude 4
- Effective prompting strategies for code generation and refactoring
- Both Python backend and Svelte/JavaScript/TypeScript frontend development
- Integration with Playwright MCP for UI interaction and testing

#### Playwright Integration Strategy
- **UI Automation:** Testing of modified Open WebUI frontend
- **MCP Tool Integration:** Claude 4 can interact with web UI through Playwright MCP
- **Development Enhancement:** AI-generated Playwright scripts and debugging

#### Version Control & Code Review
- **Branching Strategy:** Feature branches → develop → main
- **PR Process:** Human + AI-assisted reviews (Cursor Bug Bot)
- **Automated Checks:** Testing and validation pipelines

### 4.2 Phased Implementation Roadmap

#### Phase 1: Core Chat UI & Local Model Integration
- Basic Svelte chat UI components
- Ollama integration for local model serving
- Model selection and parameter controls
- WebSocket communication for streaming

#### Phase 2: Foundational Advanced Features
- RAG/Knowledge Base feature (document upload, basic retrieval)
- Model Comparison UI (side-by-side output view)

#### Phase 3: Advanced AI Capabilities & Workflows
- Custom Tool Execution Engine with Python tools
- Workflow builder UI (node-based editor)
- Multimodal capabilities (image processing with LLaVA)

#### Phase 4: Polish, Analytics, and Advanced Agents
- Enhanced UI/UX with micro-interactions
- Analytics dashboard
- Complex agentic workflows and "Manus-like" autonomy

---

## Technology Stack & Decisions

### Current Confirmed Technologies

#### Backend (Leverage Existing + Integrate)
- **Base Platform:** Open WebUI (FastAPI + Svelte) - Keep existing architecture
- **Database:** SQLite (existing) with Open WebUI's proven data models
- **RAG System:** Open WebUI's built-in advanced RAG (already production-ready)
- **LLM Integration:** Ollama (existing) + Langbase SDK integration
- **Agent Orchestration:** Langbase SDK (Pipes, Workflows, Tools)
- **Tools:** Hybrid approach - Open WebUI's pipelines + Langbase's pre-built tools

#### Frontend Enhancement Strategy
- **Base Framework:** SvelteKit (existing) - direct modification path
- **UI Enhancement:** Incremental improvements vs full rewrite
- **Component Library:** Research Svelte ecosystem vs selective React integration
- **Specialized Components:** Node-based workflow editor (evaluate React Flow vs Svelte alternatives)
- **State Management:** Enhance existing Svelte stores

#### Development Tools
- **IDE:** Cursor with multiple LLM assistance (Claude 4, Gemini 2.5)
- **Testing:** Playwright + MCP integration for browser automation
- **Version Control:** GitHub + Bug Bot
- **AI Integration:** Model Context Protocol for tool interactions
- **Rapid Prototyping:** Chai.new for agent development

#### AI Services Integration
- **Local Models:** Ollama (LLaVA, Gemma 3, Qwen 2.5 VL)
- **Agent Platform:** Langbase SDK for AI primitives
- **RAG Strategy:** Hybrid - Local (Open WebUI) + Hosted (Langbase Memory API)
- **Tools:** Web search, crawling via Langbase + custom Python tools
- **Rapid Development:** Chai.new for prompt-to-agent prototyping

---

## Current Research Findings

### Open WebUI Existing Capabilities (Major Discovery!)

**Advanced RAG System Already Built:**
- **Knowledge Collections** - Multi-document knowledge bases with `#collection_name` access
- **Document Upload** - Direct file upload to chats with automatic processing
- **Web RAG** - `#URL` integration for live web content retrieval
- **YouTube RAG** - Video transcript processing and analysis
- **Google Drive Integration** - Direct access to cloud documents
- **Hybrid Search Pipeline** - BM25 + CrossEncoder re-ranking for precision
- **Citations** - Automatic source attribution and transparency
- **Advanced Chunking** - Token-based chunking with configurable overlap
- **Multiple Embedding Models** - Ollama and OpenAI model support
- **Custom RAG Templates** - Configurable prompt engineering

**Function Calling & Tools:**
- Native Python Function Calling Tool
- Pipelines Plugin Framework
- OpenAPI Tool Servers
- UI-based and file-based tool registration

**Proven Architecture:**
- Well-structured modular FastAPI backend
- Local-first data management with SQLite
- WebSocket support for real-time interactions
- Active community with 97.7k+ GitHub stars
- Production-ready document parsing for multiple formats

### Langbase SDK Integration Opportunity

**Available AI Primitives via [Langbase SDK](https://langbase.com/docs/sdk):**
- **Pipe (Agents)** - Serverless AI agents with tools and memory
- **Memory (RAG)** - Hosted RAG with 30-50x cost efficiency
- **Tools** - Pre-built web search, crawling, and custom tools
- **Threads** - Conversation state management without DBs
- **Workflows** - Multi-step agents with durability features
- **Parser/Chunker/Embed** - Document processing primitives
- **Agent Runtime** - Unified API over 600+ LLMs

**Chai.new Integration:**
- [Chai.new](https://chai.new) - "Vibe code any AI agent" platform
- Turns prompts into production-ready agents
- Can be used for rapid prototyping of AI primitives
- Testimonials show strong developer adoption

### Revised Integration Strategy

**Leverage Existing Solutions:**
1. **Use Open WebUI's RAG** - Advanced system already built and tested
2. **Integrate Langbase SDK** - For agent orchestration and workflows
3. **Extend with Chai.new** - For rapid agent prototyping
4. **Focus on UI/UX** - Enhance existing capabilities with better interfaces
5. **Add Playwright MCP** - For browser automation and testing

### MCP + Playwright Capabilities
**Current State (2025):**
- MCP enables LLMs to control browser automation through structured commands
- Uses accessibility tree for fast, reliable interactions (vs. screenshot-based)
- Integration with Cursor, VS Code, Claude Desktop
- Active community development with 3.8k+ stars on playwright-mcp

### Multimodal AI Capabilities
**Local Options Available:**
- LLaVA 1.6+ models with improved resolution and text recognition
- Ollama support for vision models (7B, 13B, 34B variants)
- Gemma 3 and Qwen 2.5 VL for different use cases
- Apache 2.0 licensing for most models

---

## Risk Assessment

### Technical Risks
1. **Complexity of Custom AI Primitives** - Mitigation: Modular architecture, comprehensive testing
2. **Performance of Local Models** - Mitigation: Model optimization, WebLLM offloading, clear UI feedback
3. **UI/UX Parity Challenge** - Mitigation: Dedicated design time, user testing, leveraging Shadcn UI
4. **Integration Complexity** - Mitigation: Thorough documentation, standardized patterns

### Strategic Risks
1. **Scope Creep** - Mitigation: Strict adherence to phased implementation
2. **Technology Bet Risks** - Mitigation: Modular design allowing component swapping
3. **Community/Ecosystem Maturity** - Mitigation: Leverage established tools where possible

---

## Key Deliverables

### Phase 1 Deliverables
- [ ] Open WebUI architectural assessment document
- [ ] Langbase concepts to custom components mapping
- [ ] System architecture diagram with component specifications
- [ ] Frontend framework decision with justification

### Phase 2 Deliverables
- [ ] UI/UX style guide and design principles
- [ ] Wireframes and mockups for all new features
- [ ] Frontend technology stack and component strategy

### Phase 3 Deliverables
- [ ] Custom tool/function calling architecture specification
- [ ] Agentic systems architectural designs
- [ ] Multimodal integration strategy
- [ ] Custom RAG system detailed design
- [ ] DGM-inspired iterative refinement strategy

### Phase 4 Deliverables
- [ ] Development workflow documentation
- [ ] Detailed phased implementation roadmap
- [ ] Updated risk register with mitigation plans

---

## Next Steps

### Updated Development Priority (Based on Research Findings)

#### **Week 1-2: Foundation Assessment & Integration Setup**
1. **Deep Dive into Open WebUI's Existing Capabilities**
   - Hands-on exploration of Open WebUI's RAG system (Knowledge Collections, document upload)
   - Test existing function calling and pipelines framework
   - Review `backend/open_webui/` architecture with focus on extension points
   - Document current tool registration and RAG configuration

2. **Set up Langbase SDK Integration Environment**
   - Install and configure Langbase SDK
   - Create test Langbase account and API keys
   - Build simple bridge between Open WebUI and Langbase primitives
   - Test basic Pipe (agent) creation and execution

3. **Prototype with Chai.new**
   - Create account on Chai.new platform
   - "Vibe code" a simple AI agent for testing
   - Understand Chai.new → production deployment workflow
   - Document integration possibilities with our platform

4. **Set up Enhanced Development Environment**
   - Configure Playwright MCP integration with Cursor
   - Validate AI-assisted development workflow
   - Set up GitHub repository with enhanced documentation structure

#### **Week 3-4: Integration Layer Development**
1. **Build Langbase SDK Bridge Service**
   - Create FastAPI router for Langbase integration
   - Design hybrid RAG routing logic (local vs hosted)
   - Implement agent orchestration endpoints
   - Test workflow primitive integration

2. **Enhanced UI Components Research & Prototyping**
   - Research Svelte ecosystem for node-based editors
   - Prototype workflow builder interface concepts
   - Design agent management UI mockups
   - Plan Open WebUI frontend enhancement strategy

3. **Tool Integration Strategy**
   - Combine Open WebUI's existing tools with Langbase's pre-built tools
   - Design unified tool management interface
   - Prototype custom tool development workflow

#### **Week 5-8: Advanced Features Implementation**
1. **Workflow Builder UI** (node-based editor for agent orchestration)
2. **Agent Management Interface** (creation, monitoring, deployment)
3. **Advanced Analytics Dashboard** (usage tracking, performance metrics)
4. **Hybrid RAG Management** (local + hosted knowledge sources)

#### **Week 9-12: Polish & Production**
1. **Performance Optimization** (local model efficiency, UI responsiveness)
2. **Advanced Agent Patterns** (evaluator-optimizer loops, complex workflows)
3. **Production Deployment Strategy** (containerization, scaling, monitoring)
4. **Documentation & Community** (user guides, developer docs, examples)

---

## Questions for Discussion

1. **Integration Strategy:** Should we integrate Langbase SDK directly into Open WebUI's backend, or create a bridge service that connects the two platforms?

2. **Langbase vs Local RAG:** When should we use Open WebUI's built-in RAG vs Langbase's hosted Memory service? What are the tradeoffs?

3. **Chai.new Workflow:** How can we best leverage Chai.new for rapid agent prototyping while maintaining local control?

4. **UI Enhancement Focus:** Given Open WebUI's robust backend capabilities, should we focus primarily on enhancing the UI/UX layer with modern components?

5. **Agent Orchestration:** Should we build workflow orchestration on top of Open WebUI's existing pipelines, or integrate Langbase's Workflow primitives?

6. **Development Philosophy:** Are we building a "better Open WebUI" or a "local Langbase alternative" - and how does this affect our architectural decisions?

7. **Tool Integration:** How can we combine Open WebUI's existing tool system with Langbase's pre-built tools (web search, crawling)?

---

*This document serves as our living blueprint for the AI platform development project. It will be updated regularly as we make progress and discoveries.*
