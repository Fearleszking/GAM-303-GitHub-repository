import unreal,json,time,traceback,math
from pathlib import Path
out=Path('C:/Users/Aaron m/Documents/Codex/2026-10-11/he/work/runtime_carry_routes.json')
world=unreal.EditorLevelLibrary.get_game_world();pawn=unreal.GameplayStatics.get_player_pawn(world,0);pc=unreal.GameplayStatics.get_player_controller(world,0)
def actors(n):
 return list(unreal.GameplayStatics.get_all_actors_of_class(world,unreal.load_class(None,'/Game/ExoLuna/Boss/'+n+'.'+n+'_C')))
manager=actors('BP_BossEncounterManager')[0];boss=actors('BP_CrystalGolem')[0]
crystals=sorted(actors('BP_BossCrystal'),key=lambda a:a.get_editor_property('ColorID'))
pedestals=sorted(actors('BP_CrystalPedestal'),key=lambda a:a.get_editor_property('ColorID'))
report=[];start=time.monotonic();index=0;last_change=start
def save(label):
 p=pawn.get_actor_location()
 report.append({'label':label,'elapsed':round(time.monotonic()-start,2),'position':[p.x,p.y,p.z],'holding':pawn.get_editor_property('IsHolding'),'progress':manager.get_editor_property('ActivatedCount'),'boss_health':boss.get_editor_property('Health'),'remaining':manager.get_editor_property('RemainingSeconds'),'health':pawn.get_editor_property('Health'),'pedestals':[p.get_editor_property('Activated') for p in pedestals]})
 out.write_text(json.dumps(report,indent=2))
def pickup(i,yaw):
 pc.set_control_rotation(unreal.Rotator(pitch=0,yaw=yaw,roll=0))
 crystals[i].call_method('INT_Interact',(pawn,));save('pickup_'+str(i))
def drop(i):
 boss.call_method('StartCombat')
 crystals[i].call_method('INT_Drop');pawn.set_editor_property('IsHolding',False);save('drop_'+str(i))
def confirm(i):
 save('completed_'+str(i));boss.call_method('StopCombat')
 if not pedestals[i].get_editor_property('Activated'):raise RuntimeError('Carried crystal did not activate pedestal '+str(i))
manager.call_method('LoseEncounter');manager.call_method('RetryEncounter');boss.call_method('StopCombat');manager.call_method('ClearProjectiles')
save('route_start')
# Actual CharacterMovement input follows each route. Attacks are suppressed to isolate navigation and carrying.
steps=[('walk',(12450,1300)),('pickup',(0,0)),('walk',(12450,0)),('walk',(12450,-1600)),('walk',(15150,-1600)),('walk',(15150,-1450)),('drop',0),('wait',0.8),('act',lambda:confirm(0)),('walk',(15150,-1600)),('walk',(13550,-1600)),('walk',(13550,-1500)),('pickup',(1,0)),('walk',(13550,-1600)),('walk',(15550,-1600)),('walk',(15550,1450)),('walk',(15150,1450)),('drop',1),('wait',0.8),('act',lambda:confirm(1)),('walk',(15550,1450)),('walk',(15550,200)),('pickup',(2,180)),('walk',(15550,1600)),('walk',(12750,1600)),('walk',(12750,1450)),('drop',2),('wait',0.8),('act',lambda:confirm(2)),('act',lambda:save('route_complete'))]
prepared=-1
def tick(dt):
 global index,last_change,prepared
 try:
  if index>=len(steps):unreal.unregister_slate_post_tick_callback(handle);return
  if time.monotonic()-start>115:raise RuntimeError('Route exceeded 115-second test limit')
  kind,value=steps[index]
  if kind=='walk':
   p=pawn.get_actor_location();dx=value[0]-p.x;dy=value[1]-p.y;dist=math.hypot(dx,dy)
   if dist>25:
    pawn.add_movement_input(unreal.Vector(dx/dist,dy/dist,0),1,False)
    if time.monotonic()-last_change>20:raise RuntimeError('Blocked route waypoint '+str(value))
    return
   pawn.get_editor_property('CharacterMovement').stop_movement_immediately();save('waypoint_'+str(value))
  elif kind in ['pickup','drop']:
   if prepared!=index:
    prepared=index
    if kind=='pickup':
     i,yaw=value;c=crystals[i].get_editor_property('Cube').get_world_location();cam=pawn.get_editor_property('FollowCamera').get_world_location();delta=c-cam
     pc.set_control_rotation(unreal.Rotator(pitch=math.degrees(math.atan2(delta.z,math.hypot(delta.x,delta.y))),yaw=math.degrees(math.atan2(delta.y,delta.x)),roll=0))
    else:boss.call_method('StartCombat')
    save('await_native_'+kind+'_'+str(value))
   held=pawn.get_editor_property('IsHolding')
   if (kind=='pickup' and not held) or (kind=='drop' and held):return
   if kind=='pickup':pc.set_control_rotation(unreal.Rotator(pitch=0,yaw=value[1],roll=0))
   save('native_'+kind+'_'+str(value))
  elif kind=='wait':
   if time.monotonic()-last_change<value:return
  else:value()
  index+=1;last_change=time.monotonic()
 except Exception:
  report.append({'error':traceback.format_exc(),'step':index});out.write_text(json.dumps(report,indent=2));unreal.unregister_slate_post_tick_callback(handle)
handle=unreal.register_slate_post_tick_callback(tick)
