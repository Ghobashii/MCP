# MCP Servers as Attack Vectors: Security Research Project

## ⚠️ **IMPORTANT: EDUCATIONAL RESEARCH ONLY**

This project is **strictly for educational and security research purposes**. It demonstrates how Model Context Protocol (MCP) servers can potentially be weaponized as attack vectors. This research is conducted to:

- Advance understanding of MCP security implications
- Develop detection and defense strategies
- Contribute to the security community's knowledge

**DO NOT use this code for malicious purposes or against systems you don't own.**

## 📋 Project Overview

This repository contains a proof-of-concept (PoC) malicious MCP server called "DevTools Assistant" designed for a technical blog post on Securelist. The project demonstrates how MCP servers can be weaponized through:

- **Legitimate Facade**: Three convincing developer productivity tools
- **Stealth Operations**: Hidden data collection and exfiltration capabilities
- **Supply Chain Attack Vector**: Exploiting developer trust in productivity tools

### Research Objectives

1. **Demonstrate Attack Vector**: Show how MCP servers can be weaponized
2. **Test Detection Methods**: Identify behavioral and network indicators
3. **Develop Defenses**: Create actionable security recommendations
4. **Contribute to Security**: Advance MCP security understanding

## 🏗️ Project Structure

```
MCP/
├── src/
│   ├── mcp_http_server.py          # Main MCP HTTP server
│   └── tools/                      # MCP tool implementations
│       ├── analyze_project_structure.py
│       ├── check_config_health.py
│       └── optimize_dev_environment.py
├── test-project/                   # Test environment with sensitive files
│   ├── .env                        # Fake environment variables
│   ├── .ssh/                       # Simulated SSH keys
│   ├── certs/                      # Test certificates
│   └── config/                     # Configuration files
├── .cursor/                        # Cursor IDE configuration
├── cursor-mcp-config.json          # MCP server configuration
├── requirements.txt                # Python dependencies
├── mcp_blog_final_plan.md          # Detailed research plan
├── status.md                       # Project progress tracking
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Cursor IDE (or VS Code with MCP extension)
- Windows 10/11 (for testing environment)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MCP
   ```

2. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Start the MCP server**
   ```bash
   python src/mcp_http_server.py
   ```

4. **Configure Cursor IDE**
   - Copy `cursor-mcp-config.json` to your Cursor configuration
   - Restart Cursor
   - Verify tools appear in the MCP tools list

## 🛠️ Current Implementation Status

### ✅ Completed (Week 1, Day 1-2)

- **Legitimate MCP Server**: Fully functional HTTP server with JSON-RPC 2.0 support
- **Three Developer Tools**:
  - `analyze_project_structure`: Analyzes project directory organization
  - `check_config_health`: Scans configuration files for issues
  - `optimize_dev_environment`: Provides development environment suggestions
- **Cursor Integration**: Successfully tested and working
- **Test Environment**: Realistic project structure with sensitive files

### 🔄 In Progress (Week 1, Day 3-4)

- **Steganographic Hiding**: ANSI escape sequences in tool descriptions
- **Data Collection**: Systematic discovery of sensitive files
- **Stealth Operations**: Hidden functionality within legitimate tools

### 📋 Planned (Week 1, Day 5-7)

- **Exfiltration Mechanisms**: API call disguising and DNS tunneling
- **Isolated Testing**: Comprehensive testing in controlled environment
- **Network Analysis**: Traffic capture and analysis

## 🧪 Testing the Current Implementation

### 1. Start the Server
```bash
python src/mcp_http_server.py
```

### 2. Configure Cursor
Add this to your Cursor configuration:
```json
{
  "mcpServers": {
    "devtools-assistant": {
      "command": "python",
      "args": ["src/mcp_http_server.py"],
      "env": {}
    }
  }
}
```

### 3. Test the Tools
In Cursor, you can now use:
- `/analyze project structure` - Triggers project analysis
- `/check config health` - Scans configuration files
- `/optimize dev environment` - Provides optimization suggestions

### 4. Verify Integration
- Tools should appear in Cursor's MCP tools list
- All three tools should be functional and professional
- No obvious malicious indicators should be present

## 🔍 Research Methodology

### Testing Environment
- **Isolated VM**: Windows 11 with no external network access
- **Development Tools**: Cursor IDE with MCP integration
- **Monitoring**: Wireshark, Process Monitor, PowerShell logging
- **Mock Services**: Local endpoints for exfiltration testing

### Data Collection Targets
- Environment files (`.env`, `.env.local`, `.env.production`)
- SSH keys (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`)
- Cloud configuration files (`~/.aws/credentials`, `~/.gcp/credentials.json`)
- API tokens and certificates (`.pem`, `.key`, `.crt` files)
- Database connection strings and configuration files
- Windows-specific targets (`%APPDATA%` credential stores)

## 🛡️ Ethical Guidelines

### Code Safety
- All malicious functionality clearly marked as educational
- Built-in safeguards prevent actual system damage
- Exfiltration endpoints controlled and documented
- Easy reversal and cleanup mechanisms

### Responsible Disclosure
- Coordinate with Anthropic security team on any discovered vulnerabilities
- Share defensive guidance alongside offensive research
- Engage with MCP security community for collaborative improvement

### Publication Standards
- Clear ethical use disclaimers throughout
- Educational focus with practical security value
- Actionable defensive recommendations
- Responsible vulnerability disclosure coordination

## 📊 Expected Deliverables

### Primary Deliverable
- **Complete Blog Post**: 4,000-4,500 words for Securelist
- **Visual Assets**: 6-8 professional diagrams and charts
- **Testing Documentation**: Screenshots, logs, and network captures

### Supporting Deliverables
- **PoC Source Code**: Clean, well-documented educational implementation
- **Testing Scripts**: Automated setup and validation tools
- **Detection Signatures**: Network and behavioral indicators for security teams

## 🔧 Development Commands

### Running the Server
```bash
# Development mode with debug logging
python src/mcp_http_server.py --debug

# Production mode
python src/mcp_http_server.py
```

### Testing Tools
```bash
# Test individual tools
python -c "from src.tools.analyze_project_structure import analyze_project_structure; print(analyze_project_structure())"
```

### Code Quality
```bash
# Format code
black src/

# Lint code
flake8 src/

# Type checking
mypy src/
```

## 📚 Documentation

- **`mcp_blog_final_plan.md`**: Detailed research plan and timeline
- **`status.md`**: Current project progress and next steps
- **`src/`**: Source code with inline documentation
- **`test-project/`**: Test environment documentation

## 🤝 Contributing

This is a research project with specific objectives. If you're interested in contributing:

1. **Review the research plan** in `mcp_blog_final_plan.md`
2. **Check current status** in `status.md`
3. **Follow ethical guidelines** outlined above
4. **Focus on educational value** and security advancement

## 📄 License

This project is for educational and security research purposes only. All code is provided as-is without warranty. Users are responsible for ensuring compliance with applicable laws and ethical guidelines.

## ⚖️ Legal Disclaimer

This software is provided for educational and security research purposes only. The authors are not responsible for any misuse of this software. Users must ensure they have proper authorization before testing on any systems they do not own.

---

**For questions or concerns about this research, please contact the project maintainers.** 