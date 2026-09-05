# API setup

The bundled client uses two Zotero interfaces:

| Interface | Purpose | Requirement |
|---|---|---|
| Local API at `http://localhost:23119/api` | Read operations | Zotero Desktop running with local API access |
| Web API at `https://api.zotero.org` | Reads and all writes | Library ID and a least-privilege API key |

If the local API is unavailable, reads can fall back to the Web API only when credentials are present. Writes always use the Web API.

## Credentials

Create a least-privilege key at [Zotero API Keys](https://www.zotero.org/settings/keys). Enable write permission only for workflows that need it.

Set credentials in the process environment. Do not save them in this skill directory or a project:

```powershell
$env:ZOTERO_API_KEY = "<session-only key>"
$env:ZOTERO_LIBRARY_ID = "<library id>"
$env:ZOTERO_LIBRARY_TYPE = "user"
```

On POSIX shells use the corresponding `export` commands. Avoid printing or persisting these values in shell history, logs, notes, or version control. The client reads credentials only from these environment variables.

`config.example.json` contains optional non-secret collection-name mappings. Copy it to `config.json` only if those aliases are useful; never add credentials to it.

## Shared client

Resolve the installed skill directory at runtime instead of hard-coding a user's home path:

```python
import sys
from pathlib import Path

skill_dir = Path(r"<installed-skill-directory>")
sys.path.insert(0, str(skill_dir / "scripts"))

from zotero_client import ZoteroDualClient, get_client

web = get_client()
dual = ZoteroDualClient()
results = dual.search("flood adaptation")
```

Useful entries include `get_client()`, `get_collection(name)`, `check_local_api()`, `ZoteroDualClient`, and `safe_api_call()`.

Before a real write, confirm the target keys and scope. After a write, read the object back through the Web API so its version and content are authoritative.
