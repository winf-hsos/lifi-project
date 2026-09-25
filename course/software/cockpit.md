# The Team Cockpit

Online: <https://docs.lifi-project.de/software/cockpit.html>

The team cockpit shows your light link live in the browser: at the top what your LED sends, below it what your sensor measures, both on the same time axis. It is your most important tool for finding faults, because most problems can be seen here at a glance. If the sender band changes correctly but the curves do not move, something is wrong with alignment or distance. If the curves jump in step with the colours but your program still recognises nothing, the fault is in your thresholds or your timing.

## Opening it

Interactive demonstrator: <https://lifi.uber.space/cockpit>

The first time you open it, it asks for your team name. After that the name is part of the address (something like `.../cockpit?team=team-07`), so you can bookmark the page or share the link within your team. "switch team" at the top right changes the team.

The data arrives by itself: as soon as your program uses the module [`lifi_hardware`](lifi-hardware.md), it sends its measurement log to the course server, and the cockpit shows it. You do not have to configure anything.

## The status line

At the top are six values that update continuously: whether data is arriving right now ("live") or when it last did, the current LED colour with a swatch, the latest reading (the four channels r, g, b and c), the readings per second, the gain and integration time you have set, and the last error, in case your program crashed.

## Reading the timeline

The large area is a timeline that reaches from seconds to the whole semester. What it shows depends on the zoom.

Zoomed in close (up to a window of about 15 minutes) you see the raw signal: at the top the sender band, in which every block has exactly the colour the LED showed at that moment, and below it the four sensor channels as curves. The clear channel (c, the light line) is the most sensitive. Dashed vertical marks show where a session started or ended and where settings were changed; red marks are program crashes.

Zoomed far out, the same area becomes an activity overview: blue bars show when and how intensively you worked (the taller and brighter, the more readings), and red strokes above them mark periods with errors. That way you can find the spot where something interesting happened even days later.

Below the area there is always an axis with time and date, and above it the visible period and its length, so you never have to guess where you are.

## Moving and zooming

The controls work the way you know them from video editors or map apps:

- **Scroll wheel** zooms in and out, around the point the mouse is on.
- **Double-click** on a blue activity bar jumps straight into its period; anywhere else it zooms in strongly around the point you clicked.
- **Drag** with the mouse button held down moves the window in time.
- **Hover** shows details: over the sender band the exact RGB values and since when the colour has been on, over the curves the nearest reading with all four values and its timestamp, over marks what they mean.
- The buttons **30 s / 5 min / 1 h / 24 h / all** jump to fixed windows, **+ / −** zoom step by step.

As soon as you zoom or drag into the past, the view stops following. The green button **"● live"** brings you back to the present, where the right edge moves along with the clock again.

## When nothing arrives

If the status says "no data yet" for good, check these in order: Is your program running right now, and does it use `lifi_hardware`? Is the team name in the address correct? Does your laptop have internet? Without a network your program carries on completely normally, by the way; only the cockpit stays empty, and everything that matters is still in your local log file `lifi_log.jsonl`. And if your device has not been assigned to a team yet, tell us; that takes a minute.

## What is still to come

The cockpit grows during the semester: later your practice tests for the challenges will start here, and at the acceptance tests the same view runs large on the projector. We will add how that works to this page when it is ready.
