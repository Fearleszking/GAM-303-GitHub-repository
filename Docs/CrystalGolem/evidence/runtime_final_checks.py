import unreal, json, time, traceback
from pathlib import Path

OUT=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_final_checks.json')
world=unreal.EditorLevelLibrary.get_game_world()
pawn=unreal.GameplayStatics.get_player_pawn(world,0)
def cls(name): return unreal.load_class(None,'/Game/ExoLuna/Boss/'+name+'.'+name+'_C')
def actors(name): return list(unreal.GameplayStatics.get_all_actors_of_class(world,cls(name)))
manager=actors('BP_BossEncounterManager')[0]
boss=actors('BP_CrystalGolem')[0]
crystals=sorted(actors('BP_BossCrystal'),key=lambda a:a.get_editor_property('ColorID'))
pedestals=sorted(actors('BP_CrystalPedestal'),key=lambda a:a.get_editor_property('ColorID'))
report=[]
def snap(label):
 report.append({'label':label,'elapsed':round(time.monotonic()-start,2),'health':pawn.get_editor_property('Health'),'boss_health':boss.get_editor_property('Health'),'encounter':manager.get_editor_property('EncounterState'),'remaining':manager.get_editor_property('RemainingSeconds'),'progress':manager.get_editor_property('ActivatedCount'),'shots':len(actors('BP_GolemProjectile')),'widgets_in_viewport':{n:sum(1 for w in unreal.ObjectIterator(unreal.UserWidget) if w.get_class().get_name()==n+'_C' and w.is_in_viewport()) for n in ['WBP_BossHUD','WBP_VictoryScreen','WBP_DefeatScreen']}})
 OUT.write_text(json.dumps(report,indent=2))
def begin():
 manager.call_method('LoseEncounter');manager.call_method('RetryEncounter');boss.call_method('StopCombat');snap('begin_120')
def isolated_shot():
 global shot
 boss.call_method('StartCombat');boss.call_method('Attack');boss.call_method('StopCombat')
 shot=actors('BP_GolemProjectile')[0]
 shot.set_actor_location(unreal.Vector(14000,0,7000),False,True)
 shot.set_editor_property('Speed',1200.0);shot.set_editor_property('Lifetime',2.0)
 shot.call_method('ConfigureProjectile')
 report.append({'label':'projectile_config','speed':shot.get_velocity().length(),'lifespan':shot.get_life_span(),'owner_is_boss':shot.get_owner()==boss})
 OUT.write_text(json.dumps(report,indent=2))
def shot_expired():
 report.append({'label':'projectile_expired','valid':unreal.SystemLibrary.is_valid(shot)})
 OUT.write_text(json.dumps(report,indent=2))
def moving_shot():
 report.append({'label':'projectile_after_movement_update','speed':shot.get_velocity().length(),'movement_speed':shot.get_editor_property('Movement').get_editor_property('velocity').length()})
 OUT.write_text(json.dumps(report,indent=2))
def retry():
 manager.call_method('LoseEncounter');manager.call_method('RetryEncounter');boss.call_method('StopCombat');snap('retry_once')
def retry_again():
 manager.call_method('LoseEncounter');manager.call_method('RetryEncounter');boss.call_method('StopCombat');snap('retry_twice')
def walls():
 for label,origin,target in [('west',(12100,0,3095),(11500,0,3095)),('east',(15900,0,3095),(16500,0,3095)),('north',(14000,1900,3095),(14000,2500,3095)),('south',(14000,-1900,3095),(14000,-2500,3095))]:
  pawn.set_actor_location(unreal.Vector(*origin),False,True)
  pawn.set_actor_location(unreal.Vector(*target),True,False)
  p=pawn.get_actor_location()
  report.append({'label':'wall_'+label,'position':[p.x,p.y,p.z],'inside':11900<p.x<16100 and -2100<p.y<2100})
 pawn.set_actor_location(unreal.Vector(12300,0,3095),False,True)
 pawn.get_editor_property('CharacterMovement').stop_movement_immediately()
 OUT.write_text(json.dumps(report,indent=2))
def place(i):
 cube=crystals[i].get_editor_property('Cube');cube.set_simulate_physics(False)
 crystals[i].set_actor_location(pedestals[i].get_editor_property('Socket').get_world_location(),False,True)
 cube.set_collision_enabled(unreal.CollisionEnabled.QUERY_AND_PHYSICS);cube.set_simulate_physics(True)
def activate():
 boss.call_method('StartCombat')
 place(0);place(1);place(2)
steps=[(0,begin),(0.2,isolated_shot),(0.5,moving_shot),(3,shot_expired),(3.2,retry),(3.4,retry_again),(4.4,lambda:snap('one_second_after_retry')),(4.5,walls),(5,activate),(6,lambda:snap('victory_widgets'))]
start=time.monotonic();index=0
def tick(dt):
 global index
 try:
  while index<len(steps) and time.monotonic()-start>=steps[index][0]:
   fn=steps[index][1];index+=1;fn()
  if index==len(steps):unreal.unregister_slate_post_tick_callback(handle)
 except Exception:
  report.append({'error':traceback.format_exc(),'step':index});OUT.write_text(json.dumps(report,indent=2));unreal.unregister_slate_post_tick_callback(handle)
handle=unreal.register_slate_post_tick_callback(tick)
