#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

env_file=".env/env.yaml"
SCRIPT_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
PROJECT=$(yq -r .gcloud_project_name < "$env_file")
gcloud config set project "$PROJECT"
"$SCRIPT_DIR/setup-scripts/update_triggers.sh"
"$SCRIPT_DIR/setup-scripts/copy_config.sh"
