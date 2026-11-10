#!/usr/bin/env bash
# Original SDS hook. Nonblocking: it neither captures a transcript nor writes knowledge.
set -eu
printf '%s\n' '{"systemMessage":"If this investigation produced durable evidence, use team-brain:brain-learn to prepare a local reviewed draft. Keep customer evidence in that customer restricted checkout; do not publish or promote hypotheses automatically."}'
