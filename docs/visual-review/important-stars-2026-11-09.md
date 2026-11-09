# Important casts

Each Order row has an outlined/filled native star in its own dispatch cell.
Marking a cast activates Smart Order, keeps the selected request and its saved
manual bookmark, and does not change its explicit source. Unmarking leaves
the current order mode selected. Custom and Long First retain the marks for a
later return to Smart; the priority objective applies in Smart.

Smart compares minimum starred duration remaining, total starred duration
remaining, minimum ordinary duration remaining and total ordinary duration
remaining, in that order. Permanent and unavailable durations are omitted from
the finite score. A dependency-aware important-last seed and bounded swaps of
adjacent rows/same-caster neighbors improve plans that have interleaved rows.
Candidates cannot exceed the initial feasible Long First preparation estimate.
Summon, item, invisibility and spell-protection restrictions still apply. This
is a bounded heuristic, not a guaranteed global optimum.

The optional per-request flag survives save validation. Export format 3 carries
it; formats 1 and 2 remain readable with all entries initially unmarked. The
native star art is original polygon geometry, generated as two BAM V2 states
using the project's existing BC3 codec. New resources are BFBSTAR.BAM and pages
MOS88994/MOS88995; the allowlist, hashes and full asset builder include them.

## Validation

- 1,181 tests passed; six existing platform/IWD cases excluded. This includes
  installer/packaging, asset integrity, old import formats, flag roundtrips,
  selection dispatch, saved Custom positions and priority scoring.
- Native preview on the copied 57-entry preset, with all four Improved Haste
  requests starred: predicted remaining time improved from 100.2 to 112.2,
  113.4 to 121.73, 119.4 to 127.73 and 106.2 to 118.2 seconds. Source identities
  were identical, and predicted preparation stayed at 1,648 game ticks.
- Physical native star click removed only the selected Improved Haste mark;
  no source menu opened. Outlined and filled stars, column headers and controls
  were visually checked in the native compact layout.
- A real native 2x run of all 57 available entries, with four Important marks,
  completed 57 casts and zero runtime skips. Speed returned to 30, with no
  active fast-forward ownership, item loan or transfer journal left.
- Backed up and installed the updated modules/manifests/art in Definitive's
  source and override directories. WeiDU.log and personal saves were unchanged.
  The user must reopen the game to load the new menu and code.
