import React from 'react';

const WelcomeEmptyState = ({ onSendMessage }) => {
  return (
    <div className="relative w-full max-w-4xl mx-auto px-margin md:px-margin-desktop py-space-xl flex flex-col items-center justify-center">
      {/* Atmospheric Halo Decorators (contained) */}
      <div className="absolute top-12 left-1/2 -translate-x-1/2 w-96 h-96 bg-gradient-to-tr from-primary-fixed-dim/20 via-surface-container-high/40 to-secondary-container/20 rounded-full blur-3xl pointer-events-none -z-10"></div>
      <div className="absolute top-36 right-1/4 w-48 h-48 bg-primary/5 rounded-full blur-2xl pointer-events-none -z-10"></div>

      {/* Centered Brand Presence & Logo Halo */}
      <div className="relative flex items-center justify-center mb-space-lg group">
        <div className="absolute -inset-4 rounded-full bg-gradient-to-br from-primary-fixed via-surface-container-low to-secondary-fixed opacity-70 blur-md transition-all duration-700 group-hover:opacity-100 group-hover:scale-105"></div>
        <div className="relative w-24 h-24 rounded-full bg-surface-container-lowest p-3 shadow-lg flex items-center justify-center">
          <div className="w-full h-full rounded-full bg-gradient-to-tr from-primary to-secondary flex items-center justify-center drop-shadow-sm transition-transform duration-300 group-hover:scale-95">
            <span className="material-symbols-outlined text-[42px] text-on-primary">real_estate_agent</span>
          </div>
        </div>
        {/* Ambient subtle badge pill */}
        <div className="absolute -bottom-2.5 px-3 py-0.5 rounded-full bg-surface-container-highest shadow-sm flex items-center gap-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-secondary animate-pulse"></span>
          <span className="font-label-sm text-label-sm text-secondary tracking-widest uppercase">Atithi Concierge</span>
        </div>
      </div>

      {/* Elegant Typography Block */}
      <div className="text-center max-w-2xl mx-auto space-y-space-xs mb-space-xl">
        <div className="inline-flex items-center gap-2 mb-1">
          <span className="font-headline-lg text-headline-lg text-on-surface tracking-tight">Namaste</span>
          <span className="font-headline-lg text-headline-lg select-none">🙏</span>
        </div>
        <h1 className="font-headline-xl text-headline-xl text-on-surface tracking-tight">
          How can I help with your stay?
        </h1>
        <p className="font-body-lg text-body-lg text-on-surface-variant pt-space-xs leading-relaxed max-w-xl mx-auto">
          Your bespoke AI hotel companion. Inquire about rooms, amenities, verified policies, luxury availability, or curate an effortless stay itinerary across premier Indian properties.
        </p>
      </div>

      {/* Intelligent Suggestion Chips */}
      <div className="w-full mb-space-xl">
        <div className="flex items-center justify-center gap-2 mb-space-sm text-on-surface-variant">
          <span className="material-symbols-outlined text-[18px] text-primary">auto_awesome</span>
          <span className="font-label-sm text-label-sm uppercase tracking-wider font-semibold">Curated Inquiries &amp; Shortcuts</span>
        </div>
        <div className="flex flex-wrap items-center justify-center gap-2.5 max-w-3xl mx-auto">
          <SuggestionChip icon="🏨" text="Find a hotel in Bengaluru" onClick={() => onSendMessage('Find a hotel in Bengaluru')} />
          <SuggestionChip icon="📅" text="Check room availability" onClick={() => onSendMessage('Check room availability')} />
          <SuggestionChip icon="🛏️" text="Compare Deluxe vs Suite rooms" onClick={() => onSendMessage('Compare Deluxe vs Suite rooms')} />
          <SuggestionChip icon="☕" text="Hotel amenities &amp; breakfast options" onClick={() => onSendMessage('Hotel amenities & breakfast options')} />
          <SuggestionChip icon="🛡️" text="Check cancellation policies" onClick={() => onSendMessage('Check cancellation policies')} />
          <SuggestionChip icon="✈️" text="Airport transit &amp; early check-in" onClick={() => onSendMessage('Airport transit & early check-in')} />
        </div>
      </div>

      {/* Quick Category Bento Tiles */}
      <div className="w-full grid grid-cols-1 md:grid-cols-3 gap-space-md mb-space-xl">
        {/* Tile 1: Instant Availability */}
        <div className="group relative bg-surface-container-lowest rounded-xl p-space-lg shadow-sm hover:shadow-md transition-all duration-300 flex flex-col justify-between overflow-hidden">
          <div className="absolute -right-6 -bottom-6 w-28 h-28 bg-secondary-container/30 rounded-full blur-xl group-hover:scale-125 transition-transform duration-500"></div>
          <div className="relative space-y-space-sm">
            <div className="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-secondary group-hover:bg-secondary group-hover:text-on-secondary transition-colors duration-300 shadow-sm">
              <span className="material-symbols-outlined text-[22px]">calendar_clock</span>
            </div>
            <div className="space-y-1">
              <h3 className="font-headline-sm text-headline-sm text-on-surface flex items-center justify-between">
                Instant Availability
                <span className="material-symbols-outlined text-[18px] text-outline opacity-0 group-hover:opacity-100 transition-opacity">arrow_forward</span>
              </h3>
              <p className="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
                Real-time date &amp; guest capacity verification across verified luxury villas, business hubs, and heritage palatial stays.
              </p>
            </div>
          </div>
          <div className="mt-space-md pt-space-sm flex items-center justify-between">
            <span className="font-label-sm text-label-sm text-secondary bg-secondary-container px-2 py-0.5 rounded-full font-medium">99.8% Sync Rate</span>
            <span className="font-label-sm text-label-sm text-on-surface-variant">Instant Lock</span>
          </div>
        </div>

        {/* Tile 2: Personalized Amenities */}
        <div className="group relative bg-surface-container-lowest rounded-xl p-space-lg shadow-sm hover:shadow-md transition-all duration-300 flex flex-col justify-between overflow-hidden">
          <div className="absolute -right-6 -bottom-6 w-28 h-28 bg-primary-fixed/40 rounded-full blur-xl group-hover:scale-125 transition-transform duration-500"></div>
          <div className="relative space-y-space-sm">
            <div className="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-primary group-hover:bg-primary group-hover:text-on-primary transition-colors duration-300 shadow-sm">
              <span className="material-symbols-outlined text-[22px]">spa</span>
            </div>
            <div className="space-y-1">
              <h3 className="font-headline-sm text-headline-sm text-on-surface flex items-center justify-between">
                Personalized Amenities
                <span className="material-symbols-outlined text-[18px] text-outline opacity-0 group-hover:opacity-100 transition-opacity">arrow_forward</span>
              </h3>
              <p className="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
                Custom dietary preferences, high-frequency Wi-Fi configurations, private ayurvedic therapies, and infant bedding additions.
              </p>
            </div>
          </div>
          <div className="mt-space-md pt-space-sm flex items-center justify-between">
            <span className="font-label-sm text-label-sm text-primary bg-primary-fixed px-2 py-0.5 rounded-full font-medium">Concierge Curated</span>
            <span className="font-label-sm text-label-sm text-on-surface-variant">Pre-arrival Setup</span>
          </div>
        </div>

        {/* Tile 3: Transparent Policies */}
        <div className="group relative bg-surface-container-lowest rounded-xl p-space-lg shadow-sm hover:shadow-md transition-all duration-300 flex flex-col justify-between overflow-hidden">
          <div className="absolute -right-6 -bottom-6 w-28 h-28 bg-surface-container-highest rounded-full blur-xl group-hover:scale-125 transition-transform duration-500"></div>
          <div className="relative space-y-space-sm">
            <div className="w-10 h-10 rounded-lg bg-surface-container-low flex items-center justify-center text-on-surface-variant group-hover:bg-on-surface group-hover:text-surface transition-colors duration-300 shadow-sm">
              <span className="material-symbols-outlined text-[22px]">verified_user</span>
            </div>
            <div className="space-y-1">
              <h3 className="font-headline-sm text-headline-sm text-on-surface flex items-center justify-between">
                Transparent Policies
                <span className="material-symbols-outlined text-[18px] text-outline opacity-0 group-hover:opacity-100 transition-opacity">arrow_forward</span>
              </h3>
              <p className="font-body-sm text-body-sm text-on-surface-variant leading-relaxed">
                Unambiguous summaries on pet allowances, state tax breakdowns in INR (₹), refund timelines, and quiet-hour guidelines.
              </p>
            </div>
          </div>
          <div className="mt-space-md pt-space-sm flex items-center justify-between">
            <span className="font-label-sm text-label-sm text-on-surface bg-surface-container-high px-2 py-0.5 rounded-full font-medium">Zero Hidden Fees</span>
            <span className="font-label-sm text-label-sm text-on-surface-variant">Official T&amp;C</span>
          </div>
        </div>
      </div>

      {/* Editorial Hospitality Inspiration Strip */}
      <div className="w-full bg-surface-container-low rounded-xl p-space-md flex flex-col sm:flex-row items-center justify-between gap-space-md shadow-sm">
        <div className="flex items-center gap-space-md">
          <div className="w-12 h-12 rounded-lg bg-surface-container-lowest flex items-center justify-center text-primary shrink-0 shadow-sm">
            <span className="material-symbols-outlined text-[26px]">room_service</span>
          </div>
          <div className="space-y-0.5">
            <div className="font-label-lg text-label-lg text-on-surface font-semibold flex items-center gap-2">
              <span>Special Culinary &amp; Heritage Tours</span>
              <span className="bg-primary/10 text-primary font-label-sm text-label-sm px-2 py-0.2 rounded-full">New</span>
            </div>
            <p className="font-body-sm text-body-sm text-on-surface-variant">
              Discover curated coffee plantation trails in Coorg or private sunset high-tea reservations at Kabini riverside.
            </p>
          </div>
        </div>
        <button className="shrink-0 flex items-center gap-1.5 px-space-md py-2 rounded-xl bg-surface-container-lowest hover:bg-surface-container-high text-primary font-label-md text-label-md transition-colors shadow-sm" type="button">
          <span>Explore Ideas</span>
          <span className="material-symbols-outlined text-[16px]">chevron_right</span>
        </button>
      </div>

    </div>
  );
};

// SuggestionChip component directly here or could be separated
const SuggestionChip = ({ icon, text, onClick }) => {
  return (
    <button onClick={onClick} className="group flex items-center gap-2 px-space-md py-2.5 rounded-full bg-surface-container-lowest shadow-sm hover:bg-surface-container hover:shadow-md transition-all duration-200 active:scale-95 text-on-surface" type="button">
      <span className="text-[17px]">{icon}</span>
      <span className="font-label-lg text-label-lg group-hover:text-primary transition-colors">{text}</span>
      <span className="material-symbols-outlined text-[16px] text-outline opacity-0 -translate-x-1 group-hover:opacity-100 group-hover:translate-x-0 transition-all">north_east</span>
    </button>
  );
};

export default WelcomeEmptyState;
