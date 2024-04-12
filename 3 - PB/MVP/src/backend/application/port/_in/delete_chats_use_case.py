from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse   
from domain.chat.chat_id import ChatId

"""
This class is the interface of the DeleteChatsUseCase.
"""
class DeleteChatsUseCase:
       
    """
    Deletes the chats and returns the response.
    Args:
        chatsIdsList (List[ChatId]): The chats to delete.
    Returns:
        List[ChatOperationResponse]: The response of the operation.
    """ 
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        pass