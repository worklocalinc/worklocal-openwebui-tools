import pytest
from unittest.mock import Mock, patch
import json
from src.worklocal_tools import Tools

class TestWorkLocalTools:
    @pytest.fixture
    def tools(self):
        return Tools()
    
    @pytest.fixture
    def mock_response(self):
        """Create a mock response object"""
        mock = Mock()
        mock.status_code = 200
        mock.text = "OK"
        mock.json.return_value = {}
        return mock
    
    @patch('requests.get')
    def test_health_check_success(self, mock_get, tools):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "OK"
        
        result = tools.worklocal_health_check()
        
        assert "✅" in result
        assert "healthy" in result
        mock_get.assert_called_once_with(
            "https://worklocal.app/health",
            headers={"Content-Type": "application/json"},
            timeout=10
        )
    
    @patch('requests.get')
    def test_health_check_failure(self, mock_get, tools):
        mock_get.return_value.status_code = 500
        
        result = tools.worklocal_health_check()
        
        assert "⚠️" in result
        assert "500" in result
    
    @patch('requests.get')
    def test_list_resources_all(self, mock_get, tools, mock_response):
        mock_response.json.return_value = [
            {"id": "1", "name": "server1", "type": "server", "status": "running"},
            {"id": "2", "name": "server2", "type": "server", "status": "stopped"}
        ]
        mock_get.return_value = mock_response
        
        result = tools.worklocal_list_resources()
        
        assert "server1" in result
        assert "server2" in result
        assert "running" in result
        assert "stopped" in result
    
    @patch('requests.get')
    def test_list_resources_filtered(self, mock_get, tools, mock_response):
        mock_response.json.return_value = [
            {"id": "1", "name": "server1", "type": "server", "status": "running"}
        ]
        mock_get.return_value = mock_response
        
        result = tools.worklocal_list_resources("servers")
        
        mock_get.assert_called_with(
            "https://worklocal.app/resources",
            headers={"Content-Type": "application/json"},
            params={"type": "servers"},
            timeout=10
        )
    
    @patch('requests.get')
    def test_get_resource_success(self, mock_get, tools, mock_response):
        mock_response.json.return_value = {
            "id": "res-123",
            "name": "test-server",
            "type": "server",
            "status": "running",
            "created_at": "2024-01-01T00:00:00Z",
            "updated_at": "2024-01-02T00:00:00Z"
        }
        mock_get.return_value = mock_response
        
        result = tools.worklocal_get_resource("res-123")
        
        assert "test-server" in result
        assert "res-123" in result
        assert "running" in result
    
    @patch('requests.get')
    def test_get_resource_not_found(self, mock_get, tools):
        mock_get.return_value.status_code = 404
        
        result = tools.worklocal_get_resource("invalid-id")
        
        assert "❌" in result
        assert "not found" in result
    
    @patch('requests.post')
    def test_create_resource_success(self, mock_post, tools, mock_response):
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": "new-123"}
        mock_post.return_value = mock_response
        
        result = tools.worklocal_create_resource(
            name="test-server",
            resource_type="server",
            config='{"cpu": 2}'
        )
        
        assert "✅" in result
        assert "created successfully" in result
        
        # Verify the payload
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args.kwargs['json']['name'] == "test-server"
        assert call_args.kwargs['json']['type'] == "server"
        assert call_args.kwargs['json']['config'] == {"cpu": 2}
    
    @patch('requests.post')
    def test_create_resource_invalid_json(self, mock_post, tools):
        result = tools.worklocal_create_resource(
            name="test",
            resource_type="server",
            config="invalid json"
        )
        
        assert "❌" in result
        assert "Invalid JSON" in result
        mock_post.assert_not_called()
    
    @patch('requests.patch')
    def test_update_resource_success(self, mock_patch, tools, mock_response):
        mock_patch.return_value = mock_response
        
        result = tools.worklocal_update_resource(
            resource_id="res-123",
            updates='{"cpu": 4}'
        )
        
        assert "✅" in result
        assert "updated successfully" in result
    
    @patch('requests.delete')
    def test_delete_resource_success(self, mock_delete, tools):
        mock_delete.return_value.status_code = 204
        
        result = tools.worklocal_delete_resource("res-123")
        
        assert "✅" in result
        assert "deleted successfully" in result
    
    @patch('requests.post')
    def test_execute_action_success(self, mock_post, tools, mock_response):
        mock_response.json.return_value = {"message": "Server started"}
        mock_post.return_value = mock_response
        
        result = tools.worklocal_execute_action(
            resource_id="res-123",
            action="start"
        )
        
        assert "✅" in result
        assert "start" in result
        assert "Server started" in result
    
    @patch('requests.get')
    def test_get_metrics_success(self, mock_get, tools, mock_response):
        mock_response.json.return_value = {
            "cpu": {
                "current": 45.5,
                "average": 40.2,
                "max": 78.9,
                "min": 12.3
            },
            "memory": {
                "current": 62.1,
                "average": 58.7,
                "max": 85.4,
                "min": 45.2
            }
        }
        mock_get.return_value = mock_response
        
        result = tools.worklocal_get_metrics("res-123")
        
        assert "CPU" in result
        assert "45.5" in result
        assert "MEMORY" in result
        assert "62.1" in result
    
    @patch('requests.get')
    def test_search_resources_success(self, mock_get, tools, mock_response):
        mock_response.json.return_value = [
            {"id": "1", "name": "prod-server", "type": "server", "status": "running"},
            {"id": "2", "name": "prod-db", "type": "database", "status": "running"}
        ]
        mock_get.return_value = mock_response
        
        result = tools.worklocal_search_resources(
            query="prod",
            filters='{"status": "running"}'
        )
        
        assert "Found 2 resources" in result
        assert "prod-server" in result
        assert "prod-db" in result
    
    @patch('requests.get')
    def test_search_resources_no_results(self, mock_get, tools, mock_response):
        mock_response.json.return_value = []
        mock_get.return_value = mock_response
        
        result = tools.worklocal_search_resources("nonexistent")
        
        assert "No resources found" in result