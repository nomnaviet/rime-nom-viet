# rime-nom-viet

RIME input schema for Vietnamese Chữ Nôm (喃字).

Type Vietnamese using **Telex** to input Nôm characters.

## Features

- **130,000+ entries** - One of the most comprehensive Nôm dictionaries
- **74,000 compound words** - Multi-syllable phrases like "việt nam" → 越南
- **Telex input** - Type `nguowfi` to get 𠊛 (người)
- **Marks and tones optional** - `vietnam` → 越南, `quocngu` → 國語, `daihoc` → 大學
- **Vietnamese preview** - Shows "người" instead of "nguowfi" while typing
- **Frequency ranking** - Common characters appear first

## Telex Input Guide

| Type | Get | Example |
|------|-----|---------|
| `aa` | â | `aan` → ân |
| `aw` | ă | `awn` → ăn |
| `ee` | ê | `ees` → ế |
| `oo` | ô | `oof` → ồ |
| `ow` | ơ | `owf` → ờ |
| `uw` | ư | `uws` → ứ |
| `dd` | đ | `ddi` → đi |

**Tones:**

| Key | Tone | Example |
|-----|------|---------|
| `s` | sắc (á) | `as` → á |
| `f` | huyền (à) | `af` → à |
| `r` | hỏi (ả) | `ar` → ả |
| `x` | ngã (ã) | `ax` → ã |
| `j` | nặng (ạ) | `aj` → ạ |

**Leaving marks and tones out:** any of the keys above can be skipped (`dd` can be typed `d`), and the entries they would have narrowed to are still offered. Each mark or tone left out halves a spelling's weight, so typing a syllable in full still puts its own characters first. It works best for phrases (`vietnam` → 越南); a single syllable typed bare (`toi`) lists the characters read exactly that way before those of its toned forms.

## Installation

### macOS (Squirrel 鼠鬚管)

**Step 1: Install Squirrel**
```bash
brew install --cask squirrel
```
Or download from: https://github.com/rime/squirrel/releases

**Step 2: Install nom_viet**

**Option A: One-line installer (recommended)**
```bash
curl -fsSL https://github.com/nomnaviet/rime-nom-viet/raw/main/install.sh | bash
```

**Option B: Manual download**
1. Download these 2 files:
   - [nom_viet.schema.yaml](https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.schema.yaml)
   - [nom_viet.dict.yaml](https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.dict.yaml)
2. Copy both to `~/Library/Rime/`

**Step 3: Add to schema list**

Create/edit `~/Library/Rime/default.custom.yaml`:
```yaml
patch:
  schema_list:
    - schema: nom_viet
    - schema: luna_pinyin
```

**Step 4: Deploy**
- Click Squirrel icon in menu bar → Deploy (重新部署)
- Or run: `/Library/Input\ Methods/Squirrel.app/Contents/MacOS/Squirrel --reload`

**Step 5: Select schema**
- Press `Ctrl+`` or `F4` to switch to "Nôm Việt 喃越"

---

### Windows (Weasel 小狼毫)

**Step 1: Install Weasel**
- Download from: https://github.com/rime/weasel/releases
- Run installer, restart if needed

**Step 2: Install nom_viet**

**Option A: One-click installer (recommended)**
1. Download [install.cmd](https://github.com/nomnaviet/rime-nom-viet/raw/main/install.cmd)
2. Double-click to run

**Option B: Manual download**
1. Download these 2 files:
   - [nom_viet.schema.yaml](https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.schema.yaml)
   - [nom_viet.dict.yaml](https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.dict.yaml)
2. Copy both to `%APPDATA%\Rime\`

> **Tip:** Type `%APPDATA%\Rime` in File Explorer address bar to open the folder.

**Step 3: Add to schema list**

Create/edit `%APPDATA%\Rime\default.custom.yaml`:
```yaml
patch:
  schema_list:
    - schema: nom_viet
    - schema: luna_pinyin
