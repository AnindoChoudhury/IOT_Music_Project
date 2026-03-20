"use client"

export function VideoPlayer({ isReady, videoId } : {isReady: boolean; 
  videoId: string;}) {
  return (
    <div className="relative flex w-full aspect-video flex-col items-center justify-center overflow-hidden rounded-xl border border-border bg-card p-6 shadow-sm">
      
      {/* 🎨 Custom CSS for the smooth flowing wave animation */}
      <style>{`
        @keyframes flowy-wave {
          0%, 100% { height: 15%; opacity: 0.4; }
          50% { height: 100%; opacity: 1; }
        }
        .wave-bar {
          animation: flowy-wave 1.4s ease-in-out infinite;
        }
      `}</style>

      {isReady && videoId ? (
        <>
          {/* 🔊 The Invisible DJ (Hidden YouTube Player) */}
          <iframe
            className="absolute h-1 w-1 opacity-0 pointer-events-none"
            src={`https://www.youtube.com/embed/${videoId}?autoplay=1`}
            allow="autoplay"
            title="Hidden Audio Player"
          />

          {/* UI Status Text */}
          <div className="absolute top-6 flex flex-col items-center">
            <span className="text-xs font-bold uppercase tracking-widest text-primary animate-pulse">
              Audio Sync Active
            </span>
            <span className="text-sm text-muted-foreground mt-1">
              Playing Therapeutic Frequencies
            </span>
          </div>

          {/* The Flowy Waveform Visualizer */}
          <div className="flex h-32 w-full items-center justify-center gap-1.5 mt-8">
            {[...Array(30)].map((_, i) => {
              // Creating a staggered delay so it looks like a real audio wave!
              const staggerDelay = (Math.sin(i * 0.5) * 0.5).toFixed(2);
              return (
                <div
                  key={i}
                  className="w-2 rounded-full bg-primary wave-bar"
                  style={{ animationDelay: `${staggerDelay}s` }}
                />
              );
            })}
          </div>
        </>
      ) : (
        /* Idle State (Before clicking Analyze) */
        <div className="flex flex-col items-center justify-center text-muted-foreground">
          <div className="mb-4 h-1 w-32 rounded-full bg-secondary" />
          <p className="text-sm font-medium">Awaiting biometric synchronization...</p>
        </div>
      )}
    </div>
  );
}