# ComfyUI Progress Bar Fork – Setup & Maintenance Guide

> **Purpose:** Document every step taken to move our custom ComfyUI real-time progress bar integration into a safe fork that stays in sync with upstream Open WebUI.

---

## 0. Context

We added a small but critical feature: real-time ComfyUI progress inside Open WebUI.  Four core files were touched, plus tests.  To keep continuous upstream updates *without losing our patch*, we forked the project and installed a nightly rebase + test workflow.

---

## 1. Repository Layout after Migration

```
root/
├─ .github/workflows/upstream-sync.yml   # nightly rebase, build, test, push
├─ open-webui/                           # upstream source + our patches
│  ├─ backend/open_webui/routers/images.py        # + /comfyui/progress + /queue
│  ├─ backend/open_webui/utils/images/comfyui.py  # (untouched – reference)
│  ├─ src/lib/apis/images/index.ts                # + TS helpers
│  ├─ src/lib/components/chat/Messages/ResponseMessage.svelte # mounts bar
│  └─ src/lib/components/chat/ComfyUIProgressBar.svelte       # new component
├─ test_progress_bar_integration.py      # async integration test
└─ docs/PROGRESS_BAR_FORK_SETUP.md       # **THIS FILE**
```

---

## 2. Fork & Patch Procedure

```bash
# 1. Fork on GitHub (web UI) → <your-org>/open-webui

# 2. Locally add remotes and push patches
git remote add origin git@github.com:<your-org>/open-webui.git
git remote add upstream https://github.com/open-webui/open-webui.git

git fetch upstream
# Create feature branch for auditability
git checkout -b feat/comfyui-progress-bar
# Stage only the changed files
git add \
  backend/open_webui/routers/images.py \
  src/lib/apis/images/index.ts \
  src/lib/components/chat/Messages/ResponseMessage.svelte \
  src/lib/components/chat/ComfyUIProgressBar.svelte \
  ../../test_progress_bar_integration.py

git commit -m "feat: ComfyUI real-time progress bar integration"

git push -u origin feat/comfyui-progress-bar
# Merge PR → main on fork.
```

---

## 3. Continuous Upstream Sync

`.github/workflows/upstream-sync.yml` runs nightly:

1. **Checkout** repo with full history.
2. **Rebase** `main` on `upstream/main`.
3. **Build** custom Docker image: `docker build -t ghcr.io/<repo>:test open-webui`.
4. **Run** the container on port 3000.
5. **Execute** `pytest test_progress_bar_integration.py`.
6. **Publish** image as `ghcr.io/<repo>:nightly` if tests pass.

> Any rebase conflict triggers a GitHub warning and stops the push.  Manual resolution required.

---

## 4. Deploying the Custom Image

Production `docker-compose.yaml` should pin to our registry tag:

```yaml
services:
  webui:
    image: ghcr.io/<your-org>/open-webui:nightly   # or :prod once approved
    ports:
      - "3000:8080"
    volumes:
      - open-webui:/app/backend/data
      - ./plugins:/app/plugins                    # extension-only workflow
```

Upgrade path:
1. Watchtower (or CI) pulls `:nightly` automatically.
2. If staging looks good, retag `:nightly` → `:prod` and update production stack.

---

## 5. Extension-Only Guidelines

* **Backend plugins** → `/app/plugins/<name>/__init__.py` (Pipelines framework)
* **Frontend plugins** → `src/lib/plugins/<name>` export Svelte components and register via settings.
* Never modify core files beyond the four audited ones; if you must, open a new branch and document.

---

## 6. Future Patch Checklist

1. Add/modify code **only** inside plugin folders when possible.
2. If core edit is unavoidable:
   * Create branch `feat/<desc>`
   * Update tests.
   * PR → review.
3. Verify nightly workflow remains green.

---

## 7. Troubleshooting & FAQs

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Workflow fails at **rebase** | Upstream changed same lines we patched | Run `git rebase --abort`, patch conflict manually, update tests, push PR |
| Tests fail after build | Upstream API changed | Adjust TS helpers / Svelte bar, bump tests |
| Container boots but progress bar stale | `/comfyui/*` endpoints returning 404 | Ensure backend image contains patched router; rebuild if necessary |

---

## 8. Change-log

| Date | Author | Change |
|------|--------|--------|
| 2025-06-13 | LLM assistant | Initial fork documentation |

---

Happy hacking 🎉 