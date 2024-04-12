from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId

"""
This interface is the output port of the DeleteChatsUseCase. It is used to delete the chats.
"""
class DeleteChatsPort:
       
    """
    Deletes the chats and returns the response.
    Args:
        chatsIdsList (List[ChatId]): The chats to delete.
    Returns:
        List[ChatOperationResponse]: The response of the operation.
    """ 
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        pass