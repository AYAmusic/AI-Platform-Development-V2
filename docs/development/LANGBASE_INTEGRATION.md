# 🚀 Langbase Integration Guide: Hybrid AI Platform

## 🎯 **Overview: Best of Both Worlds**

This integration combines **Open WebUI's robust local capabilities** with **Langbase's efficient hosted primitives** to create a powerful hybrid AI platform that intelligently routes tasks based on privacy, cost, and performance requirements.

### **🔍 Smart Integration Philosophy**

Rather than replacing Open WebUI's excellent existing features, we **intelligently complement** them:

- **Privacy-First**: Sensitive documents stay local with Open WebUI's RAG
- **Cost-Optimized**: General knowledge leverages Langbase's 30-50x cheaper vector storage  
- **Performance-Balanced**: Dynamic routing based on real-time requirements
- **Feature-Rich**: Combine Open WebUI's rich document processing with Langbase's advanced primitives

---

## 🧠 **Open WebUI RAG Capabilities (Already Available)**

Before integrating Langbase, recognize Open WebUI's powerful existing features:

### **📚 Knowledge Collections**
- Multi-document knowledge bases with `#collection_name` syntax
- Advanced document processing (PDF, DOCX, Excel, PowerPoint, etc.)
- Token-based chunking with configurable overlap
- Multiple embedding model support (Ollama + OpenAI)

### **🔍 Advanced RAG Features**  
- **Hybrid Search Pipeline**: BM25 + CrossEncoder re-ranking
- **Web Integration**: `#URL` syntax for live content retrieval
- **YouTube RAG**: Video transcript processing and analysis
- **Google Drive**: Seamless cloud document integration
- **Citations**: Automatic source attribution and transparency
- **Relevance Scoring**: Configurable thresholds for precision

### **🎯 Model Integration**
- Knowledge-augmented models with persistent associations
- Custom RAG templates and prompts
- Advanced parameter control (context length, temperature, etc.)

---

## 🔗 **Langbase Integration Strategy**

### **When to Use Open WebUI RAG:**
✅ **Privacy-sensitive documents** (contracts, personal data, proprietary info)  
✅ **Rich document types** requiring advanced parsing (presentations, spreadsheets)  
✅ **Google Drive workflows** for team collaboration  
✅ **YouTube content analysis** for video-based knowledge  
✅ **Complex document structures** benefiting from local processing  
✅ **Real-time web content** integration via `#URL` syntax  

### **When to Use Langbase Memory:**
🚀 **General knowledge** where 30-50x cost savings matter  
🚀 **Large-scale vector storage** requiring hosted reliability  
🚀 **Cross-platform memory sharing** between different systems  
🚀 **Integration with Langbase Pipes** for workflow synergies  
🚀 **Scaling beyond local resources** for high-volume operations  

### **When to Use Hybrid Approach:**
🎯 **Mixed content types** (some private, some general)  
🎯 **Cost optimization** requiring smart routing decisions  
🎯 **Performance balancing** based on current system load  
🎯 **Comprehensive coverage** combining local richness with hosted efficiency  

---

## 🛠️ **Technical Implementation**

### **1. Environment Setup**

```bash
# Install Langbase SDK
npm install @langbase/sdk

# Configure environment variables
echo "LANGBASE_API_KEY=your_api_key_here" >> .env

# Test integration
npm run dev
```

### **2. Hybrid RAG Router Implementation**

```typescript
// src/integrations/hybrid-rag-router.ts
import createLangbaseClient from '../config/langbase.js';
import { OpenWebUIClient } from '../integrations/openwebui-client.js';

class HybridRAGRouter {
  private langbase;
  private openWebUI;

  constructor() {
    this.langbase = createLangbaseClient();
    this.openWebUI = new OpenWebUIClient();
  }

  async routeQuery(query: string, context: QueryContext) {
    // Analyze query to determine optimal routing
    const routingDecision = await this.analyzeQuery(query, context);
    
    switch (routingDecision.strategy) {
      case 'local-only':
        return await this.queryOpenWebUI(query, context);
      
      case 'hosted-only':
        return await this.queryLangbase(query, context);
      
      case 'hybrid':
        return await this.hybridQuery(query, context);
      
      default:
        return await this.fallbackQuery(query, context);
    }
  }

  private async analyzeQuery(query: string, context: QueryContext) {
    const analysis = {
      privacyLevel: this.assessPrivacyRequirements(context),
      costSensitivity: this.assessCostRequirements(context),
      performanceNeeds: this.assessPerformanceRequirements(context),
      contentType: this.assessContentType(context)
    };

    // Smart routing logic
    if (analysis.privacyLevel === 'high') {
      return { strategy: 'local-only', reasoning: 'Privacy-sensitive content' };
    }
    
    if (analysis.costSensitivity === 'high' && analysis.privacyLevel === 'low') {
      return { strategy: 'hosted-only', reasoning: 'Cost optimization priority' };
    }
    
    return { strategy: 'hybrid', reasoning: 'Balanced approach for optimal results' };
  }

  private async hybridQuery(query: string, context: QueryContext) {
    // Execute both queries in parallel
    const [localResults, hostedResults] = await Promise.all([
      this.queryOpenWebUI(query, context).catch(e => ({ error: e, results: [] })),
      this.queryLangbase(query, context).catch(e => ({ error: e, results: [] }))
    ]);

    // Intelligent result fusion
    return this.fuseResults(localResults, hostedResults, query);
  }

  private async fuseResults(localResults: any, hostedResults: any, query: string) {
    // Combine and rank results based on relevance and source quality
    const combinedResults = [
      ...localResults.results?.map(r => ({ ...r, source: 'local', priority: this.calculateLocalPriority(r) })) || [],
      ...hostedResults.results?.map(r => ({ ...r, source: 'hosted', priority: this.calculateHostedPriority(r) })) || []
    ];

    // Sort by relevance and priority
    const rankedResults = combinedResults
      .sort((a, b) => (b.priority + b.relevance) - (a.priority + a.relevance))
      .slice(0, 10); // Top 10 results

    return {
      results: rankedResults,
      sources: {
        local: localResults.sources || [],
        hosted: hostedResults.sources || []
      },
      strategy: 'hybrid',
      performance: {
        localLatency: localResults.latency,
        hostedLatency: hostedResults.latency,
        totalResults: combinedResults.length
      }
    };
  }
}
```

