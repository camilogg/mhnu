#!/usr/bin/env bash

# shellcheck disable=SC2128
DUMP=$(dirname "${BASH_SOURCE}")/dumps/mhnu.dump

echo "$DUMP"
if [[ -f "$DUMP" ]]; then
    echo "Starting database restore"
    pg_restore --verbose --clean --no-acl --no-owner -U "$POSTGRES_USER" -d "$POSTGRES_DB" "$DUMP"
    echo "Database restore completed"
else
    echo "No dump file found. Skipping database restore."
fi