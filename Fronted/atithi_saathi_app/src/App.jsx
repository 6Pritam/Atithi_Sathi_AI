import React, { useState, useEffect } from 'react'
import Sidebar from './components/layout/Sidebar'
import Header from './components/layout/Header'
import WelcomeEmptyState from './components/views/WelcomeEmptyState'
import ActiveAssistant from './components/views/ActiveAssistant'
import ChatInput from './components/ui/ChatInput'
import { sendChatMessage, getConversationHistory, getRecentConversations } from './api/client'

function App() {
  const [currentView, setCurrentView] = useState('empty');
  const [messages, setMessages] = useState([]);
  const [conversationId, setConversationId] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [historyRefreshCounter, setHistoryRefreshCounter] = useState(0);

  const handleSendMessage = async (text) => {
    // Optimistically add user message
    const tempUserMsg = { id: Date.now().toString(), sender: 'user', content: text };
    setMessages(prev => [...prev, tempUserMsg]);
    setCurrentView('active');
    setIsLoading(true);
    setError(null);

    try {
      const data = await sendChatMessage(text, conversationId);
      
      // Update conversation ID if it's the first message
      if (!conversationId && data.conversation_id) {
        setConversationId(data.conversation_id);
        setHistoryRefreshCounter(c => c + 1); // Trigger sidebar history refresh
      }

      const aiMsg = {
        id: (Date.now() + 1).toString(),
        sender: 'ai',
        content: data.message,
        attached_data: data.attachments
      };
      setMessages(prev => [...prev, aiMsg]);
    } catch (err) {
      setError(err.message || "I’m sorry, I couldn’t process that request right now. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSelectConversation = async (id) => {
    try {
      setIsLoading(true);
      setError(null);
      const data = await getConversationHistory(id);
      setConversationId(id);
      setMessages(data.messages);
      setCurrentView('active');
    } catch (err) {
      console.error(err);
      setError("Failed to load conversation history.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewChat = () => {
    setConversationId(null);
    setMessages([]);
    setCurrentView('empty');
    setError(null);
  };

  return (
    <div className="bg-surface font-body-md text-body-md text-on-surface antialiased min-h-screen">
      <Sidebar 
        onNewChat={handleNewChat} 
        onSelectConversation={handleSelectConversation}
        currentConversationId={conversationId}
        refreshCounter={historyRefreshCounter}
      />
      <div className="pl-0 md:pl-72 transition-all">
        <Header onNewChat={handleNewChat} />
        <main className="relative pt-16 bg-surface min-h-[calc(100vh-140px)] pb-56 w-full">
          {currentView === 'empty' ? (
            <WelcomeEmptyState onSendMessage={handleSendMessage} />
          ) : (
            <ActiveAssistant 
              messages={messages} 
              isLoading={isLoading} 
              error={error}
            />
          )}
        </main>
        <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
      </div>
    </div>
  )
}

export default App
