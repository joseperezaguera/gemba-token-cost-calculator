# Contract testing

## Contracts to maintain

Maintain an inventory of public APIs, events and adapter ports with owner, consumers,
version, compatibility policy and executable checks. Define field names/types, required
versus optional, missing versus null, errors and relevant behavioral guarantees.
A schema can validate structure; it does not establish the meaning of a successful
response, authorized access, transaction semantics or compatibility with every consumer.

Use three complementary levels:
- Adapter contracts: exercise fakes and real implementations against the same required
  behavior, including failures, empty data and persistence semantics. Apply Liskov.
- API/event schema and behavior checks: verify actual serialization and independently
  specified scenarios; detect breaking changes against supported previous contracts.
- Consumer/provider verification: consumers express the interactions they depend on;
  providers verify those expectations against real handlers with controlled provider state.

A frontend type declaration is not runtime response validation. Audit or generate the
actual consumed shape: names after conversion, types, optionality and nullability.
Identify the domain owner by tracing endpoint -> use case -> state owner; do not infer
ownership from a DTO name or URL prefix. Preserve legitimate projections as projections.

## Verification and lifecycle

Keep expectations independent of production implementation. A generated schema and a
mock generated from that same schema alone can agree while the deployed handler disagrees.
Test real provider code and serialize real responses. Use strict mock specifications so
changed signatures or unsupported operations fail, and explicit values over wildcards.

Cover success, relevant errors and denied access where applicable. For events, verify
producer payload and consumer handling; test duplicates/order separately when those are
behavioral guarantees. Broker connectivity and delivery semantics need integration tests.
Contract tests complement those tests and important E2E journeys.

Version contracts, consumer/provider builds and verification results with immutable
revision identities. Check changes against currently supported consumers, including old
mobile releases where relevant. Before independently deploying a component, require known
successful compatibility evidence for the versions it will meet; missing evidence is not
success. Record actual deployment versions after successful deployment.

A project can adopt Pact and its version matrix/can-i-deploy mechanism, or a simpler
versioned contract fixture verified by both sides. The guide does not require a broker
or paid service. Record which compatibility guarantees the chosen adapter provides.

Use contract-template.md in the existing canonical contract directory. Preserve schema
and behavioral tests when retiring versions; remove only after supported consumers have
migrated. Test a deliberately incompatible fixture/provider to demonstrate sensitivity.

## Evidence

Record contract and consumer/provider revisions, command, tested implementation,
provider state, result and compatibility scope. Declare unverified third-party behavior.
The personal contract-service example demonstrates real HTTP verification against an
independent fixture; it does not implement a cross-repository version broker.
