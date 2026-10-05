import cadquery as cq, math, os, json, zipfile
out=os.path.dirname(__file__)
W,D=500.5,457.0
mx,my=W/2,D/2

def box(x0,x1,y0,y1,z0,z1):
 return cq.Workplane('XY').box(x1-x0,y1-y0,z1-z0,centered=False).translate((x0,y0,z0)).val()

def tab(cx,cy,axis,clear=0):
 # Dovetail widens toward tip. Male rises into adjoining panel.
 pts=[(-5-clear,-.2-clear),(5+clear,-.2-clear),(7+clear,4+clear),(-7-clear,4+clear)]
 if axis=='x': pts=[(v,u) for u,v in pts]
 return cq.Workplane('XY').polyline([(cx+x,cy+y) for x,y in pts]).close().extrude(5).translate((0,0,15)).val()
parts=[]
for row in range(2):
 for col in range(2):
  x0,x1=(0,mx-.15) if col==0 else (mx+.15,W)
  y0,y1=(0,my-.15) if row==0 else (my+.15,D)
  p=box(x0,x1,y0,y1,15,20)
  holes=[]
  r=8/math.sqrt(3); pitch=10.25
  for i in range(60):
   x=12+i*pitch
   for j in range(60):
    x=12+i*pitch+(j%2)*pitch/2
    y=12+j*pitch*math.sqrt(3)/2
    if x-r>x0+16 and x+r<x1-16 and y-r>y0+16 and y+r<y1-16:
     pts=[(x+r*math.cos(math.radians(30+k*60)),y+r*math.sin(math.radians(30+k*60))) for k in range(6)]
     holes.append(cq.Workplane('XY').polyline(pts).close().extrude(12).translate((0,0,9)).val())
  p=p.cut(cq.Compound.makeCompound(holes))
  p=p.cut(box(x0+16,x1-16,y0+16,y1-16,14,16))
  # Side/rear seating rail reaches glass datum; outside capture skirt drops 3 mm.
  if col==0:
   p=p.fuse(box(0,16,y0,y1,0,15)).fuse(box(0,6,y0,y1,-3,0))
  else:
   p=p.fuse(box(W-16,W,y0,y1,0,15)).fuse(box(W-6,W,y0,y1,-3,0))
  if row==1:
   p=p.fuse(box(x0,x1,D-16,D,0,15))
  else:
   # Front seating rail, without outside retaining skirt; centered handle gap.
   a,b=(x0,mx-63.5) if col==0 else (mx+63.5,x1)
   p=p.fuse(box(a,b,0,10,0,15))
  for yy in [y0+45,y1-45]:
   t=tab(mx,yy,'x',0 if col==0 else .25)
   p=p.fuse(t) if col==0 else p.cut(t)
  for xx in [x0+45,x1-45]:
   t=tab(xx,my,'y',0 if row==0 else .25)
   p=p.fuse(t) if row==0 else p.cut(t)
  p=p.clean()
  assert p.isValid() and len(p.Solids())==1
  name=['Front_Left','Front_Right','Rear_Left','Rear_Right'][row*2+col]
  print_part=p.rotate((0,0,0),(1,0,0),180)
  bb=print_part.BoundingBox()
  print_part=print_part.translate((-bb.xmin,-bb.ymin,-bb.zmin))
  cq.exporters.export(print_part,os.path.join(out,'H2C_TopCover_'+name+'_v1.7.stl'),tolerance=.05,angularTolerance=.15)
  parts.append(p)
  print(name,'valid',p.Volume(),flush=True)
# Universal support: bearing shoulder at Z=16, compliant hex clip through cell.
def hexwire(af,z):
 r=af/math.sqrt(3)
 return cq.Workplane('XY',origin=(0,0,z)).polyline([(r*math.cos(math.radians(30+k*60)),r*math.sin(math.radians(30+k*60))) for k in range(6)]).close().val()
foot=cq.Workplane('XY').circle(10).extrude(2).val()
post=cq.Workplane('XY').circle(3.5).extrude(14).translate((0,0,2)).val()
shoulder=cq.Workplane('XY').circle(6.5).extrude(1.5).translate((0,0,14.5)).val()
clip=cq.Solid.makeLoft([hexwire(7.65,16),hexwire(7.65,19.9),hexwire(8.3,20.25),hexwire(7.5,20.9)],True)
clip=clip.cut(box(-.6,.6,-8,8,16.3,22))
peg=foot.fuse(post).fuse(shoulder).fuse(clip).clean()
center=cq.Workplane('XY').circle(20).extrude(2).val().fuse(cq.Workplane('XY').circle(8).extrude(11).translate((0,0,2)).val()).fuse(cq.Workplane('XY').circle(18).extrude(2).translate((0,0,13)).val()).clean()
for name,solid in [('Honeycomb_Clip_Support',peg),('Center_Junction_Support',center)]:
 assert solid.isValid() and len(solid.Solids())==1
 cq.exporters.export(solid,os.path.join(out,'H2C_TopCover_'+name+'_v1.7.stl'),tolerance=.03,angularTolerance=.15)
 print(name,'valid',flush=True)
print('DONE',flush=True)
