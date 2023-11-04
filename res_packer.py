# 注：写的很简单，不支持子文件夹。
from pathlib import Path
import base64, textwrap

TMPL_OUT = '''
RES_INLINE = {
%s
}
'''

TMPL_IN = '''
'%s': base64.b64decode(
%s
),
'''

def load_b64(p: Path, lw: int):
    with open(p, 'rb') as fp:
        dat = base64.b64encode(fp.read())
    txt = ''
    for i in range(0, len(dat), lw):
        txt += repr(dat[i:i+lw])
        txt += '\n'
    return txt[:-1]

in_txt = ''
for p in Path('img').iterdir():
    in_txt += TMPL_IN % (str(p).replace('\\', '/'), textwrap.indent(load_b64(p, 80), ' '*4))

print('import base64')
print(TMPL_OUT % textwrap.indent(in_txt, ' '*4))
