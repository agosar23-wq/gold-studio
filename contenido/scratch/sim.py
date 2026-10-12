import sys
from PIL import Image, ImageDraw
names=sys.argv[2:]; outs=[]
for n in names:
    c=Image.open(f'/home/user/gold-studio-final/whatsapp-business/{n}.png').convert('RGB')
    w,h=c.size; band=c.crop((0,(h-800)//2,w,(h+800)//2)).resize((890,371))
    ph=Image.open('/home/user/gold-studio-final/perfil-dorado.png').convert('RGBA').resize((260,260))
    m=Image.new('L',(260,260),0); ImageDraw.Draw(m).ellipse((0,0,259,259),fill=255)
    cv=Image.new('RGB',(890,511),'black'); cv.paste(band,(0,0)); cv.paste(ph,(315,241),m); outs.append(cv)
cols=2; rows=(len(outs)+1)//2
s=Image.new('RGB',(cols*900,rows*521),'white')
for i,o in enumerate(outs): s.paste(o,((i%2)*900,(i//2)*521))
s.save(sys.argv[1])
