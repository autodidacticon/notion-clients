# notion_client.DatabasesApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_databases_id_get**](DatabasesApi.md#v1_databases_id_get) | **GET** /v1/databases/{id} | Retrieve a database
[**v1_databases_id_patch**](DatabasesApi.md#v1_databases_id_patch) | **PATCH** /v1/databases/{id} | Update a database
[**v1_databases_id_query_post**](DatabasesApi.md#v1_databases_id_query_post) | **POST** /v1/databases/{id}/query | Query a database
[**v1_databases_post**](DatabasesApi.md#v1_databases_post) | **POST** /v1/databases/ | Create a database


# **v1_databases_id_get**
> object v1_databases_id_get(id, notion_version=notion_version)

Retrieve a database

Retrieves a database object using the ID specified in the request path.

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
    api_instance = notion_client.DatabasesApi(api_client)
    id = '{{DATABASE_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)

    try:
        # Retrieve a database
        api_response = api_instance.v1_databases_id_get(id, notion_version=notion_version)
        print("The response of DatabasesApi->v1_databases_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->v1_databases_id_get: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_databases_id_patch**
> object v1_databases_id_patch(id, notion_version=notion_version, body=body)

Update a database

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
    api_instance = notion_client.DatabasesApi(api_client)
    id = 'id_example' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Update a database
        api_response = api_instance.v1_databases_id_patch(id, notion_version=notion_version, body=body)
        print("The response of DatabasesApi->v1_databases_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->v1_databases_id_patch: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_databases_id_query_post**
> object v1_databases_id_query_post(id, authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)

Query a database

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
    api_instance = notion_client.DatabasesApi(api_client)
    id = '{{DATABASE_ID}}' # str |
    authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Query a database
        api_response = api_instance.v1_databases_id_query_post(id, authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)
        print("The response of DatabasesApi->v1_databases_id_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->v1_databases_id_query_post: %s\n" % e)
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_databases_post**
> object v1_databases_post(content_type=content_type, notion_version=notion_version, body=body)

Create a database

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
    api_instance = notion_client.DatabasesApi(api_client)
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Create a database
        api_response = api_instance.v1_databases_post(content_type=content_type, notion_version=notion_version, body=body)
        print("The response of DatabasesApi->v1_databases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->v1_databases_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * Set-Cookie -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
