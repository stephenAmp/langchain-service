from langchain_community.chat_message_histories import ChatMessageHistory
from threading import Lock
from cachetools import TTLCache # For auto-expiry

class InMemoryStore:
    def __init__(self, max_sessions=1000, expiry_time=3600):
        """
        Initializes a thread-safe, expiring in-memory store for chat histories.

        Args:
            max_sessions (int): The maximum number of chat sessions to store.
            expiry_time (int): The time in seconds after which a session expires.
        """
        # Initialize a Time-to-Live (TTL) cache to store session histories.
        # This automatically purges sessions that haven't been accessed for the expiry_time.
        self._store = TTLCache(maxsize=max_sessions, ttl=expiry_time)

        # Create a lock to ensure that operations on the store are thread-safe,
        # preventing race conditions when multiple threads access it simultaneously.
        self._lock = Lock()

    def get_history(self, session_id: str) -> ChatMessageHistory:
        """
        Retrieves the chat history for a given session ID.
        If no history exists for the session, a new one is created.

        Args:
            session_id (str): The unique identifier for the chat session.

        Returns:
            ChatMessageHistory: The chat history object for the session.
        """
        # Acquire the lock to ensure exclusive access to the store.
        with self._lock:
            # If a history for the session_id doesn't exist in the store, create one.
            if session_id not in self._store:
                self._store[session_id] = ChatMessageHistory()
        
        # Return the ChatMessageHistory object for the given session ID.
        return self._store[session_id]
    
    def clear_memory(self, session_id: str):
        """
        Removes a specific session's history from the store.

        Args:
            session_id (str): The identifier of the session to remove.
        """
        # Acquire the lock for a thread-safe operation.
        with self._lock:
            # Use pop with a default value of None to avoid an error if the key doesn't exist.
            self._store.pop(session_id, None)

    def clear_all(self):
        """
        Wipes all saved chat histories from the store.
        """
        # Acquire the lock to safely clear the entire store.
        with self._lock:
            self._store.clear()

# Create a global instance of the store to be used throughout the application.
# This ensures that all parts of the app share the same memory store.
store = InMemoryStore(max_sessions=1000, expiry_time=3600)
