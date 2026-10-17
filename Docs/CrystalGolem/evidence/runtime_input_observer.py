import unreal,time,json
from pathlib import Path
world=unreal.EditorLevelLibrary.get_game_world();pawn=unreal.GameplayStatics.get_player_pawn(world,0)
def actors(n):return list(unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_class(None,'/Game/ExoLuna/Boss/'+n+'.'+n+'_C')))
manager=actors('BP_BossEncounterManager')[0];boss=actors('BP_CrystalGolem')[0]
manager.call_method('LoseEncounter');manager.call_method('RetryEncounter');boss.call_method('StopCombat');manager.call_method('ClearProjectiles')
pawn.get_editor_property('CharacterMovement').stop_movement_immediately()
start=time.monotonic();samples=[];last=-1
def tick(dt):
 global last
 t=round(time.monotonic()-start,1)
 if t!=last:
  last=t;p=pawn.get_actor_location();r=unreal.GameplayStatics.get_player_controller(world,0).get_control_rotation()
  samples.append({'t':t,'position':[p.x,p.y,p.z],'rotation':[r.pitch,r.yaw,r.roll]})
  Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_input_observer.json').write_text(json.dumps(samples,indent=2))
 if t>60:unreal.unregister_slate_post_tick_callback(handle)
handle=unreal.register_slate_post_tick_callback(tick)
