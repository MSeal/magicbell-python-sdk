# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of the notification. | 
**category** | **str** | Category the notification belongs to. This is useful to allow users to set their preferences. | [optional] 
**content** | **str** | Content of the notification. If you provide HTML content, the notification inbox will render it correctly. | [optional] 
**action_url** | **str** | A URL to redirect the user to when they click the notification in their notification inbox. | [optional] 
**recipients** | [**list[Recipient]**](Recipient.md) |  | 
**custom_attributes** | **dict(str, object)** | Set of key-value pairs that you can attach to a notification. It accepts objects for the value of a key.  You can use it to share data between channels or to render a custom UI. | [optional] 
**topic** | **str** | Topic the notification belongs to. This is useful to create threads. | [optional] 
**overrides** | [**NotificationOverrides**](NotificationOverrides.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


