# notion_client.BlocksApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_blocks_id_children_get**](BlocksApi.md#v1_blocks_id_children_get) | **GET** /v1/blocks/{id}/children | Retrieve block children
[**v1_blocks_id_children_patch**](BlocksApi.md#v1_blocks_id_children_patch) | **PATCH** /v1/blocks/{id}/children | Append block children
[**v1_blocks_id_delete**](BlocksApi.md#v1_blocks_id_delete) | **DELETE** /v1/blocks/{id} | Delete a block
[**v1_blocks_id_get**](BlocksApi.md#v1_blocks_id_get) | **GET** /v1/blocks/{id} | Retrieve a block
[**v1_blocks_id_patch**](BlocksApi.md#v1_blocks_id_patch) | **PATCH** /v1/blocks/{id} | Update a block


# **v1_blocks_id_children_get**
> object v1_blocks_id_children_get(id, notion_version=notion_version, page_size=page_size)

Retrieve block children

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import notion_client
from notion_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.notion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = notion_client.Configuration(
    host = "https://api.notion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = notion_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notion_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notion_client.BlocksApi(api_client)
    id = '{{PAGE_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    page_size = 100 # int |  (optional)

    try:
        # Retrieve block children
        api_response = api_instance.v1_blocks_id_children_get(id, notion_version=notion_version, page_size=page_size)
        print("The response of BlocksApi->v1_blocks_id_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocksApi->v1_blocks_id_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **notion_version** | **str**|  | [optional]
 **page_size** | **int**|  | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * Set-Cookie -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * cf-request-id -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blocks_id_children_patch**
> object v1_blocks_id_children_patch(id, authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)

Append block children

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import notion_client
from notion_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.notion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = notion_client.Configuration(
    host = "https://api.notion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = notion_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notion_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notion_client.BlocksApi(api_client)
    id = '{{PAGE_ID}}' # str |
    authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Append block children
        api_response = api_instance.v1_blocks_id_children_patch(id, authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)
        print("The response of BlocksApi->v1_blocks_id_children_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocksApi->v1_blocks_id_children_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **authorization** | **str**|  | [optional]
 **content_type** | **str**|  | [optional]
 **notion_version** | **str**|  | [optional]
 **body** | **str**|  | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * Set-Cookie -  <br>  * ETag -  <br>  * Vary -  <br>  * CF-Cache-Status -  <br>  * cf-request-id -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  * Content-Encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blocks_id_delete**
> object v1_blocks_id_delete(id, notion_version=notion_version)

Delete a block

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import notion_client
from notion_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.notion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = notion_client.Configuration(
    host = "https://api.notion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = notion_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notion_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notion_client.BlocksApi(api_client)
    id = '{{BLOCK_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)

    try:
        # Delete a block
        api_response = api_instance.v1_blocks_id_delete(id, notion_version=notion_version)
        print("The response of BlocksApi->v1_blocks_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocksApi->v1_blocks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **notion_version** | **str**|  | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * ETag -  <br>  * Vary -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  * Content-Encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blocks_id_get**
> object v1_blocks_id_get(id, notion_version=notion_version)

Retrieve a block

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import notion_client
from notion_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.notion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = notion_client.Configuration(
    host = "https://api.notion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = notion_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notion_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notion_client.BlocksApi(api_client)
    id = '{{BLOCK_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)

    try:
        # Retrieve a block
        api_response = api_instance.v1_blocks_id_get(id, notion_version=notion_version)
        print("The response of BlocksApi->v1_blocks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocksApi->v1_blocks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **notion_version** | **str**|  | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * Set-Cookie -  <br>  * ETag -  <br>  * Vary -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  * Content-Encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_blocks_id_patch**
> object v1_blocks_id_patch(id, notion_version=notion_version, body=body)

Update a block

This endpoint allows you to update block content. [See Full Documentation](https://developers.notion.com/reference/update-a-block)

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import os
import notion_client
from notion_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.notion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = notion_client.Configuration(
    host = "https://api.notion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = notion_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notion_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notion_client.BlocksApi(api_client)
    id = '{{BLOCK_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update a block
        api_response = api_instance.v1_blocks_id_patch(id, notion_version=notion_version, body=body)
        print("The response of BlocksApi->v1_blocks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlocksApi->v1_blocks_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **notion_version** | **str**|  | [optional]
 **body** | **object**|  | [optional]

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * Set-Cookie -  <br>  * ETag -  <br>  * Vary -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  * Content-Encoding -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
