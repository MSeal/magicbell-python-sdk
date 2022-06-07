# Notifications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID of the MagicBell project these notifications belong to. | [optional] [readonly] 
**total** | **int** | Total number of notifications for this user. | [optional] [readonly] 
**per_page** | **int** | Number of notifications per page. | [optional] [readonly] 
**total_pages** | **int** | Total number of pages. | [optional] [readonly] 
**current_page** | **int** | Number of the page returned. | [optional] [readonly] 
**unseen_count** | **int** | Number of unseen notifications. Any filters applied affect this number. | [optional] [readonly] 
**unread_count** | **int** | Number of unread notifications. Any filters applied affect this number. | [optional] [readonly] 
**notifications** | [**list[Notification]**](Notification.md) | List of all notifications in the current page | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


