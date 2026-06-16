import csv, json, re

rows = []
with open("GuestList.csv", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for r in reader:
        if not r or len(r) < 2:
            continue
        name = " ".join(r[0].split()).strip()
        table_raw = " ".join(r[1].split()).strip()
        if not name or not table_raw:
            continue
        # skip the per-table capacity/summary rows (the name cell is just a number)
        if re.fullmatch(r"\d+", name):
            continue
        # tidy the table label: drop the trailing planning note in parentheses
        table = re.sub(r"\s*\(.*\)\s*$", "", table_raw).strip()
        rows.append((name, table))

# stable alphabetical order by name (case-insensitive); table order as tiebreak
rows.sort(key=lambda x: (x[0].lower(), x[1]))

lines = []
for name, table in rows:
    lines.append("    { name: %s, table: %s }," % (json.dumps(name, ensure_ascii=False),
                                                   json.dumps(table, ensure_ascii=False)))
guests_block = "\n".join(lines)

content = '''/* =============================================================
   ✦  EDIT YOUR WEDDING DETAILS & GUEST LIST HERE  ✦
   -------------------------------------------------------------
   This is the ONLY file you need to change.
   No coding required — just edit the text between the quotes.

   1. Set the couple name, date, and a short welcome line.
   2. Add one line per guest or group inside the guests [ ... ] list:
          { name: "First Last", table: "Table 7" },
      - "name"  : how the guest will search for themselves
      - "table" : whatever you want shown (e.g. "Table 7", "Family Table")
   3. Keep each line ending with a comma.
   4. Save the file and refresh the page. That's it!

   (The guest list below was imported from GuestList.csv.)
   ============================================================= */

window.WEDDING = {
  // --- Event details (shown at the top of the page) ---
  couple: "Arjun & Priyanjli\\nSharma",
  date: "Friday, the 26th of June 2026",
  welcome: "Welcome! Find your name below to discover your table.",

  // --- Guest list (order does not matter — it sorts automatically) ---
  guests: [
%s
  ],
};
''' % guests_block

with open("guests.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Imported %d entries across %d tables." % (len(rows), len({t for _, t in rows})))
