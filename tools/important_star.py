"""Deterministic native star control, using the existing BAM V2/BC3 codec."""
from pathlib import Path
import hashlib,json,math,struct
from PIL import Image,ImageDraw
from visual_codec import encode_bam

ROOT=Path(__file__).resolve().parents[1]

def star_resources(page):
    images=[]
    for selected in (False,True):
        scale=4;image=Image.new('RGBA',(24*scale,24*scale))
        points=[]
        for n in range(10):
            angle=-math.pi/2+n*math.pi/5;radius=10 if n%2==0 else 4.5
            points.append(((12+radius*math.cos(angle))*scale,(12+radius*math.sin(angle))*scale))
        draw=ImageDraw.Draw(image)
        draw.polygon(points,fill=(246,205,92,255)if selected else (28,25,17,220))
        draw.line(points+[points[0]],fill=(255,231,152,255)if selected else (142,122,76,255),width=scale,joint='curve')
        images.append(image.resize((24,24),Image.Resampling.LANCZOS))
    entries=[];blocks=[];files={}
    for image in images:
        bam,pages=encode_bam(image,page);page+=len(pages)
        count=struct.unpack_from('<I',bam,16)[0];offset=struct.unpack_from('<I',bam,28)[0]
        entries.append(struct.pack('<HHhhHH',24,24,0,0,len(blocks),count))
        blocks.extend(bam[offset+n*28:offset+(n+1)*28]for n in range(count))
        files.update({f'MOS{n:04d}.PVRZ':data for n,data in pages.items()})
    files['BFBSTAR.BAM']=b'BAM V2  '+struct.pack('<6I',2,1,len(blocks),32,56,60)+b''.join(entries)+struct.pack('<HH',2,0)+b''.join(blocks)
    return files,page

def update():
    manifest_path=ROOT/'buffbot/BfBotVA.json';manifest=json.loads(manifest_path.read_text())
    output=ROOT/'buffbot/visual';existing=output/'BFBSTAR.BAM'
    if existing.exists():
        bam=existing.read_bytes();offset=struct.unpack_from('<I',bam,28)[0]
        page=struct.unpack_from('<I',bam,offset)[0]
    else:page=manifest['pageRange'][1]+1
    files,end=star_resources(page)
    for name,data in files.items():(output/name).write_bytes(data)
    manifest['files']=sorted(set(manifest['files'])|set(files))
    manifest['resources']=sum(n.endswith('.BAM')for n in manifest['files'])
    manifest['pageRange'][1]=max(manifest['pageRange'][1],end-1)
    manifest['sha256'].update({n:hashlib.sha256(data).hexdigest()for n,data in files.items()})
    manifest_path.write_text(json.dumps(manifest,indent=2))
    data_path=ROOT/'buffbot/BfBotVD.lua';text=data_path.read_text(encoding='utf-8')
    import re
    text=re.sub(r'\["lastPage"\]=\d+',f'["lastPage"]={end-1}',text)
    data_path.write_text(text,encoding='utf-8')

if __name__=='__main__':update()
