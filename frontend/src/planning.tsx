import { useEffect, useState } from 'react'

interface Event {
  id: number
  title: string
  start_utc: string
  end_utc: string
}

export default function PlanningView() {
  const [events, setEvents] = useState<Event[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const from = '2025-01-01T00:00:00Z'
    const to = '2025-02-01T00:00:00Z'
    fetch(`/v1/planning/events?from=${from}&to=${to}`)
      .then(r => r.json())
      .then(data => {
        setEvents(data)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Loading...</div>
  if (events.length === 0) return <div>No events</div>

  const groups: Record<string, Event[]> = {}
  events.forEach(e => {
    const day = e.start_utc.split('T')[0]
    groups[day] = groups[day] || []
    groups[day].push(e)
  })

  return (
    <div>
      {Object.keys(groups).sort().map(day => (
        <div key={day} className="mb-4">
          <h2 className="font-bold">{day}</h2>
          <ul>
            {groups[day].map(ev => (
              <li key={ev.id}>{ev.title} ({ev.start_utc.slice(11,16)})</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}
