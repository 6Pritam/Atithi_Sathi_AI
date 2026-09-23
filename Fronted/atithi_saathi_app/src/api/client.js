const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

export const sendChatMessage = async (message, conversationId = null) => {
  const payload = { message };
  if (conversationId) {
    payload.conversation_id = conversationId;
  }

  const response = await fetch(`${API_BASE_URL}/api/v1/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    let errorDetail = "An error occurred";
    try {
      const errorData = await response.json();
      errorDetail = errorData?.error?.message || errorDetail;
    } catch (e) {
      // JSON parse failed
    }
    throw new Error(errorDetail);
  }

  const data = await response.json();
  if (data.success === false) {
    throw new Error(data.error?.message || "An AI service error occurred.");
  }
  return data;
};

export const getConversationHistory = async (conversationId) => {
  const response = await fetch(`${API_BASE_URL}/api/v1/history/${conversationId}`);
  if (!response.ok) {
    throw new Error("Failed to fetch conversation history");
  }
  return response.json();
};

export const getRecentConversations = async () => {
  const response = await fetch(`${API_BASE_URL}/api/v1/history`);
  if (!response.ok) {
    throw new Error("Failed to fetch recent conversations");
  }
  return response.json();
};

export const healthCheck = async () => {
  const response = await fetch(`${API_BASE_URL}/api/v1/health`);
  return response.json();
};
