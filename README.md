# Welcome to the Pancakes vs Waffles Bot (pvswbot)!
Pancakes vs Waffles is a project that collects information on emoji usage from the Tidbyt Discord guild for display on a Tidbyt. The project is made up of a Discord bot that sends message information, a backend that stores and fetches emoji data via http requests, and a Tidbyt app that gets and displays emoji data.

This bot is the intermediary between the Tidbyt Discord guild and the pvswbot backend. It fetches messages at a given interval and sends them to the backend for insertion.
