"use client"
import { useRef, useEffect } from "react";
import { Play, Pause } from "lucide-react";

export function VideoPlayer({ isReady, videoId,isPlaying, 
  setIsPlaying} : {isReady: boolean; videoId: string;isPlaying: boolean;
  setIsPlaying: (val: boolean) => void;}) {
  
  // 1. Create a reference to the iframe to send commands without re-rendering it
  const iframeRef = useRef<HTMLIFrameElement>(null);

  // 2. Effect to send Play/Pause commands via the YouTube JavaScript API
  useEffect(() => {
    if (!iframeRef.current) return;

    const command = isPlaying 
      ? '{"event":"command","func":"playVideo","args":""}'
      : '{"event":"command","func":"pauseVideo","args":""}';

    iframeRef.current.contentWindow?.postMessage(command, "*");
  }, [isPlaying]);

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
        /* 🛑 Pause the animation when isPlaying is false */
        .wave-bar-paused {
          animation-play-state: paused !important;
          opacity: 0.2;
        }
      `}</style>

      {isReady && videoId ? (
        <>
          {/* 🔊 The YouTube Player - Kept 'always on' but controlled via Ref */}
          {/* enablejsapi=1 allows us to control the player remotely */}
          <iframe
            ref={iframeRef}
            className="absolute h-1 w-1 opacity-0 pointer-events-none"
            src={`https://www.youtube.com/embed/${videoId}?autoplay=1&enablejsapi=1`}
            allow="autoplay"
            title="Hidden Audio Player"
          />

          {/* UI Status Text & Controls */}
          <div className="absolute top-6 left-6 right-6 flex justify-between items-start">
            <div className="flex flex-col">
              <span className={`text-xs font-bold uppercase tracking-widest text-primary ${isPlaying ? 'animate-pulse' : ''}`}>
                {isPlaying ? "Audio Sync Active" : "Audio Paused"}
              </span>
              <span className="text-sm text-muted-foreground mt-1">
                {isPlaying ? "Playing Therapeutic Frequencies" : "Sync Standby"}
              </span>
            </div>

            {/* 🔘 THE PLAY/PAUSE BUTTON */}
            <button 
              onClick={() => setIsPlaying(!isPlaying)}
              className="flex h-10 w-10 items-center justify-center rounded-full bg-secondary text-primary hover:bg-primary hover:text-primary-foreground transition-all z-10"
            >
              {isPlaying ? <Pause size={20} fill="currentColor" /> : <Play size={20} fill="currentColor" className="ml-1" />}
            </button>
          </div>

          {/* The Flowy Waveform Visualizer */}
          <div className="flex h-32 w-full items-center justify-center gap-1.5 mt-8">
            {[...Array(30)].map((_, i) => {
              const staggerDelay = (Math.sin(i * 0.5) * 0.5).toFixed(2);
              return (
                <div
                  key={i}
                  className={`w-2 rounded-full bg-primary wave-bar ${!isPlaying ? 'wave-bar-paused' : ''}`}
                  style={{ animationDelay: `${staggerDelay}s` }}
                />
              );
            })}
          </div>
        </>
      ) : (
        /* Idle State */
        <div className="flex flex-col items-center justify-center text-muted-foreground">
          <div className="mb-4 h-1 w-32 rounded-full bg-secondary" />
          <p className="text-sm font-medium">Awaiting biometric synchronization...</p>
        </div>
      )}
    </div>
  );
}