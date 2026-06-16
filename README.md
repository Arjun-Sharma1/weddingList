# 💍 Find Your Seat — Wedding Table Finder

A fast, mobile-friendly page for wedding guests. Scan a QR code → type your name →
instantly see your table. Guests can also browse the full list, sorted alphabetically.

No backend, no database, no monthly cost — it's a single static page.

---

## 📁 What's in here

| File         | What it's for                                              |
|--------------|------------------------------------------------------------|
| `index.html` | The app itself. **You don't need to edit this.**           |
| `guests.js`  | **Edit this** — your names, tables, and event details.     |
| `README.md`  | This guide.                                                |

---

## ✏️ Editing your guest list

Open **`guests.js`** in any text editor (Notepad works fine) and:

1. Change the couple name, date, and welcome line at the top.
2. Add one line per guest:
   ```js
   { name: "First Last", table: "7" },
   ```
   - `table` can be a number (`"7"`) **or** a name (`"Rosewood"`, `"Head Table"`).
   - Order doesn't matter — the list sorts itself alphabetically (by last name).
3. Save, then refresh the page.

> Tip: keep the comma at the end of each guest line.

---

## 👀 Previewing it locally

Just **double-click `index.html`** — it opens in your browser. Resize the window
narrow (or use your browser's phone/device view) to see the mobile layout.

---

## 🚀 Publishing it online (so the QR code works)

Pick any **free** static host. Two easy options:

**Vercel** (recommended)
1. Install once: `npm i -g vercel`
2. In this folder, run: `vercel` (follow the prompts) — then `vercel --prod`.
3. You'll get a link like `https://your-wedding.vercel.app`.

**Netlify Drop** (no install)
1. Go to <https://app.netlify.com/drop>
2. Drag this whole folder onto the page. Done — you get a public link.

---

## 🔳 Making the QR code

1. Copy your published link (e.g. `https://your-wedding.vercel.app`).
2. Paste it into any free QR generator, such as <https://qr.io> or
   <https://www.qr-code-generator.com>.
3. Download the QR image, drop it onto your table cards / signage, and you're set.

> Test the QR with your own phone before the big day!

---

## 🎨 Want to change the colours or fonts?

Open `index.html` and look at the `:root { … }` block near the top of the
`<style>` section — every colour is a clearly-named variable you can tweak.

Made with ❤️ for your celebration.
