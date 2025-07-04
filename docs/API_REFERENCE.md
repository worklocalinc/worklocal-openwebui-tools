# API Reference

## Class: Tools

The main class that provides all WorkLocal API integration methods.

### Constructor

```python
Tools()
```

Initializes the Tools class with default configuration.

**Configuration attributes:**
- `base_url`: The base URL for the API (default: "https://worklocal.app")
- `headers`: HTTP headers including Content-Type and optional authentication

### Methods

#### worklocal_health_check()

Check if the WorkLocal Studio API is healthy and accessible.

**Returns:**
- `str`: Health status message with emoji indicators

**Example:**
```python
result = tools.worklocal_health_check()
# Returns: "✅ WorkLocal Studio API is healthy. Status: OK"
```

---

#### worklocal_list_resources(resource_type="all")

List infrastructure resources from WorkLocal Studio.

**Parameters:**
- `resource_type` (str, optional): Type of resources to list. Default: "all"
  - Options: "all", "servers", "containers", "databases"

**Returns:**
- `str`: Formatted list of resources with details

**Example:**
```python
resources = tools.worklocal_list_resources("servers")
```

---

#### worklocal_get_resource(resource_id)

Get detailed information about a specific resource.

**Parameters:**
- `resource_id` (str): The ID of the resource to retrieve

**Returns:**
- `str`: Formatted resource details including metadata

**Example:**
```python
details = tools.worklocal_get_resource("res-123")
```

---

#### worklocal_create_resource(name, resource_type, config="{}")

Create a new infrastructure resource.

**Parameters:**
- `name` (str): Name of the resource to create
- `resource_type` (str): Type of resource (e.g., "server", "container", "database")
- `config` (str, optional): JSON string containing additional configuration. Default: "{}"

**Returns:**
- `str`: Creation result message with resource ID

**Example:**
```python
result = tools.worklocal_create_resource(
    name="web-server-01",
    resource_type="server",
    config='{"cpu": 4, "memory": "8GB", "disk": "100GB"}'
)
```

---

#### worklocal_update_resource(resource_id, updates)

Update an existing infrastructure resource.

**Parameters:**
- `resource_id` (str): ID of the resource to update
- `updates` (str): JSON string containing the updates

**Returns:**
- `str`: Update result message

**Example:**
```python
result = tools.worklocal_update_resource(
    resource_id="res-123",
    updates='{"cpu": 8, "memory": "16GB"}'
)
```

---

#### worklocal_delete_resource(resource_id)

Delete an infrastructure resource.

**Parameters:**
- `resource_id` (str): ID of the resource to delete

**Returns:**
- `str`: Deletion result message

**Example:**
```python
result = tools.worklocal_delete_resource("res-123")
```

---

#### worklocal_execute_action(resource_id, action, parameters="{}")

Execute an action on a resource.

**Parameters:**
- `resource_id` (str): ID of the resource
- `action` (str): Action to execute (e.g., "start", "stop", "restart")
- `parameters` (str, optional): JSON string containing action parameters. Default: "{}"

**Returns:**
- `str`: Action execution result

**Example:**
```python
result = tools.worklocal_execute_action(
    resource_id="res-123",
    action="restart",
    parameters='{"graceful": true, "timeout": 30}'
)
```

---

#### worklocal_get_metrics(resource_id, metric_type="all", timeframe="1h")

Get metrics for a specific resource.

**Parameters:**
- `resource_id` (str): ID of the resource
- `metric_type` (str, optional): Type of metrics to retrieve. Default: "all"
  - Options: "cpu", "memory", "network", "disk", "all"
- `timeframe` (str, optional): Timeframe for metrics. Default: "1h"
  - Options: "1h", "6h", "12h", "24h", "7d", "30d"

**Returns:**
- `str`: Formatted metrics data

**Example:**
```python
metrics = tools.worklocal_get_metrics(
    resource_id="res-123",
    metric_type="cpu",
    timeframe="24h"
)
```

---

#### worklocal_search_resources(query, filters="{}")

Search for resources based on query and filters.

**Parameters:**
- `query` (str): Search query string
- `filters` (str, optional): JSON string containing search filters. Default: "{}"

**Returns:**
- `str`: Search results

**Example:**
```python
results = tools.worklocal_search_resources(
    query="production",
    filters='{"type": "server", "status": "running", "region": "us-east-1"}'
)
```

## Error Handling

All methods include built-in error handling and return user-friendly messages:

- ✅ Success messages (operations completed successfully)
- ⚠️ Warning messages (non-fatal issues, like HTTP status codes)
- ❌ Error messages (failures, exceptions, or critical errors)

## Response Format

All methods return formatted strings suitable for display in OpenWebUI:
- Markdown formatting for better readability
- Emoji indicators for quick status recognition
- Structured data presentation with headers and lists
- Code blocks for IDs and technical details

## Authentication

To use authenticated endpoints, update the headers in the Tools class:

```python
self.headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}
```

Or for API key authentication:

```python
self.headers = {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY"
}
```