# News MCP Server PyPI Examples

Python package integration examples for the News MCP Server.

## 📁 Examples

### 🚀 Basic Usage
- `basic_client.py` - Simple MCP client implementation
- `async_client.py` - Async/await patterns
- `batch_requests.py` - Efficient batch processing

### 🤖 AI Framework Integrations
- `langchain_agent.py` - LangChain agent with news capabilities
- `crewai_workflow.py` - CrewAI multi-agent news analysis
- `openai_integration.py` - Direct OpenAI API integration

### 🏢 Enterprise Use Cases
- `brand_monitor.py` - Automated brand monitoring
- `market_intelligence.py` - Investment research automation
- `compliance_tracker.py` - Regulatory news monitoring

### 📊 Data Processing
- `news_analytics.py` - Sentiment analysis and trending
- `entity_extraction.py` - Named entity recognition
- `export_formats.py` - CSV, JSON, Excel export

### 🔧 Utilities
- `config_manager.py` - Configuration management
- `error_handling.py` - Robust error handling patterns
- `caching_strategies.py` - Redis and memory caching

## 🔧 Setup

```bash
# Install the package
pip install news-mcp-server[full]

# Copy environment template
cp .env.example .env

# Edit with your credentials
nano .env

# Run examples
python basic_client.py
```