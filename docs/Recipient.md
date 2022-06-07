# Recipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email | [optional] 
**external_id** | **str** | A unique string that MagicBell can utilize to uniquely identify the user. We recommend setting this attribute to the ID of the user in your database. Provide the external id if the user&#39;s email is unavailable. | [optional] 
**matches** | **str** | An SQL-like expression to match users by their stored attributes. Set it to \&quot;*\&quot; to send a notification to all users. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


