import React from 'react';

const Header = ({ onNewChat }) => {
  return (
    <header className="fixed top-0 left-0 md:left-72 right-0 h-16 bg-surface/85 backdrop-blur-xl z-40 flex items-center justify-between px-space-lg shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
      <div className="flex items-center gap-space-sm">
        <div className="flex items-center gap-space-xs px-space-sm py-1 bg-surface-container-low rounded-full">
          <span className="material-symbols-outlined text-[18px] text-secondary">hotel_class</span>
          <span className="font-label-md text-label-md text-on-surface hidden md:inline-block">Session Active: Karnataka Stays &amp; Bookings</span>
        </div>
        <span className="font-label-sm text-label-sm bg-secondary-container text-on-secondary-container px-space-sm py-0.5 rounded-full font-medium hidden md:inline-block">Verified Inventory</span>
      </div>
      <div className="flex items-center gap-space-md">
        <button onClick={onNewChat} className="flex items-center gap-space-xs px-space-sm py-1.5 bg-surface-container-low hover:bg-surface-container hover:text-on-surface text-on-surface-variant rounded-xl font-label-md text-label-md transition-colors" type="button">
          <span className="material-symbols-outlined text-[18px]">add</span>
          <span>New</span>
          <kbd className="bg-surface font-label-sm text-label-sm px-1.5 py-0.5 rounded text-on-surface-variant">Ctrl+K</kbd>
        </button>
        <button aria-label="Search conversations" className="text-on-surface-variant hover:text-on-surface p-1.5 rounded-lg hover:bg-surface-container transition-colors" type="button">
          <span className="material-symbols-outlined text-[22px]">search</span>
        </button>
        <button aria-label="Guest preferences" className="text-on-surface-variant hover:text-on-surface p-1.5 rounded-lg hover:bg-surface-container transition-colors" type="button">
          <span className="material-symbols-outlined text-[22px]">settings</span>
        </button>
        <div className="flex items-center gap-space-xs pl-space-xs">
          <div className="w-8 h-8 rounded-full bg-surface-container-high flex items-center justify-center ring-2 ring-surface-container-highest text-on-surface-variant">
            <span className="material-symbols-outlined text-[20px]">person</span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
