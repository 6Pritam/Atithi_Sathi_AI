import React from 'react';
import ReactMarkdown from 'react-markdown';

const HotelCard = ({ hotel }) => {
  const imageSrc = hotel.image_url || "https://lh3.googleusercontent.com/aida-public/AB6AXuAlLgmZwdK0o8dUpgdDbD9ICJLF6ctMY3SuG6N3D-84lXPrdH9tdiAx8jPHydr3y_6OMfMzpAcYV3n9PmZ_bOTd7wo8a5oFY773U0cVvjiTNepM34dAVMp4u_wG2lza0e38mdorgBOInbhGy8nJjMkSevIuEHohgbFZfH5N0uGDF43bako2KW8v0sd6CPos7hx_KjPTFF0wmCpoMfDp3F2086yinvqx3svKyU876nCkfYPmjmtndJp7SQ";
  const rating = hotel.rating || "4.5";
  const reviews = hotel.review_count || "100+";
  const location = hotel.location || "Bengaluru";
  const name = hotel.name || "Hotel";
  const distanceInfo = "City center";
  
  let amenitiesList = [];
  if (Array.isArray(hotel.amenities)) {
    amenitiesList = hotel.amenities;
  } else if (typeof hotel.amenities === 'string') {
    amenitiesList = hotel.amenities.split(',').map(a => a.trim());
  } else {
    amenitiesList = ["Wi-Fi", "Parking"];
  }

  const price = hotel.price ? `₹${hotel.price.toLocaleString('en-IN')}` : "Contact for price";
  const totalInfo = "+ taxes & fees";

  return (
    <div className="bg-surface-container-lowest rounded-2xl shadow-sm p-4 flex flex-col justify-between hover:shadow-md transition-shadow group">
      <div className="flex flex-col gap-3">
        <div className="relative w-full h-44 rounded-xl overflow-hidden bg-surface-container">
          <img className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" src={imageSrc} alt={name}/>
          <span className="absolute top-3 left-3 bg-surface-container-lowest/90 backdrop-blur-md px-2.5 py-1 rounded-full font-label-sm text-label-sm text-on-surface font-semibold flex items-center gap-1 shadow-sm">
            <span className="material-symbols-outlined text-[15px] text-amber-600 fill-1">star</span> {rating}
            <span className="text-on-surface-variant font-normal">({reviews})</span>
          </span>
          <span className="absolute bottom-3 right-3 bg-secondary text-on-secondary px-2.5 py-1 rounded-full font-label-sm text-label-sm font-medium shadow-sm">
            {location}
          </span>
        </div>
        <div>
          <h3 className="font-headline-sm text-headline-sm text-on-surface">{name}</h3>
          <p className="font-body-sm text-body-sm text-on-surface-variant flex items-center gap-1 mt-0.5">
            <span className="material-symbols-outlined text-[16px] text-primary">location_on</span>
            {distanceInfo}
          </p>
        </div>
        <div className="flex flex-wrap gap-1.5 pt-1">
          {amenitiesList.slice(0,3).map((amenity, index) => (
            <span key={index} className={index === 0 ? "bg-secondary-container/50 text-secondary px-2.5 py-1 rounded-full font-label-sm text-label-sm font-medium" : "bg-surface-container text-on-surface-variant px-2.5 py-1 rounded-full font-label-sm text-label-sm"}>
              ✓ {amenity}
            </span>
          ))}
        </div>
      </div>
      <div className="mt-4 pt-3 flex items-center justify-between">
        <div className="flex flex-col">
          <div className="flex items-baseline gap-1">
            <span className="font-headline-sm text-headline-sm text-on-surface">{price}</span>
            <span className="font-body-sm text-body-sm text-on-surface-variant">/ night</span>
          </div>
          <span className="font-label-sm text-label-sm text-outline">{totalInfo}</span>
        </div>
        <div className="flex items-center gap-2">
          <button className="px-3.5 py-1.5 rounded-xl font-label-md text-label-md bg-primary text-on-primary hover:bg-primary-container transition-all active:scale-95 shadow-sm" type="button">Book</button>
        </div>
      </div>
    </div>
  );
};

