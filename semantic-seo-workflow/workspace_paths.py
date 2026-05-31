from __future__ import annotations

import json
import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = REPO_ROOT / "workspace.config.json"
DEFAULT_CLIENT_DATA_DIRNAME = "client_data"


def _load_workspace_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}

    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def get_client_data_root() -> Path:
    env_value = os.getenv("CLIENT_DATA_ROOT")
    if env_value:
        return Path(env_value).expanduser().resolve()

    config = _load_workspace_config()
    config_value = config.get("client_data_root")
    if config_value:
        return Path(config_value).expanduser().resolve()

    return (REPO_ROOT / DEFAULT_CLIENT_DATA_DIRNAME).resolve()


def get_client_path(client_name: str) -> Path:
    return get_client_data_root() / client_name
