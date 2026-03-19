"use client"

import { cn } from "@/lib/utils"
import type { LucideIcon } from "lucide-react"

interface MetricCardProps {
  title: string
  value: string
  unit?: string
  icon: LucideIcon
  iconColor: string
  glowColor: string
}

export function MetricCard({
  title,
  value,
  unit,
  icon: Icon,
  iconColor,
  glowColor,
}: MetricCardProps) {
  return (
    <div className="group relative overflow-hidden rounded-xl border border-border bg-card p-6 transition-all duration-300 hover:border-primary/50">
      {/* Subtle glow effect on hover */}
      <div
        className={cn(
          "absolute inset-0 opacity-0 blur-2xl transition-opacity duration-500 group-hover:opacity-20",
          glowColor
        )}
      />

      <div className="relative flex items-start justify-between">
        <div className="space-y-3">
          <p className="text-sm font-medium text-muted-foreground">{title}</p>
          <div className="flex items-baseline gap-2">
            <span className="text-4xl font-bold tracking-tight text-foreground">
              {value}
            </span>
            {unit && (
              <span className="text-lg font-medium text-muted-foreground">
                {unit}
              </span>
            )}
          </div>
        </div>

        <div
          className={cn(
            "flex h-14 w-14 items-center justify-center rounded-xl transition-all duration-300",
            "bg-gradient-to-br from-secondary to-muted",
            "group-hover:scale-110"
          )}
        >
          <Icon className={cn("h-7 w-7", iconColor)} strokeWidth={2} />
        </div>
      </div>

      {/* Animated border gradient */}
      <div className="absolute bottom-0 left-0 h-[2px] w-full bg-gradient-to-r from-transparent via-primary/50 to-transparent opacity-0 transition-opacity duration-300 group-hover:opacity-100" />
    </div>
  )
}
