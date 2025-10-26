#!/usr/bin/env bash
set -euo pipefail 


#the above is a common “strict mode” for bash scripts:

    #-e: exit immediately if any command returns a non‑zero status.
    #-u: treat unset variables as an error (exit).
    #-o pipefail: in a pipeline, return the exit code of the first failing command (not just the last).

#Together, they make scripts fail fast and avoid silent errors.



python3 src/main.py