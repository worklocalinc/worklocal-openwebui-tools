"""
WorkLocal Studio Infrastructure API Tools for OpenWebUI
"""

import requests
import json
from typing import Dict, List, Optional, Any

class Tools:
    def __init__(self):
        self.base_url = "https://worklocal.app"
        # If you have path-based routing in Google Cloud Gateway:
        # self.base_url = "https://worklocal.app/api"
        # self.base_url = "https://worklocal.app/tools"
        
        self.headers = {
            "Content-Type": "application/json",
            # "Authorization": "Bearer YOUR_API_KEY"  # Uncomment and add if needed
            # "X-API-Key": "YOUR_API_KEY"  # Alternative auth header
        }

    def worklocal_health_check(self) -> str:
        """
        Check if the WorkLocal Studio API is healthy and accessible.
        
        Returns:
            str: Health status of the API
        """
        try:
            response = requests.get(
                f"{self.base_url}/health",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                return f"✅ WorkLocal Studio API is healthy. Status: {response.text}"
            else:
                return f"⚠️ API returned status code: {response.status_code}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error connecting to API: {str(e)}"

    def worklocal_list_resources(self, resource_type: str = "all") -> str:
        """
        List infrastructure resources from WorkLocal Studio.
        
        Args:
            resource_type (str): Type of resources to list (e.g., 'servers', 'containers', 'all')
            
        Returns:
            str: Formatted list of resources
        """
        try:
            endpoint = f"{self.base_url}/resources"
            params = {} if resource_type == "all" else {"type": resource_type}
            
            response = requests.get(
                endpoint,
                headers=self.headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                resources = response.json()
                
                # Format the response
                output = f"📋 **WorkLocal Resources ({resource_type})**\n\n"
                
                if isinstance(resources, list):
                    for idx, resource in enumerate(resources, 1):
                        output += f"{idx}. **{resource.get('name', 'Unnamed')}**\n"
                        output += f"   - Type: {resource.get('type', 'Unknown')}\n"
                        output += f"   - Status: {resource.get('status', 'Unknown')}\n"
                        output += f"   - ID: `{resource.get('id', 'N/A')}`\n\n"
                elif isinstance(resources, dict):
                    for key, value in resources.items():
                        output += f"- **{key}**: {value}\n"
                else:
                    output += f"Raw response: {resources}\n"
                    
                return output
            else:
                return f"⚠️ API returned status code: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error listing resources: {str(e)}"

    def worklocal_get_resource(self, resource_id: str) -> str:
        """
        Get detailed information about a specific resource.
        
        Args:
            resource_id (str): The ID of the resource to retrieve
            
        Returns:
            str: Formatted resource details
        """
        try:
            response = requests.get(
                f"{self.base_url}/resources/{resource_id}",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                resource = response.json()
                
                # Format the response
                output = f"🔍 **Resource Details**\n\n"
                output += f"**ID**: `{resource.get('id', resource_id)}`\n"
                output += f"**Name**: {resource.get('name', 'Unnamed')}\n"
                output += f"**Type**: {resource.get('type', 'Unknown')}\n"
                output += f"**Status**: {resource.get('status', 'Unknown')}\n"
                output += f"**Created**: {resource.get('created_at', 'Unknown')}\n"
                output += f"**Updated**: {resource.get('updated_at', 'Unknown')}\n\n"
                
                # Add any additional metadata
                if 'metadata' in resource:
                    output += "**Metadata**:\n"
                    for key, value in resource['metadata'].items():
                        output += f"  - {key}: {value}\n"
                
                return output
            elif response.status_code == 404:
                return f"❌ Resource with ID '{resource_id}' not found"
            else:
                return f"⚠️ API returned status code: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error getting resource: {str(e)}"

    def worklocal_create_resource(self, name: str, resource_type: str, config: str = "{}") -> str:
        """
        Create a new infrastructure resource.
        
        Args:
            name (str): Name of the resource to create
            resource_type (str): Type of resource (e.g., 'server', 'container', 'database')
            config (str): JSON string containing additional configuration
            
        Returns:
            str: Creation result message
        """
        try:
            # Parse the config string
            try:
                config_dict = json.loads(config)
            except json.JSONDecodeError:
                return "❌ Invalid JSON in config parameter. Please provide valid JSON."
            
            payload = {
                "name": name,
                "type": resource_type,
                "config": config_dict
            }
            
            response = requests.post(
                f"{self.base_url}/resources",
                headers=self.headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code in [200, 201]:
                resource = response.json()
                return f"✅ Resource created successfully!\n\n**ID**: `{resource.get('id', 'N/A')}`\n**Name**: {name}\n**Type**: {resource_type}"
            else:
                return f"⚠️ Failed to create resource. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error creating resource: {str(e)}"

    def worklocal_update_resource(self, resource_id: str, updates: str) -> str:
        """
        Update an existing infrastructure resource.
        
        Args:
            resource_id (str): ID of the resource to update
            updates (str): JSON string containing the updates
            
        Returns:
            str: Update result message
        """
        try:
            # Parse the updates string
            try:
                updates_dict = json.loads(updates)
            except json.JSONDecodeError:
                return "❌ Invalid JSON in updates parameter. Please provide valid JSON."
            
            response = requests.patch(
                f"{self.base_url}/resources/{resource_id}",
                headers=self.headers,
                json=updates_dict,
                timeout=10
            )
            
            if response.status_code == 200:
                return f"✅ Resource '{resource_id}' updated successfully!"
            elif response.status_code == 404:
                return f"❌ Resource with ID '{resource_id}' not found"
            else:
                return f"⚠️ Failed to update resource. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error updating resource: {str(e)}"

    def worklocal_delete_resource(self, resource_id: str) -> str:
        """
        Delete an infrastructure resource.
        
        Args:
            resource_id (str): ID of the resource to delete
            
        Returns:
            str: Deletion result message
        """
        try:
            response = requests.delete(
                f"{self.base_url}/resources/{resource_id}",
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code in [200, 204]:
                return f"✅ Resource '{resource_id}' deleted successfully!"
            elif response.status_code == 404:
                return f"❌ Resource with ID '{resource_id}' not found"
            else:
                return f"⚠️ Failed to delete resource. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error deleting resource: {str(e)}"

    def worklocal_execute_action(self, resource_id: str, action: str, parameters: str = "{}") -> str:
        """
        Execute an action on a resource (e.g., start, stop, restart).
        
        Args:
            resource_id (str): ID of the resource
            action (str): Action to execute (e.g., 'start', 'stop', 'restart')
            parameters (str): JSON string containing action parameters
            
        Returns:
            str: Action execution result
        """
        try:
            # Parse the parameters string
            try:
                params_dict = json.loads(parameters)
            except json.JSONDecodeError:
                return "❌ Invalid JSON in parameters. Please provide valid JSON."
            
            payload = {
                "action": action,
                "parameters": params_dict
            }
            
            response = requests.post(
                f"{self.base_url}/resources/{resource_id}/actions",
                headers=self.headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                return f"✅ Action '{action}' executed successfully on resource '{resource_id}'\n\nResult: {result.get('message', 'Success')}"
            elif response.status_code == 404:
                return f"❌ Resource with ID '{resource_id}' not found"
            else:
                return f"⚠️ Failed to execute action. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error executing action: {str(e)}"

    def worklocal_get_metrics(self, resource_id: str, metric_type: str = "all", timeframe: str = "1h") -> str:
        """
        Get metrics for a specific resource.
        
        Args:
            resource_id (str): ID of the resource
            metric_type (str): Type of metrics to retrieve (e.g., 'cpu', 'memory', 'network', 'all')
            timeframe (str): Timeframe for metrics (e.g., '1h', '24h', '7d')
            
        Returns:
            str: Formatted metrics data
        """
        try:
            params = {
                "type": metric_type,
                "timeframe": timeframe
            }
            
            response = requests.get(
                f"{self.base_url}/resources/{resource_id}/metrics",
                headers=self.headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                metrics = response.json()
                
                output = f"📊 **Metrics for Resource '{resource_id}'**\n"
                output += f"*Timeframe: {timeframe}*\n\n"
                
                if isinstance(metrics, dict):
                    for metric_name, metric_data in metrics.items():
                        output += f"**{metric_name.upper()}**:\n"
                        if isinstance(metric_data, dict):
                            output += f"  - Current: {metric_data.get('current', 'N/A')}\n"
                            output += f"  - Average: {metric_data.get('average', 'N/A')}\n"
                            output += f"  - Max: {metric_data.get('max', 'N/A')}\n"
                            output += f"  - Min: {metric_data.get('min', 'N/A')}\n"
                        else:
                            output += f"  {metric_data}\n"
                        output += "\n"
                else:
                    output += f"Raw metrics: {metrics}\n"
                
                return output
            elif response.status_code == 404:
                return f"❌ Resource with ID '{resource_id}' not found"
            else:
                return f"⚠️ Failed to get metrics. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error getting metrics: {str(e)}"

    def worklocal_search_resources(self, query: str, filters: str = "{}") -> str:
        """
        Search for resources based on query and filters.
        
        Args:
            query (str): Search query string
            filters (str): JSON string containing search filters
            
        Returns:
            str: Search results
        """
        try:
            # Parse the filters string
            try:
                filters_dict = json.loads(filters) if filters else {}
            except json.JSONDecodeError:
                return "❌ Invalid JSON in filters parameter. Please provide valid JSON."
            
            params = {
                "q": query,
                **filters_dict
            }
            
            response = requests.get(
                f"{self.base_url}/resources/search",
                headers=self.headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                results = response.json()
                
                output = f"🔍 **Search Results for '{query}'**\n\n"
                
                if isinstance(results, list) and results:
                    output += f"Found {len(results)} resources:\n\n"
                    for idx, resource in enumerate(results, 1):
                        output += f"{idx}. **{resource.get('name', 'Unnamed')}** (`{resource.get('id', 'N/A')}`)\n"
                        output += f"   - Type: {resource.get('type', 'Unknown')}\n"
                        output += f"   - Status: {resource.get('status', 'Unknown')}\n\n"
                elif isinstance(results, list):
                    output += "No resources found matching your search criteria."
                else:
                    output += f"Results: {results}"
                
                return output
            else:
                return f"⚠️ Search failed. Status: {response.status_code}\nResponse: {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"❌ Error searching resources: {str(e)}"