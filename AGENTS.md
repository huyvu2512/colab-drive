# COLAB DRIVE - DEVELOPMENT & RELEASE WORKFLOW (WORKFLOW RULES)

## 1. MANDATORY: PROACTIVELY BUMP VERSION ON ANY FEATURE / UI / BUG FIX
- Whenever making changes to features, UI parameters, or fixing bugs: **ALWAYS PROACTIVELY BUMP VERSION** (e.g., `2.2.1` -> `2.2.2`).
- Never make the user ask or remind to bump versions.
- Strict Semantic Versioning standard (`MAJOR.MINOR.PATCH`):
  - **PATCH (`x.y.Z`)**: Bug fixes, parameter adjustments, UI label tweaks, minor performance optimizations.
  - **MINOR (`x.Y.0`)**: New feature implementations, new engine/protocol support, new queue mechanisms, non-breaking major enhancements.
  - **MAJOR (`X.0.0`)**: Complete architectural redesigns or breaking changes to notebook structure.
  - Do not jump minor or major versions arbitrarily for minor prompt edits. Maintain stable, disciplined incremental versioning.
- Files that MUST be synchronized simultaneously upon every version bump:
  1. `src/core/constants.py` -> `APP_VERSION = "x.y.z"`
  2. `scripts/build.py` -> Run to rebuild `colab-drive.ipynb` with updated version metadata.
  3. `colab-drive.ipynb` -> Recompiled with current version and form parameters.
  4. `README.md` & `README_EN.md` -> Update version badges and latest release summary.
  5. `CHANGELOG.md` -> Add `## vx.y.z - DD/MM/YYYY HH:MM` and record all changes.
- Before each push, review and update `README.md`, `README_EN.md`, and `CHANGELOG.md` to ensure documentation matches the changes being committed.
- Keep `CHANGELOG.md` entries concise: each bullet point should be a short sentence stating the feature or fix (around 6-15 words), clear and punchy without overly long implementation details.
- **ABSOLUTE RULE: ZERO EMOJIS OR ICONS ANYWHERE**:
  - 0 emojis or graphical icons in markdown files (`README.md`, `README_EN.md`, `CHANGELOG.md`, `AGENTS.md`).
  - 0 emojis or graphical icons in source code, comments, console logs, commit messages, and assistant responses.

## 2. STANDARD BUILD & DEPLOYMENT WORKFLOW
1. Run packaging script to compile notebook: `python scripts/build.py`
2. Validate Python syntax across modules: `python -m py_compile scripts/build.py src/core/*.py src/engines/*.py src/notifications/*.py src/queue/*.py src/storage/*.py`
3. Review `README.md`, `README_EN.md`, and `CHANGELOG.md`; keep documentation synchronized and verified for zero emojis.
4. Commit and push to GitHub `main` branch:
   `git add .; git commit -m "..."; git push origin main`
5. Always provide the user with the direct clickable Google Colab URL containing the exact commit hash:
   `https://colab.research.google.com/github/huyvu2512/colab-drive/blob/<commit_hash>/colab-drive.ipynb`

## 3. DESIGN, PERFORMANCE & OPERATIONAL PRINCIPLES
- **Minimalist & Pragmatic**: Clean enterprise-grade layout. No decorative fluff, no unnecessary titles, and no emojis.
- **Colab Form Precision**: Form parameter variable names must remain unaccented uppercase (e.g., `LINK_CAN_TAI`, `CHAT_LUONG_TAI`, `GIOI_HAN_PLAYLIST`), and all dropdown choices must map 100% to backend processing logic.
- **Analysis vs Execution Discipline**: When the user asks to analyze only ("tu tu hay code", "chi phan tich thoi"): analyze and explain thoroughly, NEVER modify code before explicit user confirmation.
