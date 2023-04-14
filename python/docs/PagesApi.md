# notion_client.PagesApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_pages_id_get**](PagesApi.md#v1_pages_id_get) | **GET** /v1/pages/{id} | Retrieve a Page
[**v1_pages_id_patch**](PagesApi.md#v1_pages_id_patch) | **PATCH** /v1/pages/{id} | Update Page properties
[**v1_pages_page_id_properties_property_id_get**](PagesApi.md#v1_pages_page_id_properties_property_id_get) | **GET** /v1/pages/{page_id}/properties/{property_id} | Retrieve a Page Property Item
[**v1_pages_post**](PagesApi.md#v1_pages_post) | **POST** /v1/pages/ | Create a Page with Content


# **v1_pages_id_get**
> object v1_pages_id_get(id, notion_version=notion_version)

Retrieve a Page

Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content.

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
    api_instance = notion_client.PagesApi(api_client)
    id = '{{PAGE_ID}}' # str |
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)

    try:
        # Retrieve a Page
        api_response = api_instance.v1_pages_id_get(id, notion_version=notion_version)
        print("The response of PagesApi->v1_pages_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->v1_pages_id_get: %s\n" % e)
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

# **v1_pages_id_patch**
> object v1_pages_id_patch(id, content_type=content_type, notion_version=notion_version, body=body)

Update Page properties

Updates a page by setting the values of any properties specified in the JSON body of the request. Properties not updated via parameters will remain unchanged.

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
    api_instance = notion_client.PagesApi(api_client)
    id = '{{PAGE_ID}}' # str |
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Update Page properties
        api_response = api_instance.v1_pages_id_patch(id, content_type=content_type, notion_version=notion_version, body=body)
        print("The response of PagesApi->v1_pages_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->v1_pages_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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
**200** | OK |  * Date -  <br>  * Content-Type -  <br>  * Transfer-Encoding -  <br>  * Connection -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-XSS-Protection -  <br>  * Referrer-Policy -  <br>  * Content-Security-Policy -  <br>  * X-Content-Security-Policy -  <br>  * X-WebKit-CSP -  <br>  * Set-Cookie -  <br>  * ETag -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * CF-Cache-Status -  <br>  * cf-request-id -  <br>  * Expect-CT -  <br>  * Server -  <br>  * CF-RAY -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pages_page_id_properties_property_id_get**
> object v1_pages_page_id_properties_property_id_get(page_id, property_id)

Retrieve a Page Property Item

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
    api_instance = notion_client.PagesApi(api_client)
    page_id = '{{PAGE_ID}}' # str |
    property_id = 'property_id_example' # str |

    try:
        # Retrieve a Page Property Item
        api_response = api_instance.v1_pages_page_id_properties_property_id_get(page_id, property_id)
        print("The response of PagesApi->v1_pages_page_id_properties_property_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->v1_pages_page_id_properties_property_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**|  |
 **property_id** | **str**|  |

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

# **v1_pages_post**
> object v1_pages_post(authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)

Create a Page with Content

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
    api_instance = notion_client.PagesApi(api_client)
    authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Create a Page with Content
        api_response = api_instance.v1_pages_post(authorization=authorization, content_type=content_type, notion_version=notion_version, body=body)
        print("The response of PagesApi->v1_pages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PagesApi->v1_pages_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
