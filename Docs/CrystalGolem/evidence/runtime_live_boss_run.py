from pathlib import Path
source=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_carry_routes.py').read_text()
source=source.replace('runtime_carry_routes.json','runtime_live_boss_run.json')
source=source.replace(";boss.call_method('StopCombat')",'')
source=source.replace("else:boss.call_method('StartCombat')","else:pass")
exec(compile(source,'runtime_live_boss_run.py','exec'))
