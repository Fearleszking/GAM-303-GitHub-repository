import unreal,json,time,traceback
from pathlib import Path
out=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_sequence.json')
world=unreal.EditorLevelLibrary.get_game_world()
pawn=unreal.GameplayStatics.get_player_pawn(world,0)
def actors(path):
 c=unreal.load_class(None,path+'.'+path.split('/')[-1]+'_C')
 return list(unreal.GameplayStatics.get_all_actors_of_class(world,c))
manager=actors('/Game/ExoLuna/Boss/BP_BossEncounterManager')[0]
boss=actors('/Game/ExoLuna/Boss/BP_CrystalGolem')[0]
door=actors('/Game/Module04/BP_PuzzleDoor')[0]
trigger=actors('/Game/ExoLuna/Boss/BP_BossArenaTrigger')[0]
plates=sorted(actors('/Game/Module04/BP_Button'),key=lambda a:a.get_editor_property('ButtonIndex'))
cubes=[a for a in actors('/Game/Module04/BP_ColorPickup') if a.get_class().get_name()=='BP_ColorPickup_C']
crystals=sorted(actors('/Game/ExoLuna/Boss/BP_BossCrystal'),key=lambda a:a.get_editor_property('ColorID'))
pedestals=sorted(actors('/Game/ExoLuna/Boss/BP_CrystalPedestal'),key=lambda a:a.get_editor_property('ColorID'))
results=[]
def snap(label):
 results.append({'label':label,'time':round(time.monotonic()-start,2),'player_health':pawn.get_editor_property('Health'),'player_position':str(pawn.get_actor_location()),'door_unlocked':door.get_editor_property('IsUnlocked'),'plates':[a.get_editor_property('IsPressed') for a in plates],'boss_health':boss.get_editor_property('Health'),'boss_state':boss.get_editor_property('State'),'interval':boss.get_editor_property('AttackInterval'),'encounter':manager.get_editor_property('EncounterState'),'remaining':manager.get_editor_property('RemainingSeconds'),'progress':manager.get_editor_property('ActivatedCount'),'pedestals':[a.get_editor_property('Activated') for a in pedestals],'holding':pawn.get_editor_property('IsHolding')})
 out.write_text(json.dumps(results,indent=2))
def place(a,pos):
 cube=a.get_editor_property('Cube')
 cube.set_simulate_physics(False)
 a.set_actor_location(pos,False,True)
 cube.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS)
 cube.set_simulate_physics(True)
def original(i):
 plate=plates[i];color=plate.get_editor_property('PickupColor')
 cube=min(cubes,key=lambda a:sum((getattr(a.get_editor_property('PickupColor'),c)-getattr(color,c))**2 for c in ['r','g','b']))
 pos=plate.get_actor_location();pos.z+=65
 place(cube,pos)
def boss_place(crystal_id,pedestal_id):
 place(crystals[crystal_id],pedestals[pedestal_id].get_editor_property('Socket').get_world_location())
def pickup():
 crystals[0].call_method('INT_Interact',(pawn,))
def drop():
 crystals[0].call_method('INT_Drop',(pawn,))
def damage():
 unreal.GameplayStatics.apply_damage(pawn,200.0,unreal.GameplayStatics.get_player_controller(world,0),boss,unreal.DamageType)
steps=[(0,lambda:snap('initial')),(0.2,lambda:original(0)),(2,lambda:snap('one_original_cube')),(2.2,lambda:original(1)),(4,lambda:snap('two_original_cubes')),(4.2,lambda:original(2)),(6,lambda:snap('three_original_cubes')),(6.2,lambda:trigger.call_method('INT_Interact',(pawn,))),(7,lambda:snap('teleported')),(13,lambda:snap('projectile_damage')),(13.2,pickup),(13.4,lambda:snap('pickup')),(13.6,drop),(14,lambda:boss_place(0,1)),(15,lambda:snap('incorrect_color')),(15.2,lambda:boss_place(0,0)),(16,lambda:snap('first_correct')),(18,lambda:snap('stun_and_duplicate')),(22,lambda:snap('resume_phase_two')),(22.2,lambda:boss_place(1,1)),(23,lambda:snap('second_correct')),(29,lambda:snap('resume_phase_three')),(29.2,lambda:boss_place(2,2)),(30,lambda:snap('victory')),(31,lambda:manager.call_method('RetryEncounter')),(32,lambda:snap('retry_after_victory')),(32.2,damage),(33,lambda:snap('health_defeat')),(34,lambda:manager.call_method('RetryEncounter')),(35,lambda:snap('retry_after_defeat'))]
start=time.monotonic();index=0
def tick(dt):
 global index
 try:
  while index<len(steps) and time.monotonic()-start>=steps[index][0]:
   fn=steps[index][1];index+=1;fn()
  if index==len(steps):unreal.unregister_slate_post_tick_callback(handle)
 except Exception:
  results.append({'error':traceback.format_exc(),'step':index});out.write_text(json.dumps(results,indent=2));unreal.unregister_slate_post_tick_callback(handle)
handle=unreal.register_slate_post_tick_callback(tick)

