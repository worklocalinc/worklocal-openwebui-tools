# WorkLocal OpenWebUI Tools

Official OpenWebUI integration tools for WorkLocal infrastructure management platform.

🌐 **Live API**: https://worklocal.app

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/worklocalinc/worklocal-openwebui-tools.git

# Install in OpenWebUI
cp src/worklocal_tools.py /path/to/openwebui/tools/
```

## 📋 Features

- ✅ Health monitoring
- 📊 Resource management (create, read, update, delete)
- ⚡ Action execution (start, stop, restart)
- 📈 Metrics and monitoring
- 🔍 Advanced search capabilities

## 🛠️ Available Tools

| Tool | Description |
|------|-------------|
| `worklocal_health_check` | Check API connectivity |
| `worklocal_list_resources` | List all infrastructure resources |
| `worklocal_get_resource` | Get resource details |
| `worklocal_create_resource` | Create new resources |
| `worklocal_update_resource` | Update existing resources |
| `worklocal_delete_resource` | Delete resources |
| `worklocal_execute_action` | Execute actions on resources |
| `worklocal_get_metrics` | Retrieve resource metrics |
| `worklocal_search_resources` | Search with filters |

## 📖 Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Usage Examples](docs/USAGE.md)
- [API Reference](docs/API_REFERENCE.md)
- [Contributing](docs/CONTRIBUTING.md)

## 🔧 Configuration

```python
# Basic configuration
self.base_url = "https://worklocal.app"

# With authentication
self.headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md).

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📧 Email: support@worklocal.app
- 💬 Discord: [Join our community](https://discord.gg/worklocal)
- 📚 Docs: https://worklocal.app/docs
