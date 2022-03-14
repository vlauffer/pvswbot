# Welcome to the Pancakes vs Waffles Bot (pvswbot)!
Pancakes vs Waffles is a project that collects information on emoji usage from the Tidbyt Discord guild for display on a Tidbyt. The project is made up of a Discord bot that sends message information, a backend that stores and fetches emoji data via http requests, and a Tidbyt app that gets and displays emoji data.

This bot is the intermediary between the Tidbyt Discord guild and the pvswbot backend. It fetches messages at a given interval and sends them to the backend for insertion.

## What am I currently working on?
- Adding time of message data to the message information object
- Adding event handling for emoji reactions. Either going to add reactions in bulk within a given timeframe (which would require a general sense of how long it takes for a message to stop receiving reactions) or send reactions to the backend the instant they occur
- Handling message edits/deletions
- Handling reaction removals