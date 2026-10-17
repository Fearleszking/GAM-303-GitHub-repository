from pathlib import Path
source=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_sequence.py').read_text()
prefix=source.split('steps=[')[0]
exec(compile(prefix,'regression_setup.py','exec'))
out=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_resumed_regression.json')
steps=[(0,lambda:snap('initial')),(0.2,lambda:original(0)),(1,lambda:snap('one_original_cube')),(1.2,lambda:original(1)),(2,lambda:snap('two_original_cubes')),(2.2,lambda:original(2)),(3,lambda:snap('three_original_cubes')),(3.2,lambda:trigger.call_method('INT_Interact',(pawn,))),(4,lambda:snap('teleported')),(8,lambda:snap('combat_active')),(8.2,lambda:boss_place(0,1)),(9,lambda:snap('incorrect_color')),(9.2,lambda:boss_place(0,0)),(10,lambda:snap('first_correct')),(12,lambda:snap('duplicate_and_stun')),(16,lambda:snap('resume_phase_two')),(16.2,lambda:boss_place(1,1)),(17,lambda:snap('second_correct')),(23,lambda:snap('resume_phase_three')),(23.2,lambda:boss_place(2,2)),(24,lambda:snap('victory')),(25,lambda:manager.call_method('RetryEncounter')),(26,lambda:snap('retry_after_victory')),(26.2,damage),(27,lambda:snap('health_defeat')),(28,lambda:manager.call_method('RetryEncounter')),(29,lambda:snap('retry_after_defeat'))]
start=time.monotonic();index=0
exec(compile('def tick'+source.split('def tick',1)[1],'runtime_resumed_regression.py','exec'))
