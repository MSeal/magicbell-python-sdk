# magicbell.UsersApi

All URIs are relative to *https://api.magicbell.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update a user


# **create_user**
> WrappedUser create_user(wrapped_user=wrapped_user)

Create a user

Create a user. Please note that you must provide the user's email or the external id so MagicBell can uniquely identify the user.  The external id, if provided, must be unique to the user.

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
    api_instance = magicbell.UsersApi(api_client)
    wrapped_user = {"user":{"external_id":"56780","email":"hana@supportbee.com","first_name":"Hana","last_name":"Mohan","custom_attributes":{"plan":"enterprise","pricing_version":"v10","preferred_pronoun":"She"}}} # WrappedUser |  (optional)

    try:
        # Create a user
        api_response = api_instance.create_user(wrapped_user=wrapped_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
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
    api_instance = magicbell.UsersApi(api_client)
    wrapped_user = {"user":{"external_id":"56780","email":"hana@supportbee.com","first_name":"Hana","last_name":"Mohan","custom_attributes":{"plan":"enterprise","pricing_version":"v10","preferred_pronoun":"She"}}} # WrappedUser |  (optional)

    try:
        # Create a user
        api_response = api_instance.create_user(wrapped_user=wrapped_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wrapped_user** | [**WrappedUser**](WrappedUser.md)|  | [optional] 

### Return type

[**WrappedUser**](WrappedUser.md)

### Authorization

[AuthAPIKeyAuth](../README.md#AuthAPIKeyAuth), [AuthAPISecretAuth](../README.md#AuthAPISecretAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user

Delete a user by id, email or external_id.  We will delete the user completely 7 days after. If the user makes a request to the API, the deletion will be canceled. This will happen when the notification inbox for this user is loaded in your app, for example.

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
    api_instance = magicbell.UsersApi(api_client)
    user_id = 'user_id_example' # str | The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.

    try:
        # Delete a user
        api_instance.delete_user(user_id)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
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
    api_instance = magicbell.UsersApi(api_client)
    user_id = 'user_id_example' # str | The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.

    try:
        # Delete a user
        api_instance.delete_user(user_id)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id is the MagicBell user id. Alternatively, provide an id like &#x60;email:theusersemail@example.com&#x60; or &#x60;external_id:theusersexternalid&#x60; as the user id. | 

### Return type

void (empty response body)

### Authorization

[AuthAPIKeyAuth](../README.md#AuthAPIKeyAuth), [AuthAPISecretAuth](../README.md#AuthAPISecretAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> WrappedUser update_user(user_id, wrapped_user=wrapped_user)

Update a user

Update a user's data. If you identify users by their email addresses, you need to update the MagicBell data, so this user can still access their notifications.

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
    api_instance = magicbell.UsersApi(api_client)
    user_id = 'user_id_example' # str | The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
wrapped_user = {"user":{"email":"hana@magicbell.io"}} # WrappedUser |  (optional)

    try:
        # Update a user
        api_response = api_instance.update_user(user_id, wrapped_user=wrapped_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
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
    api_instance = magicbell.UsersApi(api_client)
    user_id = 'user_id_example' # str | The user id is the MagicBell user id. Alternatively, provide an id like `email:theusersemail@example.com` or `external_id:theusersexternalid` as the user id.
wrapped_user = {"user":{"email":"hana@magicbell.io"}} # WrappedUser |  (optional)

    try:
        # Update a user
        api_response = api_instance.update_user(user_id, wrapped_user=wrapped_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id is the MagicBell user id. Alternatively, provide an id like &#x60;email:theusersemail@example.com&#x60; or &#x60;external_id:theusersexternalid&#x60; as the user id. | 
 **wrapped_user** | [**WrappedUser**](WrappedUser.md)|  | [optional] 

### Return type

[**WrappedUser**](WrappedUser.md)

### Authorization

[AuthAPIKeyAuth](../README.md#AuthAPIKeyAuth), [AuthAPISecretAuth](../README.md#AuthAPISecretAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Validation error |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

