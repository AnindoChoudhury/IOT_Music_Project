"use client"

import { Play, Volume2 } from "lucide-react"

interface VideoPlayerProps {
  isReady: boolean
}

export function VideoPlayer({ isReady }: VideoPlayerProps) {
  return (
    <div className="relative overflow-hidden rounded-xl border border-border bg-card">
      <div className="p-4">
        <div className="flex items-center justify-between">
          <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground">
            Music Player
          </h3>
          <div className="flex items-center gap-2 text-muted-foreground">
            <Volume2 className="h-4 w-4" />
            <span className="text-xs">Ready</span>
          </div>
        </div>
      </div>

      {/* 16:9 aspect ratio container */}
      <div className="relative aspect-video w-full bg-black/50">
        {isReady ? (
          <iframe
            className="absolute inset-0 h-full w-full"
            src="https://www.youtube.com/embed/jfKfPfyJRdk?si=placeholder"
            title="Music Player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        ) : (
          <div className="absolute inset-0 flex flex-col items-center justify-center gap-4">
            <div className="flex h-20 w-20 items-center justify-center rounded-full bg-gradient-to-br from-secondary to-muted">
              <Play className="h-10 w-10 text-muted-foreground" />
            </div>
            <p className="text-sm text-muted-foreground">YouTube Player Ready</p>
            <p className="text-xs text-muted-foreground/60">
              Click {"\"Analyze Mood & Play Music\""} to begin
            </p>
          </div>
        )}

        {/* Scanline overlay effect */}
        <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(transparent_50%,rgba(0,0,0,0.1)_50%)] bg-[length:100%_4px]" />
      </div>
    </div>
  )
}
