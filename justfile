list:
    #!/usr/bin/env bash
    set -euo pipefail
    cd "{{justfile_directory()}}"
    python3 utils/list.py