### **3. Enhanced Content Generation Pipeline**

```typescript
// src/workflows/enhanced-content-generation.ts
export class EnhancedContentGenerationPipeline {
  private ragRouter: HybridRAGRouter;
  private langbaseAgent: any;

  async generateContent(prompt: string, requirements: ContentRequirements) {
    // Step 1: Intelligent research using hybrid RAG
    const researchContext = await this.ragRouter.routeQuery(
      `Research context for: ${prompt}`,
      {
        privacyLevel: requirements.privacyLevel,
        contentType: requirements.contentType,
        sources: requirements.preferredSources
      }
    );

    // Step 2: Use Langbase agent for content generation with retrieved context
    const content = await this.langbaseAgent.run({
      prompt: this.buildEnhancedPrompt(prompt, researchContext),
      model: requirements.model || 'openai:gpt-4o',
      temperature: requirements.creativity || 0.7
    });

    // Step 3: Quality validation using local models
    const validation = await this.validateContent(content, requirements);

    return {
      content: content.completion,
      research: researchContext,
      validation: validation,
      sources: this.consolidateSources(researchContext),
      metadata: {
        strategy: researchContext.strategy,
        generationTime: Date.now(),
        costOptimized: researchContext.strategy.includes('hosted')
      }
    };
  }
}
```

---

## 🎯 **Integration Patterns**

### **1. Document Processing Workflow**
```
User Upload → Content Analysis → Smart Routing Decision
├── Privacy-Sensitive → Open WebUI Knowledge Collection
├── General Knowledge → Langbase Memory (30-50x cheaper)
└── Mixed Content → Hybrid processing with intelligent splitting
```

### **2. Query Processing Workflow**  
```
User Query → Context Analysis → Route Decision
├── Local RAG → Open WebUI (citations, hybrid search)
├── Hosted RAG → Langbase Memory (cost-efficient)
└── Hybrid → Parallel execution + result fusion
```

### **3. Content Generation Workflow**
```
Content Request → Research Phase → Generation Phase → Validation
├── Research → Hybrid RAG for comprehensive context
├── Generation → Langbase Pipes for efficient processing  
└── Validation → Local models for quality assurance
```

---

## 📊 **Performance & Cost Optimization**

### **Cost Comparison:**
- **Open WebUI RAG**: Local processing, no per-query costs, hardware dependent
- **Langbase Memory**: 30-50x cheaper vector storage, pay-per-use pricing
- **Hybrid Approach**: Optimal cost based on content type and requirements

### **Performance Optimization:**
- **Caching Strategy**: Cache frequently accessed results locally
- **Load Balancing**: Route based on current system capacity
- **Fallback Logic**: Graceful degradation when one system is unavailable

### **Smart Defaults:**
```typescript
const routingConfig = {
  defaultPrivacyLevel: 'medium', // Hybrid approach by default
  costThreshold: 0.10, // Switch to Langbase above this cost per query
  performanceTarget: 2000, // Target response time in ms
  qualityMinimum: 0.8 // Minimum relevance score for results
};
```

---

## 🚀 **Getting Started**

### **Step 1: Verify Open WebUI RAG Setup**
1. Create a Knowledge Collection in Open WebUI
2. Upload test documents and verify `#collection_name` access
3. Test advanced features (web RAG, YouTube RAG, citations)

### **Step 2: Setup Langbase Integration**
1. Run existing Langbase demos: `npm run agent:prompt-chain`
2. Test Memory integration: `npm run agent:memory`
3. Verify API connectivity and basic functionality

### **Step 3: Implement Hybrid Router**
1. Deploy the HybridRAGRouter class
2. Configure routing rules based on your use cases
3. Test with sample queries across different privacy levels

### **Step 4: Enhanced Workflows**
1. Implement the Enhanced Content Generation Pipeline
2. Create custom workflows for your specific needs
3. Monitor performance and optimize routing decisions

---

## 📋 **Decision Framework**

Use this framework to decide on integration approach:

| Factor | Open WebUI | Langbase | Hybrid |
|--------|------------|----------|--------|
| **Privacy** | High | Low-Medium | Configurable |
| **Cost** | Hardware | 30-50x cheaper vectors | Optimized |
| **Features** | Rich local features | Advanced primitives | Best of both |
| **Scale** | Hardware limited | Cloud scale | Dynamic scaling |
| **Latency** | Local processing | Network dependent | Balanced |
| **Control** | Full local control | Hosted service | Smart routing |

---

## 🎉 **Ready to Build!**

Your enhanced hybrid AI platform now intelligently combines:
- **Open WebUI's privacy-first, feature-rich local processing**
- **Langbase's cost-efficient, scalable hosted primitives**  
- **Smart routing** that optimizes for privacy, cost, and performance
- **Comprehensive workflows** that leverage the best of both platforms

The background agents are ready to optimize these workflows while you focus on building amazing AI applications! 🚀 