# Smart Order and casting waits: Test Me save

Investigated in a separate copy of `000000094-Test Me`. The personal game
process and original save were left open and unchanged.

## Causes and changes

- Allocation formerly followed the current row positions. Sorting could give
  a scarce stronger source to another recipient, changing both duration keys
  and summon dependencies after they had already been calculated. Allocation
  now follows saved manual priorities, including when displaying or executing
  the sorted list. New unranked requests follow existing requests. Explicit
  source selections and augmenting-path resource reservations remain intact.
- Smart/Long sorting now starts from saved priorities, so an earlier sorting
  result cannot become the next invocation's tie-breaker. Dependencies and
  their duration priorities use the same assignments as queue construction.
- Creation steps inherit their longest dependent buff's sorting priority.
  The helmet's 96-second summon duration no longer leaves its 780-second buffs
  behind ordinary short buffs. Creator-before-dependent constraints still
  apply in every order mode.
- The latest-start solver previously delayed entire caster lanes, including
  Stoneskin and other long buffs, and could insert repeated multi-round gaps
  as the remaining schedule was recalculated. Permanent buffs and buffs lasting
  at least five minutes now start at their earliest feasible time. Short buffs
  retain deliberate latest-start scheduling; actual aura, native casting time,
  invisibility and summon prerequisites still apply.
- Summon creation and borrowed item use are also eager. A deferred loan must
  pass the timing gate before borrowing starts, so a scheduled wait cannot
  take custody and suspend its item's owner prematurely.
- Repeated native runs exposed an intermittent Ring of Duplication skip.
  A bounded trace caught a return-phase journal with both actors present in
  the same area but the ring temporarily absent from every party inventory.
  Native GiveItem was between removal and destination attachment. Custody
  checks now allow up to 30 game ticks for that handoff, preserving the return
  journal throughout. Persistent absence still fails; no item is created and
  no charges are restored. Active equipment-swap recovery also precedes the
  inventory/fingerprint check.

## Native verification

- The selected preset contains 51 requests, 50 available at preflight.
- The old run showed Aerie waiting about 15–17 game seconds between successive
  long-buff actions. It was stopped for diagnosis after ten casts; this was
  not a completed baseline or a watchdog result.
- The fixed preset produced identical order/source signatures across ten
  forced recalculations before execution, and twelve more after execution.
  Dependency validation passed each time.
- Vhailor's Helm moves ahead of its long clone casts and ordinary short buffs.
  All clone-dependent rows follow creation. Its exact position can improve
  when timing and incoming-protection dependencies are considered together.
- A Force All native execution completed 50 casts with zero runtime skips,
  in 868 game ticks (about 58 game seconds). This was a direct normal-speed
  harness run, not a fast-forward benchmark. Independent caster issue/finish
  events overlap. The clone was bound after creation and issued its real spells.
- No timing fallback, outstanding live loan or saved transfer journal remained.
- Aerie still has an intentional wait before her short-buff tail. Native aura
  waits and useful short-buff alignment are retained; eliminating every visible
  pause would contradict the requested duration-preserving scheduling.

Raw preset and timing evidence is kept under the local diagnostic scratch
directory rather than publishing the user's complete save-backed plan.

## Regression and installation

- Full suite: 1,165 passed, six deliberately excluded platform/IWD cases.
  Final focused run including the additional allocation/loan regressions:
  1,026 runtime tests passed (installer/package checks excluded from this final
  rerun). No IWD gameplay testing was performed.
- Backed up and installed the changed modules to Definitive's BuffBot
  source and override directories. The installed executor received only the
  new timing gate, preserving that installation's older completion/localization
  behavior. WeiDU.log was unchanged; no saves were written.

## Spell Ineffective and estimated remaining duration

The native message history placed Aerie's rejection immediately after Anomen's
Righteous Wrath of the Faithful. A controlled repeat with Aerie's magic
resistance explicitly set to zero reproduced the rejection with Spell
Deflection present, and no rejection with it removed. This is spell protection,
not a failed magic-resistance roll. The installed party spell launches its
buffs through single-target children, which can encounter that protection.

Smart ordering and the real dispatch model now defer Spell Deflection/Turning
until other casters' incoming buffs, including party wrappers, have completed.
Self casts remain independent. A final native 2x run completed 50 casts with
zero runtime skips and no Aerie Spell Ineffective message. Item-return state
was clear after completion; the fast-forward audit recorded speed restoration.

Order now shows Duration and Est. Left separately. The latter reuses the
concurrent scheduling model, subtracting the time between the estimated spell
release and whole-plan finish. Custom/Long use earliest native dispatch;
Smart includes intentional delays. Unknown/unavailable casts show a dash,
permanent buffs remain permanent, and exhausted durations show Expired.
Native preview of the copied preset showed 40.0m Stoneskin with 39.2m left,
and the final Improved Invisibility retaining its full 1.9m. Its estimated
preparation was 724 game ticks, not a wall-clock promise. Movement, actual
handoffs, projectiles and failed casts can change the result. The compact
native layout was visually checked with both duration columns and inline
move/remove controls.
