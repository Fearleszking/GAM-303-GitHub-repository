# ExoLuna GAM 303 rubric review

Review date: October 16, 2026. Project owner: Aaron Marquez.

Reference: GAM 303 Final Project Guidelines and Rubric (2).pdf, all seven pages. Its extracted text is identical to the previously supplied (1) copy. This is a requirements review, not an instructor grade. The rubric is reference material; the user's development assignment determines the authorized work.

## Part I

| Criterion | Weight | Evidence and current assessment | Remaining work |
|---|---:|---|---|
| Feature branching | 11 | Existing `feature/boss-encounter` branch contains commit `670e60e`, separate from `main`. Earlier merged feature branches are present in history. | Preserve this branch and prepare the requested review PR. The branch name differs from the assignment's requested `feature/crystal-golem-boss`; do not overwrite either branch. |
| Frequent, accurate, informative commits | 11 | History includes menu/HP work `7fbfb27`, alpha polish `db7ab82`, and boss encounter `670e60e`. | Record remaining completed changes with informative commits. Do not fabricate earlier commits or claim the boss was developed in multiple historical commits. |
| Traceability | 17 | Original environmental cube puzzle and new timed pedestal encounter map to the two required puzzle types. New manager supplies health/defeat, win, countdown, and separate game-time display. The October 9 matrix records Pre-alpha, Alpha, and Final submission phase targets. | Update the official matrix to the implemented final scope. Preserve its phase schedule; do not invent calendar dates. |
| Test features and descriptions | 17 | PIE evidence exists for original plates, teleport, damage, matching, phase timing, defeat, retry, HUD, and menu. | Transfer procedures and evidence into the submission template. Complete a continuous manual playthrough and remaining control/navigation checks. |
| Test pass/fail and errors | 11 | Runtime JSON records actual values. Harness failures are preserved separately from gameplay failures. | Keep unexecuted tests marked pending. Include exact errors and the scope of each pass. |
| Test updates/error resolution | 11 | Retests cover final-crystal trace obstruction, defeated-state preservation, projectile configuration, and HUD contrast. | Include initial failure, corrective action, and retest outcome in the official test plan. |
| Prototype functionality | 11 | Boss puzzle, environmental damage, timed loss, health loss, victory, and reset run in the existing playable map. | Complete all outstanding verification before claiming every design requirement is met. Finish comments on all new gameplay graphs and audit existing comments without rebuilding prior systems. |
| Level design | 11 | Arena uses simple geometry, four cover pillars, three objectives, enclosed boundaries, and a safe start point. Four wall sweeps blocked the player capsule in PIE. | Validate complete walking/carrying routes, corners, jumping, objective readability, and continuous natural progression. Wall sweeps alone do not prove every route is safe. |

## Part II

The postmortem must include specific project examples and the task log. Required categories are problems (15%), what went well (15%), lessons (15%), scope refactoring (22.5%), balanced approach (22.5%), and clear communication (10%).

Supported examples for the postmortem:

- **Problem and mitigation:** the shrine arrival volume intercepted the visibility trace to the final crystal. The boss trigger now changes that volume's visibility response while retaining pawn overlap behavior. Native E interaction subsequently entered the arena.
- **Problem and mitigation:** stopping combat overwrote the boss's defeated state. The stop function now retains Defeated when health is zero; the retest recorded health zero, state 3, hidden shield, and victory UI.
- **Problem and mitigation:** white HUD text lost contrast over the arena floor. Black offset shadows were added; the October 16 PIE review confirmed legible text.
- **Reusable success:** inherit the existing color-pickup/physics system and use separate boss pedestal classes, preserving the original puzzle.
- **Scope decision:** a stationary boss, static meshes, simple rock rotation, and timers keep the prototype focused on playability. No skeletal animation or navigation AI is needed for this encounter.
- **Lesson:** verify the player's actual interaction trace and UI buttons in addition to calling Blueprint functions from a test harness. Scripted state checks cannot replace a full player playthrough.
- **Balanced work:** implementation and tests cover combat, puzzle progression, reset, collision, and UI. Detailed art remains secondary to functional requirements.

These are development evidence notes, not a substitute for Aaron's personal reflection or course feedback. No task duration, original schedule, or completion date should be invented.

## Submission requirements

The rubric requests the completed Traceability Matrix and Test Plan Template with the repository link, the prototype through that repository, and a polished postmortem with task log. The instructor's repository access must be active; access has not been verified here. AI assistance must be acknowledged. An appropriate factual acknowledgment is: "OpenAI Codex assisted with Blueprint development, debugging, test execution, and documentation. Aaron Marquez is responsible for reviewing and submitting the project."

The project is not yet certified as fully complete. Outstanding items are the full manual playthrough/control and route checks, complete graph-comment coverage, submission-template updates, and the review PR. Nine new Blueprints compiled after the short comment edits; the current log scan found no Blueprint runtime errors, Accessed None, or Blueprint compiler errors. Packaging and instructor access have not been verified.

Follow-up verification: native WASD, mouse and jump/landing checks passed. All three carrying routes and native E pickup/drop pairs passed during one uninterrupted live-combat boss run; victory appeared with 60 health and 29 seconds remaining. Movement and aiming were scripted. Nine boss assets and nine existing assets compiled in the reopened editor, with no matching Blueprint errors/warnings in its reviewed active log. Full manual progression, exhaustive escape checks and the complete comment audit still remain. Two newer uncommitted boss-asset revisions were preserved separately; earlier runtime results are not claimed to certify those later revisions.
