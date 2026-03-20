"use client"

import { Zap, Music } from "lucide-react"

interface EmotionResultCardProps {
  emotion: string
  isActive: boolean
}

export function EmotionResultCard({ emotion, isActive }: EmotionResultCardProps) {
  return (
    <div className="relative overflow-hidden rounded-xl border border-border bg-card p-6">
      {/* Background glow effect when active */}
      {isActive && (
        <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-transparent to-accent/10 animate-pulse" />
      )}

      <div className="relative space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Music className="h-5 w-5 text-primary" />
            <h3 className="text-sm font-semibold uppercase tracking-wider text-muted-foreground">
              Analysis Result
            </h3>
          </div>
          {isActive && (
            <span className="flex items-center gap-1.5 rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
              <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-primary" />
              Live
            </span>
          )}
        </div>

        <div className="flex items-center gap-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-500/20">
            <Zap className="h-6 w-6 text-amber-400" />
          </div>
          <div>
            <p className="text-xs text-muted-foreground">Detected Emotion</p>
            <p className="text-xl font-bold text-foreground">{emotion}</p>
          </div>
        </div>
      </div>
    </div>
  )
}
