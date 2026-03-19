"use client"

import { useState } from "react"
import { Heart, Activity } from "lucide-react"
import { DashboardHeader } from "@/components/dashboard-header"
import { MetricCard } from "@/components/metric-card"
import { AnalyzeButton } from "@/components/analyze-button"
import { EmotionResultCard } from "@/components/emotion-result-card"
import { VideoPlayer } from "@/components/video-player"

export default function Dashboard() {
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [isAnalyzed, setIsAnalyzed] = useState(false)

  const handleAnalyze = () => {
    setIsAnalyzing(true)
    // Simulate analysis
    setTimeout(() => {
      setIsAnalyzing(false)
      setIsAnalyzed(true)
    }, 2000)
  }

  return (
    <div className="min-h-screen bg-background">
      <DashboardHeader />

      <main className="mx-auto max-w-7xl px-6 py-8">
        {/* Page Title */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-foreground">Sensor Dashboard</h2>
          <p className="mt-1 text-muted-foreground">
            Real-time biometric data analysis and mood-based music recommendations
          </p>
        </div>

        {/* Two Column Grid */}
        <div className="grid gap-8 lg:grid-cols-2">
          {/* Left Column - Sensor Data & Action */}
          <div className="space-y-6">
            <div className="grid gap-4 sm:grid-cols-2">
              {/*Humidity*/}
              <MetricCard
                title="Humidity"
                value="1000"
                icon={Activity}
                iconColor="text-yellow-400"
                glowColor="bg-yellow-500"
              />
              {/*Temperature*/}
              <MetricCard
                title="Temperature"
                value="21"
                icon={Activity}
                iconColor="text-purple-400"
                glowColor="bg-purple-500"
              />

              {/* Heart Rate Card */}
              <MetricCard
                title="Heart Rate"
                value="85"
                unit="BPM"
                icon={Heart}
                iconColor="text-rose-400"
                glowColor="bg-rose-500"
              />

              {/* Skin Conductivity Card */}
              <MetricCard
                title="Skin Conductivity (GSR)"
                value="2100"
                icon={Activity}
                iconColor="text-cyan-400"
                glowColor="bg-cyan-500"
              />
            </div>

            {/* Sensor Status */}
            <div className="rounded-xl border border-border bg-card p-4">
              <div className="flex items-center justify-between">
                <span className="text-sm text-muted-foreground">Last Updated</span>
                <span className="text-sm font-medium text-foreground">Just now</span>
              </div>
              <div className="mt-3 h-1.5 w-full overflow-hidden rounded-full bg-secondary">
                <div className="h-full w-3/4 rounded-full bg-gradient-to-r from-primary to-accent animate-pulse" />
              </div>
            </div>

            {/* Analyze Button */}
            <AnalyzeButton onClick={handleAnalyze} isLoading={isAnalyzing} />

            {/* Quick Stats */}
            <div className="grid grid-cols-3 gap-4">
              <div className="rounded-xl border border-border bg-card p-4 text-center">
                <p className="text-2xl font-bold text-foreground">24</p>
                <p className="text-xs text-muted-foreground">Sessions Today</p>
              </div>
              <div className="rounded-xl border border-border bg-card p-4 text-center">
                <p className="text-2xl font-bold text-foreground">98%</p>
                <p className="text-xs text-muted-foreground">Accuracy</p>
              </div>
              <div className="rounded-xl border border-border bg-card p-4 text-center">
                <p className="text-2xl font-bold text-foreground">142</p>
                <p className="text-xs text-muted-foreground">Songs Played</p>
              </div>
            </div>
          </div>

          {/* Right Column - Results & Media */}
          <div className="space-y-6">
            {/* Emotion Result */}
            <EmotionResultCard
              emotion="Workout / High Energy"
              isActive={isAnalyzed}
            />

            {/* Video Player */}
            <VideoPlayer isReady={isAnalyzed} />

            {/* Recommendations */}
            
            {/* <div className="rounded-xl border border-border bg-card p-4">
              <h4 className="mb-3 text-sm font-semibold uppercase tracking-wider text-muted-foreground">
                Recommended Playlist
              </h4>
              <div className="space-y-2">
                {[
                  { title: "High Energy Workout", tracks: 48 },
                  { title: "Power Running", tracks: 32 },
                  { title: "Gym Beast Mode", tracks: 56 },
                ].map((playlist, index) => (
                  <div
                    key={index}
                    className="flex items-center justify-between rounded-lg bg-secondary/50 px-4 py-3 transition-colors hover:bg-secondary"
                  >
                    <span className="text-sm font-medium text-foreground">
                      {playlist.title}
                    </span>
                    <span className="text-xs text-muted-foreground">
                      {playlist.tracks} tracks
                    </span>
                  </div>
                ))}
              </div>
            </div> */}
          </div>
        </div>
      </main>
    </div>
  )
}
