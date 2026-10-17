# Final scope traceability

Updated October 16, 2026. Repository: https://github.com/Fearleszking/GAM-303-GitHub-repository. Original schedule uses Pre-alpha, Alpha and Final submission phases; these phase targets are preserved from the October 9 matrix. Calendar deadlines and historical completion dates have not been invented.

| Requirement | Implementation plan / actual system | Schedule phase | Verification |
|---|---|---|---|
| Single-player first person | Retain existing BP_Player and player GameMode. | Pre-alpha | Existing PIE pawn; no multiplayer additions. |
| WASD, mouse, Space | Preserve existing enhanced input and movement/camera/jump functions. | Pre-alpha | Native WASD taps, mouse rotation and jump/landing verified in `runtime_input_observer.json`. |
| E or left-click interaction | Retain E visibility trace and interaction interface. | Pre-alpha -> Alpha | Native final-crystal teleport and crystal pickup/drop verified. |
| Physics interactions | Inherit BP_ColorPickup/BP_PhysicsPickup for boss crystals. | Alpha | All three native E pickup/drop pairs and carrying routes completed during continuous live combat. |
| Health and defeat | Existing health function/HP widget; route health-zero to boss manager loss. | Alpha -> Final submission | Health 100 ->90 projectile damage; lethal damage caused defeat. |
| Environmental puzzle | Preserve original three-cube color plates and door. | Pre-alpha -> Alpha | Locked until three matching placements; tests 1/2. |
| Timed puzzle | Three matching boss crystals/pedestals within 120 seconds. | Alpha -> Final submission | Matching/rejection/duplicate/stun/timeout tests 5/9-16. |
| Boss uses environment | Pedestal activation is the only boss-health path; stationary Golem attacks while puzzle progresses. | Alpha -> Final submission | Health 3 ->2 ->1 ->0; final state 3 and victory. |
| Learned mechanics | Original color matching and E pickup precede arena reuse of those mechanics. | Final submission | Systems verified separately; continuous player playthrough pending. |
| Win/lose/retry | Manager owns state, result UI, cleanup and complete arena reset. | Alpha -> Final submission | Tests 14-18 and repeated widget/countdown checks. |
| Single playable level | Arena geometry added inside LV_ExoLuna_Alpha; menu map remains UI only. | Pre-alpha -> Final submission | Current map and actor inspection; safe teleport test. |
| Natural progression/blockout | Existing ruins, gate, cover and shrine lead to final crystal; arena offers multiple objective routes and four pillars. | Pre-alpha -> Final submission | Four wall sweeps and all three carrying routes passed. Fully manual start-to-finish progression and exhaustive jump/corner checks remain pending. |
| Health UI | Keep existing Player_Widget. | Alpha | Visible full and reduced HP in native PIE. |
| Game-time UI | Manager tracks GameSeconds independently from RemainingSeconds. | Alpha -> Final submission | Game time runs before arena; countdown starts at encounter and resets independently. |
| Boss UI | WBP_BossHUD displays health, time, progress and objective; result widgets handle replay/menu. | Final submission | HUD contrast, urgent timer, victory/retry/menu checked. |
| Comments | Short explanations in new graph sections at user request. | Final submission | Nine new assets have four-word explanations; full per-function comment audit remains pending. |
| Classes/timers | Gameplay lives in Blueprint classes; repeated attacks/countdown/checks use timers. Tick used for decorative rock motion. | Final submission | Graph inspection and measured attack intervals. |
| No asset packs/Starter Content | Existing project assets/materials and simple engine geometry. | All phases | New boss asset references reviewed; no new external packs introduced. |
| Feature branching/commits | Continue saved feature/boss-encounter, preserve baseline, commit meaningful work. | All phases | `670e60e` implementation; `e2170a2` concise explanations. |
| PR review | Prepare review PR after tests; merge requires owner approval. | Final submission | PR preparation pending. |
| Test plan/task log/postmortem | Maintain procedures, actual results, errors, retests and scope decisions. | Alpha -> Final submission | Accompanying test record, development log and rubric review. Official template transfer and personal reflection remain. |

## Proposal scope adjustment

The earlier matrix listed separate timed runes, pillar alignment, and three full ancient seals. The user's final Crystal Golem assignment replaces that extra scope with the original cube puzzle plus a timed three-crystal boss puzzle. Those older proposal features are not marked implemented. Boss pedestal progress is not relabeled as three completed full-game seals.

The rubric's minimum design requires two puzzles, including timed and environmental puzzles, and an environmental boss encounter. The implemented structure targets those requirements. Passing isolated functionality tests does not certify the final continuous playthrough or submission readiness.