```

**Step 4: Deploy**
- Right-click Weasel icon in system tray → 重新部署 (Deploy)

**Step 5: Select schema**
- Press `Ctrl+`` or `F4` to switch to "Nôm Việt 喃越"

---

### Linux (ibus-rime / fcitx5-rime)

**Step 1: Install ibus-rime or fcitx5-rime**
```bash
# Ubuntu/Debian
sudo apt install ibus-rime
# or
sudo apt install fcitx5-rime

# Arch
sudo pacman -S ibus-rime
# or
sudo pacman -S fcitx5-rime
```

**Step 2: Install nom_viet**

**Option A: One-line installer (recommended)**
```bash
curl -fsSL https://github.com/nomnaviet/rime-nom-viet/raw/main/install.sh | bash
```

**Option B: Manual download**
```bash
# For ibus-rime
cd ~/.config/ibus/rime

# For fcitx5-rime
cd ~/.local/share/fcitx5/rime

# Download files
curl -LO https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.schema.yaml
curl -LO https://github.com/nomnaviet/rime-nom-viet/raw/main/nom_viet.dict.yaml
```

**Step 3: Add to schema list**

Edit `default.custom.yaml` in the same directory:
```yaml
patch:
  schema_list:
    - schema: nom_viet
    - schema: luna_pinyin
```

**Step 4: Deploy**
- ibus: Right-click icon → Deploy
- fcitx5: Right-click icon → Restart

---

### Android (Trime 同文輸入法)

1. Install [Trime](https://github.com/osfans/trime/releases) from GitHub releases
2. Download `nom_viet.schema.yaml` and `nom_viet.dict.yaml`
3. Copy to `/sdcard/rime/` using file manager
4. Open Trime → Settings → Deploy
5. Select "Nôm Việt" in schema list

---

### iOS (iRime)

1. Install [iRime](https://apps.apple.com/app/id1142623977) from App Store
2. Download the schema files
3. Transfer via iCloud Drive or WebDAV (built into iRime)
4. Deploy in app settings
5. Select "Nôm Việt" schema

---

## Usage Examples

| Input | Vietnamese | Output |
|-------|------------|--------|
| `nguowfi` | người | 𠊛 |
| `vieetj nam` | việt nam | 越南 |
| `awn cowm` | ăn cơm | 咹𩚵 |
| `tooi` | tôi | 碎 |
| `vietnam` | việt nam | 越南 |
| `quocngu` | quốc ngữ | 國語 |
| `ddij` | đi | 𨅸 |

## Data Source

Dictionary data from [Nôm Na Việt](https://nomnaviet.com) — a comprehensive Vietnamese Hán-Nôm dictionary platform.

## Maintenance

The dictionary is partly auto-generated from the upstream Nôm Na Việt database. Entries between the markers `# >>> NOM-NA-VIET-AUTO-START` and `# <<< NOM-NA-VIET-AUTO-END` at the end of `nom_viet.dict.yaml` are appended by an automated export; re-runs strip and rewrite only the marked block, so hand-curated lines outside it are preserved across refreshes. To add an entry by hand, place it anywhere outside the auto-block.

Characters use standard Unicode codepoints, not NomNaTong's Private Use Area (U+F0000…), which no system font renders. Where NOM Foundation has published a standard codepoint for a NomNaTong PUA character (mostly Extension H and J), the dictionary uses it; `python3 scripts/pua_to_unicode.py` rewrites any that come back (`--check` only reports). It reads the mapping from a Nôm Na Việt checkout that holds this repo as `tools/rime-nom-viet`, or from `--map <path to nomnatong-pua-map.json>`. Displaying Extension H/J needs a font that covers them, such as NomNaTong 5.15 or later. PUA characters with no published mapping yet are kept as they are.

## License

[MIT](LICENSE)

## Related Projects

- [rime-hannom](https://github.com/tranduythanh/rime-hannom) - Another RIME Hán-Nôm schema
- [rime-vietnamese](https://github.com/gkovacs/rime-vietnamese) - Vietnamese Quốc ngữ + Nôm
- [chunom.org](https://chunom.org) - Chữ Nôm resources
