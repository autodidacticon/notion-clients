# notion_client.CommentsApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_comments_get**](CommentsApi.md#v1_comments_get) | **GET** /v1/comments | Retrieve comments
[**v1_comments_post**](CommentsApi.md#v1_comments_post) | **POST** /v1/comments | Add comment to discussion


# **v1_comments_get**
> object v1_comments_get(notion_version=notion_version, block_id=block_id, page_size=page_size)

Retrieve comments

Retrieve a user object using the ID specified in the request path.

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
    api_instance = notion_client.CommentsApi(api_client)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    block_id = '{{BLOCK_ID}}' # str |  (optional)
    page_size = 100 # int |  (optional)

    try:
        # Retrieve comments
        api_response = api_instance.v1_comments_get(notion_version=notion_version, block_id=block_id, page_size=page_size)
        print("The response of CommentsApi->v1_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notion_version** | **str**|  | [optional]
 **block_id** | **str**|  | [optional]
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
**200** | OK |  * Content-Security-Policy -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-Permitted-Cross-Domain-Policies -  <br>  * Referrer-Policy -  <br>  * X-XSS-Protection -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * ETag -  <br>  * Vary -  <br>  * Date -  <br>  * Connection -  <br>  * Keep-Alive -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_comments_post**
> object v1_comments_post(content_type=content_type, notion_version=notion_version, body=body)

Add comment to discussion

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
    api_instance = notion_client.CommentsApi(api_client)
    content_type = 'application/json' # str |  (optional)
    notion_version = '{{NOTION_VERSION}}' # str |  (optional)
    body = 'body_example' # str |  (optional)

    try:
        # Add comment to discussion
        api_response = api_instance.v1_comments_post(content_type=content_type, notion_version=notion_version, body=body)
        print("The response of CommentsApi->v1_comments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->v1_comments_post: %s\n" % e)
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
**200** | OK |  * Content-Security-Policy -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Frame-Options -  <br>  * Strict-Transport-Security -  <br>  * X-Download-Options -  <br>  * X-Content-Type-Options -  <br>  * X-Permitted-Cross-Domain-Policies -  <br>  * Referrer-Policy -  <br>  * X-XSS-Protection -  <br>  * Content-Type -  <br>  * Content-Length -  <br>  * ETag -  <br>  * Vary -  <br>  * Date -  <br>  * Connection -  <br>  * Keep-Alive -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
