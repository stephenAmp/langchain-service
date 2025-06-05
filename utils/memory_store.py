from langchain.memory import ConversationBufferMemory;
from threading import Lock;
from cachetools import TTLCache # For auto-expiry

class InMemoryStore:
    def __init__(self, max_sessions=1000, expiry_time=3600):
        """
        Max session refers to total sessions number memory can store
        expiry time is time taken for memory to auto delete
        """
        # Initialize dictionary to store session memories
        self._store = TTLCache(max_sessions, expiry_time)

        # Create lock to make operations thread-safe
        self._lock = Lock()

    def get_memory(self, session_id:str)-> ConversationBufferMemory:
        # Thread-safe access to store dictionary
        with self._lock:

            # If memory for session_id doesnt exist create it
            if session_id not in self._store:
                self._store[session_id] = ConversationBufferMemory(
                    return_messages=True,
                    memory_key="chat_history"
                )
        # Return memory object for session id
        return self._store[session_id]
    
    def clear_memory(self, session_id:str):
        # Enabling thread-safe operation
        with self._lock:
            #   Remove session
            self._store.pop(session_id, None)

    def clear_all(self):
        # Wipe all saved sessions
        with self._lock:
            self._store.clear()

# Global instance to be used throughout app
store = InMemoryStore(max_sessions=1000, expiry_time=3600)
