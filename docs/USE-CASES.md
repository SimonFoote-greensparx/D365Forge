# Use cases

Situations that cross departments, worked end to end. Most CRM projects go wrong at the hand-offs between modules and
disciplines, so these double as acceptance tests for the library: Robert Peledie runs each one before a department moves
from `draft` to `reviewed`.

Each case lists what engages, in what order, the reviewer gate, and what the library cannot decide for you.

## 1. A marketing-qualified lead reaches a seller with its history

**Situation.** Marketing runs journeys in Customer Insights - Journeys. Sales complains that leads arrive with no context
and that hot leads wait days.

**What engages.**
1. `marketing:lead-scoring-and-sales-handoff` defines the score threshold, the hand-off trigger and what context travels.
2. `sales:lead-to-opportunity` defines qualification and conversion so the hand-off lands in a process sellers follow.
3. `solution-architecture:cross-module-data-model` checks that lead, contact and account records are not duplicated across modules.

**Reviewer gate.** `security-compliance:marketing-consent-compliance` confirms that consent and preferences travel with the
lead and that sales follow-up respects them. Blocking if a seller could contact someone who has opted out.

**What the library cannot decide.** Your score thresholds. They come from your own conversion data.

## 2. A service case needs a technician visit

**Situation.** Customer Service agents log faults that need an engineer. Today they re-key details into a separate job system.

**What engages.**
1. `customer-service:case-lifecycle-design` defines when a case needs field work and what status it holds meanwhile.
2. `field-service:work-order-design` defines the work order created from the case and what flows back on completion.
3. `field-service:incident-types-and-service-tasks` standardises the fault types so the right skills and parts are booked.

**Reviewer gate.** `design-authority:design-review` checks there is one source of truth for status and that the case does
not close before the work order does.

**What the library cannot decide.** Whether your organisation bills from the case, the work order or the ERP.

## 3. A customer withdraws consent

**Situation.** A contact unsubscribes from marketing email and later calls the service desk.

**What engages.**
1. `marketing:consent-and-preference-centre` records the withdrawal against the right purpose and channel.
2. `customer-service:digital-and-voice-channels` checks that service communications are not blocked by a marketing opt-out.
3. `integration-and-data:integration-architecture` checks that the withdrawal reaches every system that sends messages.

**Reviewer gate.** `security-compliance:marketing-consent-compliance`, blocking. A withdrawal that does not reach every
sending system is a compliance failure, not a defect to fix after go-live.

**What the library cannot decide.** Your lawful basis for each purpose. That is your DPO's call.

## 4. A 25-user SMB goes live on Sales and Customer Service with one consultant

**Situation.** A partner consultant is the architect, configurer and trainer. The owner wants go-live in four months.

**What engages.**
1. `project-tailoring:edition-selection` confirms the SMB edition and what can be simplified.
2. `project-tailoring:role-mapping` maps the consultant and internal staff to roles and flags unsafe combinations, such as
   the consultant testing their own configuration.
3. `programme-management:delivery-plan` and `testing-quality:user-acceptance-testing` keep the plan realistic and make sure
   key users, not the consultant, sign off UAT.

**Reviewer gate.** `design-authority:customisation-challenge` keeps the build close to standard, which is what keeps a
small project supportable.

**What the library cannot decide.** Whether four months is achievable. It shows you what has to be true for it to be.

## 5. An enterprise moves its contact-centre voice channel into Dynamics 365

**Situation.** A large service desk wants voice, chat and email routed in one place, with call recording.

**What engages.**
1. `customer-service:digital-and-voice-channels` and `customer-service:queues-and-routing` design channels and routing.
2. `integration-and-data:integration-architecture` covers the telephony integration and its failure modes.
3. `testing-quality:performance-testing` and `platform-administration:licensing-and-capacity` cover concurrency and capacity.

**Reviewer gate.** `security-compliance:data-retention` on call recording retention and access. Blocking until retention
periods and access are agreed with the DPO.

**What the library cannot decide.** The licensing for your channel mix. Confirm with the Microsoft licensing guide or your partner.

## 6. Field technicians lose data offline in the first week of hypercare

**Situation.** Technicians in poor-coverage areas report notes and parts usage disappearing.

**What engages.**
1. `support-operations:hypercare` triages the incident and protects technicians' work in the meantime.
2. `field-service:mobile-and-offline` reviews the offline profile, sync scope and conflict handling.
3. `platform-engineering:plugin-design` checks for server-side logic that rejects records synchronised later.

**Reviewer gate.** `design-authority:change-impact-assessment` before the offline profile changes in production.

**What the library cannot decide.** Which data technicians genuinely need offline. That comes from riding along with them.
