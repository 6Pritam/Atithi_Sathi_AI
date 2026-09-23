import React, { useEffect, useState } from 'react';
import { getRecentConversations } from '../../api/client';

const Sidebar = ({ onNewChat, onSelectConversation, currentConversationId, refreshCounter }) => {
  const [conversations, setConversations] = useState([]);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const data = await getRecentConversations();
        setConversations(data.conversations || []);
      } catch (err) {
        console.error("Failed to load history", err);
      }
    };
    fetchHistory();
  }, [refreshCounter]);

  return (
    <aside className="hidden md:flex fixed left-0 top-0 h-full w-72 bg-surface-container-low z-50 flex-col justify-between shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
      <div className="flex flex-col h-full overflow-hidden">
        <div className="h-16 px-space-md flex items-center gap-space-sm">
          <div className="h-8 w-8 rounded-lg bg-gradient-to-tr from-primary to-secondary flex items-center justify-center shrink-0 shadow-sm">
            <span className="material-symbols-outlined text-[20px] text-on-primary">real_estate_agent</span>
          </div>
          <div className="flex flex-col">
            <span className="font-headline-sm text-headline-sm text-on-surface tracking-tight leading-none">Atithi Saathi AI</span>
            <span className="font-label-sm text-label-sm text-secondary tracking-wider uppercase mt-0.5 font-semibold">Travel Concierge</span>
          </div>
        </div>
        <div className="px-space-md pt-space-xs pb-space-sm">
          <button onClick={onNewChat} className="w-full flex items-center justify-between px-space-md py-space-sm bg-primary text-on-primary rounded-xl font-label-lg text-label-lg transition-transform active:scale-[0.98] shadow-sm" type="button">
            <span className="flex items-center gap-space-xs">
              <span className="material-symbols-outlined text-[20px]">add</span>New Conversation
            </span>
            <span className="font-label-sm text-label-sm bg-primary-container text-on-primary-container px-space-xs py-0.5 rounded-lg opacity-90">Ctrl+K</span>
          </button>
        </div>
        <div className="flex-1 overflow-y-auto px-space-md space-y-space-md pt-space-xs">
          <nav className="space-y-space-xs">
            <div className="font-label-sm text-label-sm text-on-surface-variant uppercase tracking-wider px-space-xs mb-space-xs">Recent History</div>
            {conversations.map(conv => {
              const isActive = conv.id === currentConversationId;
              return (
                <button 
                  key={conv.id} 
                  onClick={() => onSelectConversation(conv.id)}
                  className={`w-full flex items-center gap-space-xs px-space-sm py-2 rounded-xl text-left truncate transition-colors ${isActive ? 'bg-surface-container-highest text-on-surface font-semibold' : 'text-on-surface-variant hover:bg-surface-container hover:text-on-surface'}`}
                >
                  <span className="material-symbols-outlined text-[18px] shrink-0">chat_bubble</span>
                  <span className="truncate font-body-sm text-body-sm">{conv.title || "Conversation"}</span>
                </button>
              );
            })}
          </nav>
        </div>
        <div className="p-space-md bg-surface-container-low space-y-space-xs shadow-[0_-1px_6px_rgba(0,0,0,0.02)]">
          <div className="flex items-center justify-between px-space-xs py-1 text-secondary">
            <div className="flex items-center gap-space-xs">
              <span className="h-2 w-2 rounded-full bg-secondary animate-pulse"></span>
              <span className="font-label-sm text-label-sm font-semibold">Live Concierge AI</span>
            </div>
            <span className="font-label-sm text-label-sm bg-secondary-container text-on-secondary-container px-space-xs py-0.5 rounded-full">Ready</span>
          </div>
          <button className="w-full flex items-center gap-space-xs px-space-xs py-1.5 text-on-surface-variant hover:text-on-surface transition-colors font-body-sm text-body-sm text-left" type="button">
            <span className="material-symbols-outlined text-[18px]">help</span>Guest Support
          </button>
          <button className="w-full flex items-center gap-space-xs px-space-xs py-1.5 text-on-surface-variant hover:text-on-surface transition-colors font-body-sm text-body-sm text-left" type="button">
            <span className="material-symbols-outlined text-[18px]">delete_sweep</span>Clear History
          </button>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
