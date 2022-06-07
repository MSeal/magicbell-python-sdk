# magicbell.RealTimeApi

All URIs are relative to *https://api.magicbell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](RealTimeApi.md#create_notification) | **POST** /notifications | Create notifications


# **create_notification**
> CreateNotification201Response create_notification(wrapped_notification=wrapped_notification)

Create notifications

Send a notification to one or multiple users. You can identify users by their email address or by an external_id.  You don't have to import your users into MagicBell. If a user does not exist we'll create it automatically.  The new notification will be shown in the notification inbox of each recipient in real-time. It will also be delivered to each recipient through all channels your have enabled for your MagicBell project.

### Example

* Api Key Authentication (AuthAPIKeyAuth):
```python
from __future__ import print_function
import time
import magicbell
from magicbell.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.magicbell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = magicbell.Configuration(
    host = "https://api.magicbell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthAPIKeyAuth
configuration.api_key['AuthAPIKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthAPIKeyAuth'] = 'Bearer'

# Configure API key authorization: AuthAPISecretAuth
configuration.api_key['AuthAPISecretAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthAPISecretAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with magicbell.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = magicbell.RealTimeApi(api_client)
    wrapped_notification = {"notification":{"title":"We're processing your order","content":"<p>Thank you for your order. We'll notify you when these items are ready.</p>","category":"order_created","topic":"order:33098","recipients":[{"email":"dan@example.com"},{"external_id":"83d987a-83fd034"},{"matches":"custom_attributes.order.id = 88492"}],"overrides":{"email":{"title":"[MagicBell] We're processing your order","content":"Thank you for your order. If you need help, or have any questions please don't hesitate to reach out to us directly at hello@magicbell.io"}}}} # WrappedNotification |  (optional)

    try:
        # Create notifications
        api_response = api_instance.create_notification(wrapped_notification=wrapped_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->create_notification: %s\n" % e)
```

* Api Key Authentication (AuthAPISecretAuth):
```python
from __future__ import print_function
import time
import magicbell
from magicbell.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.magicbell.com
# See configuration.py for a list of all supported configuration parameters.
configuration = magicbell.Configuration(
    host = "https://api.magicbell.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AuthAPIKeyAuth
configuration.api_key['AuthAPIKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthAPIKeyAuth'] = 'Bearer'

# Configure API key authorization: AuthAPISecretAuth
configuration.api_key['AuthAPISecretAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthAPISecretAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with magicbell.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = magicbell.RealTimeApi(api_client)
    wrapped_notification = {"notification":{"title":"We're processing your order","content":"<p>Thank you for your order. We'll notify you when these items are ready.</p>","category":"order_created","topic":"order:33098","recipients":[{"email":"dan@example.com"},{"external_id":"83d987a-83fd034"},{"matches":"custom_attributes.order.id = 88492"}],"overrides":{"email":{"title":"[MagicBell] We're processing your order","content":"Thank you for your order. If you need help, or have any questions please don't hesitate to reach out to us directly at hello@magicbell.io"}}}} # WrappedNotification |  (optional)

    try:
        # Create notifications
        api_response = api_instance.create_notification(wrapped_notification=wrapped_notification)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RealTimeApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wrapped_notification** | [**WrappedNotification**](WrappedNotification.md)|  | [optional] 

### Return type

[**CreateNotification201Response**](CreateNotification201Response.md)

### Authorization

[AuthAPIKeyAuth](../README.md#AuthAPIKeyAuth), [AuthAPISecretAuth](../README.md#AuthAPISecretAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Invalid data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

