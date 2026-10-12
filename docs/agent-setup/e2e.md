# End-to-end journeys and shared environments

Describe critical user journeys independently of the automation tool. Record acceptance,
platforms, fixtures, environment and observability. Separate backend/data preparation
from web/mobile interactions while preserving one coherent scenario and result.
Contract checks reduce interface risk; they do not replace important user journeys.

Use controlled test environments. Confirm deployed revision, endpoint and configuration
before changing state. Diagnostic/preparation tools must refuse an unknown or production
environment unless an explicitly authorized production procedure is intended.
Never infer a safe target from a missing environment variable.

Prefer per-run accounts, data, ports and isolated schemas. If a run must modify shared
flags/configuration, record prior values and restore them in a finally/cleanup path even
when assertions fail. Serialize or lease a single writer for shared backend state;
parallel frontend runners must not independently toggle the same flags. Restoration
must not overwrite changes from another legitimate owner; define ownership and compare
expected state before restoring. Report cleanup failures as unresolved evidence.

Make readiness and interaction waits condition-based and bounded. Record failures,
screenshots/traces where useful and stable identifiers rather than brittle selectors.
State what browser/device/version and release was actually tested. Rerunning a flaky
journey until green is not a fix. Keep cleanup scoped to resources owned by the run.

A small number of critical journeys complements focused tests; do not build an E2E suite
for every private function. Projects without UI can use end-to-end CLI/API workflows.
Link each scenario to an executable test or explicit manual procedure and report gaps.
