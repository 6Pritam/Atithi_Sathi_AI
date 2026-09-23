import React, { useState } from 'react';

const ChatInput = ({ onSendMessage, isLoading }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    if (e) e.preventDefault();
    const trimmed = input.trim();
    if (trimmed && !isLoading) {
      onSendMessage(trimmed);
      setInput('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="fixed bottom-0 left-0 md:left-72 right-0 bg-gradient-to-t from-surface via-surface to-transparent pt-12 pb-space-lg px-space-lg z-30">
      <div className="max-w-4xl mx-auto w-full relative">
        <div className="absolute -top-12 left-1/2 -translate-x-1/2 w-32 h-10 bg-gradient-to-t from-surface-container-low/50 to-transparent blur-xl pointer-events-none"></div>
        <form 
          onSubmit={handleSubmit}
          className="relative bg-surface-container-lowest rounded-[24px] shadow-[0_4px_24px_rgba(0,0,0,0.06)] ring-1 ring-surface-container-highest transition-all duration-300 hover:shadow-[0_8px_32px_rgba(0,0,0,0.08)] flex items-center p-2"
        >
          <button aria-label="Upload document" className="p-2.5 rounded-full text-on-surface-variant hover:text-on-surface hover:bg-surface-container transition-colors" type="button">
            <span className="material-symbols-outlined text-[22px]">attach_file</span>
          </button>
          <input 
            className="flex-1 bg-transparent border-none outline-none font-body-lg text-body-lg text-on-surface px-3 py-3 placeholder:text-on-surface-variant/60" 
            placeholder="Ask about availability, amenities, or policies..." 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isLoading}
          />
          <div className="flex items-center gap-1.5 pr-2">
            <button aria-label="Voice input" className="p-2.5 rounded-full text-on-surface-variant hover:text-on-surface hover:bg-surface-container transition-colors" type="button">
              <span className="material-symbols-outlined text-[22px]">mic</span>
            </button>
            <button 
              aria-label="Send message" 
              className="p-3 rounded-full bg-primary text-on-primary hover:bg-primary-container hover:shadow-md transition-all active:scale-95 disabled:opacity-50 disabled:active:scale-100" 
              type="submit"
              disabled={isLoading || !input.trim()}
            >
              <span className="material-symbols-outlined text-[20px] ml-0.5">send</span>
            </button>
          </div>
        </form>
        <div className="text-center mt-3">
          <span className="font-label-sm text-label-sm text-on-surface-variant/70">Concierge AI may produce inaccurate results. Verify critical booking details.</span>
        </div>
      </div>
    </div>
  );
};

export default ChatInput;
