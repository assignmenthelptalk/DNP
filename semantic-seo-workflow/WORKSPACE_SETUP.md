# Workspace Setup

This repository supports two client-data layouts:

## 1. Backward-compatible local layout

```text
semantic-seo-workflow/
  client_data/
    [client-name]/
```

If no configuration is provided, the workflows and helper scripts fall back to this layout.

## 2. Recommended external client-data layout

```text
agentic-workflow/
  semantic-seo-workflow/
  client-data/
    tupate.studio/
    ot-assignment-help/
    ciiassignmenthelp/
```

Use this when you want to keep client projects separate from the reusable workflow repository.

## VS Code Workspace

Open the shared VS Code workspace file at:

```text
C:\Users\jobmu\agentic-workflow\semantic-seo.code-workspace
```

This workspace should include:

```text
agentic-workflow/
  semantic-seo-workflow/
  client-data/
    tupate.studio/
    ot-assignment-help/
    ciiassignmenthelp/
```

This keeps the workflow repo reusable across projects while keeping client data outside the workflow repo.

## Configuration

Set the client data root in one of these ways:

### Option A: Environment variable

```powershell
$env:CLIENT_DATA_ROOT = 'C:\Users\jobmu\agentic-workflow\client-data'
```

### Option B: Local workspace config

Copy [workspace.config.example.json](/C:/Users/jobmu/agentic-workflow/semantic-seo-workflow/workspace.config.example.json) to `workspace.config.json` and set:

```json
{
  "client_data_root": "C:\\Users\\jobmu\\agentic-workflow\\client-data"
}
```

The environment variable takes priority over `workspace.config.json`.
If both are missing, the workflow still falls back to local `client_data/` inside the repo for backward compatibility.

## Path convention

All workflow instructions should now be interpreted as:

```text
[CLIENT_DATA_ROOT]/[client_name]/...
```

Examples:

- `[CLIENT_DATA_ROOT]/tupate.studio/business_profile.json`
- `[CLIENT_DATA_ROOT]/tupate.studio/page-briefs/`
- `[CLIENT_DATA_ROOT]/ot-assignment-help/pages/`

## Migration

1. Move each client folder from `semantic-seo-workflow/client_data/` into your external client-data folder.
2. Set `CLIENT_DATA_ROOT` or create `workspace.config.json`.
3. Run the workflow as normal.
4. If a legacy helper script or old JSON artifact still references `client_data/...`, update it to the new root or regenerate it.

## How to Open in VS Code

1. In VS Code, choose `File` -> `Open Workspace from File...`
2. Open `C:\Users\jobmu\agentic-workflow\semantic-seo.code-workspace`
3. Work from the two-folder workspace:
   - `semantic-seo-workflow`
   - `client-data`

With this setup, PageGPT, WriterGPT, LinkingGPT, and audit flows resolve client paths from `workspace.config.json` or `CLIENT_DATA_ROOT`. If neither is set, they still fall back to local `client_data/`.