const RoomCard = ({ room }) => {
  const imageSrc = room.image_url || "https://lh3.googleusercontent.com/aida-public/AB6AXuBqbiRV5kWG18G7M6QbapHhhl1iCVLE9WDycMCy_3FMLmrJQF-p6_LKvjEZLbM_EPkyYslfABATbL_jeEnLSslcYig80Pga2iHHtTfLidLDxux8QesvXRwGk2wh362ievcnMoziTj6TVnp5xF-vwyF1gu9r73UJ11JeWgs_g8ueA74ftCOSDJUFR6dKeNLPM_5KaSZ-wqCtW6sihSQDMkwb5GO0MGhsfTI0n-i4jgbOaWLgy8d17caY5Q";
  const price = room.price_per_night ? `₹${room.price_per_night.toLocaleString('en-IN')}` : "Contact for price";
  const guests = room.max_guests || 2;
  const name = room.name || "Standard Room";

  return (
    <div className="bg-surface-container-lowest rounded-2xl shadow-sm p-4 sm:p-5 flex flex-col lg:flex-row gap-5 items-stretch hover:shadow-md transition-shadow">
      <div className="w-full lg:w-64 h-48 lg:h-auto rounded-xl overflow-hidden bg-surface-container shrink-0 relative">
        <img className="w-full h-full object-cover" src={imageSrc} alt="Room"/>
        <span className="absolute top-2.5 left-2.5 bg-secondary text-on-secondary px-2 py-0.5 rounded-full font-label-sm text-label-sm font-semibold">
          Instant Confirmation
        </span>
      </div>
      <div className="flex-1 flex flex-col justify-between gap-3">
        <div>
          <div className="flex flex-wrap items-center justify-between gap-2">
            <h4 className="font-headline-md text-headline-md text-on-surface">{name}</h4>
            <div className="text-right">
              <span className="font-headline-md text-headline-md text-primary">{price}</span>
              <span className="font-body-sm text-body-sm text-on-surface-variant">/ night</span>
            </div>
          </div>
          <div className="flex flex-wrap gap-y-1 gap-x-4 mt-2 font-label-md text-label-md text-on-surface-variant">
            <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px] text-secondary">group</span> {guests} Guests max</span>
            <span className="flex items-center gap-1"><span className="material-symbols-outlined text-[16px] text-secondary">bed</span> King Bed</span>
          </div>
          <p className="font-body-sm text-body-sm text-on-surface mt-2.5">
            {room.amenities || "Includes espresso machine, high-pressure rain shower, and fast Wi-Fi."}
          </p>
        </div>
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-3 bg-surface-container-low/50 -mx-4 -mb-4 sm:-mx-5 sm:-mb-5 p-4 rounded-b-2xl">
          <span className="font-label-sm text-label-sm text-outline">+ taxes & fees</span>
          <div className="flex items-center gap-2">
             <button className="px-4 py-2 rounded-xl font-label-md text-label-md bg-primary text-on-primary hover:bg-primary-container transition-all shadow-sm" type="button">Book Now</button>
          </div>
        </div>
      </div>
    </div>
  );
};

