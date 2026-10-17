# Crystal Golem development log

Project: ExoLuna: The Forgotten Isle. Engine: existing Unreal Engine 5.8 configuration. Implementation: Blueprints. Repository: https://github.com/Fearleszking/GAM-303-GitHub-repository.

## Preserved baseline

The current work continues `feature/boss-encounter` at `670e60e` (repository commit date October 13, 2026). This existing commit contains the integrated arena and encounter. Its parent is `b1939ff`, the main-menu/HP feature merge. The separately existing local `feature/crystal-golem-boss` branch has not been overwritten. Historical tests below are identified by evidence rather than invented execution dates or durations.

| Work | Implementation / scope | Evidence |
|---|---|---|
| Inspect existing systems | Reused BP_Player E interaction, BP_ColorPickup/BP_PhysicsPickup, player health/HP widget, original cube plates/door, and turret damage concepts. Reviewed official design and rubric. | Existing Blueprint inspection JSON and extracted references retained in working records. |
| Arena integration | Added enclosed geometry, four pillars, three crystal/pedestal pairs, Golem and arena start in LV_ExoLuna_Alpha. | `670e60e`; runtime arrival and cover checks. |
| Golem behavior | Three HP, dormant/active/stunned/defeated states; timer attacks at 4/3/2.5 seconds; five-second stun. Tick rotates decorative rocks only. | `runtime_cover_timer.json`. |
| Environmental puzzle | Independent boss crystal/pedestal classes inherit existing pickup behavior. Matching ColorID, crystal lock, pedestal latch and manager color flags prevent duplicate damage. | `runtime_sequence.json`. |
| Encounter/UI | 120-second boss countdown and separate game-time timer; HUD, victory, defeat and retry. Manager owns widgets and cleanup. | `runtime_sequence.json`, `runtime_cover_timer.json`, `runtime_final_checks.json`. |
| Final crystal | Existing final beacon gets an interaction trigger, original-door gate, fade, teleport and one-time latch. Original shrine pawn overlap remains. | Native E check in prior session; scripted teleport evidence. |
| Existing player integration | Health-zero routes to encounter loss; original destroy path remains fallback when no manager exists. Existing control bindings retained. | `runtime_sequence.json`, health_defeat. |
| October 16 review | Reviewed updated seven-page rubric; extracted text matches earlier supplied copy. Inspected original submission matrix and preserved its phase schedule. | `ExoLuna_Rubric_Review.md`. |
| October 16 tests | Verified all four wall sweeps, edited projectile speed/lifetime, repeated retry widget count/countdown, victory replay, main-menu return, Controls, Credits and Play. | `runtime_final_checks.json`; native UI observations documented in test record. |
| October 16 comments | Added/shortened explanatory graph comments to four words at user request. Compiled and saved all nine new Blueprints. | `compile_2026_10_16.json`. |
| October 16 combat completion | Completed all three carried placements in one normal live-combat encounter using scripted movement/aim and native E. Victory appeared with 60 player health and 29 seconds remaining. | `runtime_live_boss_run.json`, route_complete at 92.25 seconds. |
| Resumed editor verification | Reconnected the reopened editor and compiled nine boss assets plus nine existing gameplay/HUD assets. Reviewed the active log: no matching Blueprint compiler/runtime errors, Accessed None, or Blueprint warnings. | `final_compile_review.json`. |

## Problems and resolution

| Problem | Corrective action | Retest |
|---|---|---|
| Final crystal interaction trace hit shrine arrival volume | Trigger sets arrival volume Visibility response to Ignore at BeginPlay, retaining pawn overlap. | Native E entered arena. |
| Defeat state overwritten by StopCombat | Retain Defeated when health is zero. | Health 0, state 3, shield hidden and victory UI. |
| Spawn-time projectile defaults masked editable values | ConfigureProjectile reapplies speed/lifetime after boss assignment. | October 16: movement speed 1200 after update, lifespan 2, shot expired. |
| HUD low contrast | Added black offset shadows to new HUD text. | October 16 native PIE review confirmed readability. |
| Original door interface event removed during editor inspection | Restored original interface event and its execution links; subsequent inspections avoid destructive graph DSL reads on original assets. | Original plate/door state tests passed. |
| Unsupported Python test APIs | Used ObjectIterator for widget counts and existing boss Attack to spawn a test shot. | Corrected final-check script completed. These were harness errors, not runtime game errors. |

## Scope decisions

Preserved the original cube puzzle, menu, level, doors, physics objects and HP widget. Added the boss arena inside the existing playable map. Used simple geometry and existing project materials. Kept the boss stationary and avoided skeletal animation/navigation AI. The timed three-pedestal boss puzzle supplies the design document's required timed puzzle; the original three-cube puzzle supplies its environmental puzzle.

The earlier proposal's separate rune puzzle, rotating-pillar puzzle and three full seals were not added as unrelated features. The final implementation uses the user's approved Crystal Golem scope. The submission matrix must explicitly record this scope adjustment rather than marking those abandoned proposal features complete.

## Remaining acceptance work

Complete a fully manual playthrough from the original level start, finish any uncovered per-function comments, and transfer final evidence into the official submission template. Packaging and instructor access remain unverified. The task log does not claim all original proposal features or all acceptance tests are finished. Native WASD, mouse and Space checks passed October 16. The later uninterrupted boss run passed with normal attacks and damage; all three pickup/drop pairs used native E while movement/aim were scripted.

On reconnecting the reopened editor, BP_CrystalGolem and BP_BossEncounterManager already had uncommitted binary changes newer than the concise-comment commit. Both were backed up before compilation and preserved. Their unreviewed changes are excluded from the documentation commit; earlier runtime results are not asserted to certify these later binary revisions. Automatic approval review briefly failed because of its usage limit; a later authorized retry succeeded.

AI assistance: OpenAI Codex assisted Blueprint development, debugging, tests and documentation. Aaron Marquez remains responsible for review and final submission.

Resumed local-revision retest: the current Golem/manager revisions passed a 29-second scripted PIE sequence covering the original door locked through two placements, third-cube unlock, final-crystal interface teleport, wrong-color rejection, duplicate prevention, both phase resumes, three-pedestal victory with Defeated state 3, lethal-health defeat, and retry after both outcomes. Evidence: `runtime_resumed_regression.json`. The post-run active log again contained no matching Blueprint runtime/compiler errors or warnings. These are additional scoped runtime checks; the prior continuous carried-placement run remains separate evidence.
