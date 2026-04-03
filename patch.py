#!/usr/bin/env python3
"""
patch.py — Run this script in the same folder as index.html to apply all updates.
Usage: python3 patch.py
"""
import sys, re

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"Loaded index.html ({len(html)} chars)")
except FileNotFoundError:
    print("ERROR: index.html not found. Run this script in the same folder.")
    sys.exit(1)

# ══ PATCH 1: Insert CVSS topic before <!-- ZERO TRUST --> ══
CVSS_TOPIC = open('_cvss-patch.html','r').read()

# Find the Zero Trust comment marker and insert before it
if '<!-- ZERO TRUST -->' in html:
    html = html.replace('          <!-- ZERO TRUST -->', CVSS_TOPIC + '\n          <!-- ZERO TRUST -->', 1)
    print("✓ Patch 1 applied: CVSS calculator inserted before Zero Trust")
else:
    print("✗ WARN: Could not find '<!-- ZERO TRUST -->' anchor")

# ══ PATCH 2: Replace Diamond Model section ══
DIAMOND_TOPIC = open('_diamond-patch.html','r').read()

# Find the diamond model block start and end
diamond_start = html.find('          <!-- DIAMOND MODEL -->')
if diamond_start == -1:
    print("✗ WARN: Could not find Diamond Model section")
else:
    # Find the end (next <!-- ... --> comment at same indent level, or next topic div ending)
    # We'll find the next topic div start after the diamond
    search_from = diamond_start + 50
    next_topic = html.find('\n          <!-- THREAT INTEL CYCLE -->', search_from)
    if next_topic == -1:
        next_topic = html.find('\n          <!-- THREAT INTEL', search_from)
    if next_topic != -1:
        old_diamond = html[diamond_start:next_topic]
        html = html[:diamond_start] + DIAMOND_TOPIC + html[next_topic:]
        print(f"✓ Patch 2 applied: Diamond Model replaced ({len(old_diamond)} → {len(DIAMOND_TOPIC)} chars)")
    else:
        print("✗ WARN: Could not find end of Diamond Model section")

# ══ Write output ══
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\n✓ index.html updated successfully!")
print("  → Also replace style.css and script.js with the provided updated versions.")
