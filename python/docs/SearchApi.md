# notion_client.SearchApi

All URIs are relative to *https://api.notion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_search_post**](SearchApi.md#v1_search_post) | **POST** /v1/search | Search


# **v1_search_post**
> object v1_search_post(content_type=content_type, notion_version=notion_version, body=body)

Search

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
    api_instance = notion_client.SearchApi(api_client)
    content_type = 'application/json' # str |  (optional)
    notion_version = '2022-06-28' # str |  (optional) (default to '2022-06-28')
    body = 'body_example' # str |  (optional)

    try:
        # Search
        api_response = api_instance.v1_search_post(content_type=content_type, notion_version=notion_version, body=body)
        print("The response of SearchApi->v1_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->v1_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional]
 **notion_version** | **str**|  | [optional] [default to &#39;2022-06-28&#39;]
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