const ActiveAssistant = ({ messages, isLoading, error }) => {
  return (
    <div className="max-w-4xl mx-auto w-full px-space-md sm:px-space-lg pb-12 flex flex-col gap-y-space-xl">
      {messages.map((msg, index) => {
        if (msg.sender === 'user') {
          return (
            <div key={msg.id || index} className="flex flex-col items-end w-full pl-8 sm:pl-24">
              <div className="bg-[#EFECE6] text-on-surface rounded-2xl rounded-tr-none px-space-md py-3.5 shadow-sm max-w-xl">
                <p className="font-body-md text-body-md text-on-surface leading-relaxed whitespace-pre-wrap">
                  {msg.content}
                </p>
              </div>
              <div className="flex items-center gap-1.5 mt-1 mr-1">
                <span className="font-label-sm text-label-sm text-outline">You</span>
              </div>
            </div>
          );
        } else {
          return (
            <div key={msg.id || index} className="flex flex-col items-start w-full pr-0 sm:pr-8">
              <div className="flex items-center gap-space-sm mb-2.5">
                <div className="w-7 h-7 rounded-md bg-gradient-to-tr from-primary to-secondary flex items-center justify-center shrink-0 shadow-sm">
                  <span className="material-symbols-outlined text-[16px] text-on-primary">real_estate_agent</span>
                </div>
                <div className="flex items-center gap-2">
                  <span className="font-headline-sm text-headline-sm text-on-surface">Atithi Saathi AI</span>
                  <span className="px-2 py-0.5 rounded-full bg-secondary-container text-on-secondary-container font-label-sm text-label-sm font-semibold">Verified Concierge</span>
                </div>
              </div>
              {msg.content && (
                <div className="max-w-3xl w-full">
                  <ReactMarkdown 
                    className="font-body-lg text-body-lg text-on-surface leading-relaxed"
                    components={{
                      p: ({node, ...props}) => <p className="mb-4 last:mb-0" {...props} />,
                      strong: ({node, ...props}) => <strong className="font-semibold text-primary" {...props} />,
                      ul: ({node, ...props}) => <ul className="list-disc pl-6 mb-4 space-y-1" {...props} />,
                      ol: ({node, ...props}) => <ol className="list-decimal pl-6 mb-4 space-y-1" {...props} />,
                      li: ({node, ...props}) => <li className="pl-1" {...props} />,
                      h3: ({node, ...props}) => <h3 className="font-headline-sm text-headline-sm mt-6 mb-3 text-on-surface" {...props} />,
                      a: ({node, ...props}) => <a className="text-secondary hover:underline" {...props} />
                    }}
                  >
                    {msg.content}
                  </ReactMarkdown>
                </div>
              )}
              
              {msg.attached_data && msg.attached_data.length > 0 && (
                <div className="w-full mt-4 flex flex-col gap-4">
                  {msg.attached_data.map((attachment, aIndex) => {
                    if (attachment.type === 'hotel_list' && attachment.data) {
                      return (
                        <div key={aIndex} className="grid grid-cols-1 md:grid-cols-2 gap-space-md w-full">
                          {attachment.data.map(h => <HotelCard key={h.id} hotel={h} />)}
                        </div>
                      );
                    }
                    if (attachment.type === 'hotel' && attachment.data) {
                      return (
                         <div key={aIndex} className="grid grid-cols-1 md:grid-cols-2 gap-space-md w-full">
                          <HotelCard hotel={attachment.data} />
                         </div>
                      );
                    }
                    if (attachment.type === 'room' && attachment.data) {
                      const rooms = Array.isArray(attachment.data) ? attachment.data : [attachment.data];
                      return (
                        <div key={aIndex} className="flex flex-col gap-4 w-full">
                          {rooms.map(r => <RoomCard key={r.id} room={r} />)}
                        </div>
                      );
                    }
                    return null;
                  })}
                </div>
              )}
            </div>
          );
        }
      })}

      {isLoading && (
        <div className="flex flex-col items-start w-full">
          <div className="flex items-center gap-space-sm mb-2">
            <img alt="Atithi Saathi AI" className="w-7 h-7 rounded-md object-contain shadow-sm" src="https://lh3.googleusercontent.com/aida/AEtjO1UYE4JHd8hKI9SLrDbFBmC9GUPK1Tkxm60jio0ncCwgUUug52f3-dp2L8TPf2ljZINuyXMwpgOmx2i4k0sy1_SGpfo-jIghq_johzGhXAxSQZi8KDw5tDf41UVglwHtYlhvNcgUOU-dYvgmnG2yHRUpMjjVFWc46RKBaqhHMH9hRDYoS5YEudjcDgHeXUaWaPYoX-_VKetkOcn97IKFsLD9g-tMfsQg982Pa9e0TqfrppO4DjmM8myAg-XG"/>
            <span className="font-headline-sm text-headline-sm text-on-surface">Atithi Saathi AI</span>
          </div>
          <div className="inline-flex items-center gap-2.5 px-4 py-2 rounded-full bg-surface-container shadow-sm">
            <span className="relative flex h-2.5 w-2.5">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-secondary opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-secondary"></span>
            </span>
            <span className="font-label-md text-label-md text-on-surface-variant font-medium">
              Thinking...
            </span>
          </div>
        </div>
      )}

      {error && (
        <div className="flex flex-col items-start w-full mt-2">
          <div className="bg-error-container text-on-error-container px-4 py-3 rounded-xl max-w-xl">
             <span className="font-label-md text-label-md">{error}</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default ActiveAssistant;
