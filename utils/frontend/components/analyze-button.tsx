"use client"

import { cn } from "@/lib/utils"
import { Sparkles, Loader2 } from "lucide-react"

interface AnalyzeButtonProps {
  onClick: () => void
  isLoading: boolean
}

export function AnalyzeButton({ onClick, isLoading }: AnalyzeButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={isLoading}
      className={cn(
        "group relative w-full overflow-hidden rounded-xl px-8 py-5",
        "bg-gradient-to-r from-primary via-primary to-accent",
        "text-lg font-semibold text-primary-foreground",
        "transition-all duration-300",
        "hover:shadow-[0_0_40px_rgba(74,222,128,0.4)]",
        "active:scale-[0.98]",
        "disabled:cursor-not-allowed disabled:opacity-70"
      )}
    >
      {/* Animated shine effect */}
      <div className="absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/20 to-transparent transition-transform duration-700 group-hover:translate-x-full" />

      {/* Glow ring */}
      <div className="absolute inset-0 rounded-xl ring-2 ring-primary/50 ring-offset-2 ring-offset-background opacity-0 transition-opacity duration-300 group-hover:opacity-100" />

      <span className="relative flex items-center justify-center gap-3">
        {isLoading ? (
          <>
            <Loader2 className="h-6 w-6 animate-spin" />
            Analyzing...
          </>
        ) : (
          <>
            <Sparkles className="h-6 w-6 transition-transform duration-300 group-hover:rotate-12 group-hover:scale-110" />
            Analyze Mood & Play Music
          </>
        )}
      </span>

      {/* Pulsing glow when not loading */}
      {!isLoading && (
        <div className="absolute inset-0 animate-pulse rounded-xl bg-gradient-to-r from-primary/20 via-transparent to-accent/20" />
      )}
    </button>
  )
}
