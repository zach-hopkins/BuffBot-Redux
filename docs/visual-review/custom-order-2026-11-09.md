# Custom timing and invisibility repair

Investigated using a private copy of the newest quicksave, with the selected
57-entry New Prebattle list in Custom. The personal save and running personal
game were not controlled or saved by the diagnostic harness.

## Causes

Mass Invisibility preceded targeted Improved Haste casts in the same caster's
saved sequence. The estimate and executor both added an anticipatory invisibility
dependency pointing backward from those later casts. Together with the caster's
own queue order this made a cycle. The solver returned no estimate, while runtime
dependencies could leave a lane pending after other casters finished.

Custom formerly had no deliberate end-alignment, so a character with only Ring
of Duplication could use it immediately despite its low position in the displayed
list. Its expiration prediction could consequently be correct while the behavior
was unexpected.

## Behavior

- Custom preserves per-caster saved sequences and uses the shared read-only
  timing model to align short independent lanes near completion. It does not
  impose global serial dispatch. Long First remains immediate; Smart also
  optimizes order.
- Uses of one physical item have a shared sequence dependency, preserving their
  relevant relative order. Borrowing starts only after its timing gate; once a
  handoff is ready the item is used promptly, without another deliberate delay.
- Smart's invisibility look-ahead is not imposed on Custom. Custom flags the
  earlier invisibility with Later buffs may fail, and affected targeted buffs
  with Target may be invisible. Saved order and native targeting rules remain.
- Smart's primary optimization score is now the minimum remaining duration in
  seconds, then total remaining duration, rather than retained fractions.
- An Important/star control was discussed but is not part of this patch.

## Verification

1,029 runtime tests passed, including Custom end-alignment, shared physical-item
sequencing, cyclic invisibility estimates and warning generation. Installer and
package code were unchanged. The private fixture replenishes prepared books and
daily charges to exercise all 57 saved requests using native spell/item actions;
this is diagnostic setup, not a runtime replenishment feature.

The revised model predicts 1,710 game ticks of preparation, with 96 seconds left
on the first ring use. A proposed globally ordered variant was discarded after
the user clarified that useful cross-caster overlap must remain; its 2,629-tick
estimate is not the final implementation.

The final native 2x run completed 57 casts with zero runtime skips and no timeout.
The three ring casts were issued at game ticks 46,541,150, 46,541,179 and
46,541,253. The first completed at 46,541,176; the run finished at 46,541,357,
leaving approximately 95.9 seconds of its 108-second duration. Fast-forward
ownership was released, speed restored to 30, and no loan or transfer journal
remained. Native acceptance/effect landing is still subject to the warned-about
Custom targeting choices.

Backed up and installed the four changed source/runtime modules in Definitive.
The executor received only the relevant field propagation changes, preserving
that install's existing completion/localization behavior. WeiDU.log and personal
saves were unchanged; the running personal game was left open.
