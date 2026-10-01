# usage: python3 -I build_tex.py spec.json out.tex
import json, os, re, sys

SPECIALS = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
            '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}

def esc(t):
    return ''.join(SPECIALS.get(c, c) for c in t)

def fmt(t):  # escape, then turn **x** into \textbf{x}
    parts = re.split(r'\*\*(.+?)\*\*', t)
    return ''.join(esc(p) if i % 2 == 0 else r'\textbf{' + esc(p) + '}' for i, p in enumerate(parts))

def title(t):  # names and role lines: ' | ' becomes $|$
    return esc(t).replace(' | ', ' $|$ ')

def row(a, b, c, d):
    return r'\row{%s}{%s}{%s}{%s}' % (a, b, c, d)

def bullets(items):
    return [r'\bstart'] + [r'\bi{%s}' % fmt(b) for b in items] + [r'\bend']

def link(text, url):
    if not text:
        return ''
    return r'\href{%s}{\underline{%s}}' % (url, esc(text))

spec = json.load(open(sys.argv[1], encoding='utf-8'))
here = os.path.dirname(os.path.abspath(__file__))
template = open(os.path.join(here, 'template.tex'), encoding='utf-8').read()
preamble = template.split(r'\begin{document}')[0]

L = [preamble.rstrip(), r'\begin{document}', r'\begin{center}',
     r'{\LARGE\bfseries %s}\\[3pt]' % esc(spec['name'])]
hdr = r'{\footnotesize %s $\bullet$' % esc(spec['phone'])
hdr += '\n' + r'\href{mailto:%s}{%s}' % (spec['email'], esc(spec['email']))
for l in spec['links']:
    hdr += r' $\bullet$' + '\n' + r'\href{%s}{%s}' % (l['url'], esc(l['label']))
hdr += r'}\\[3pt]'
L += [hdr, r'{\small\bfseries\color{accent} %s}' % title(spec['role']),
      r'\end{center}', r'\vspace{-8pt}', '']

def summary():
    return [r'\section{Summary}', r'{\small %s}' % fmt(spec['summary']), '']

def education():
    rows = [row(esc(e['school']), esc(e['loc']), esc(e['degree']), esc(e['date'])) for e in spec['education']]
    return [r'\section{Education}', (r'\\[2pt]' + '\n').join(rows), '']

def skills():
    out = [r'\section{Technical Skills}', r'\begin{itemize}[leftmargin=0em,label={},itemsep=1pt]']
    out += [r'  \item \textbf{%s:} %s' % (esc(s['label']), esc(s['items'])) for s in spec['skills']]
    return out + [r'\end{itemize}', '']

def projects():
    out = [r'\section{Projects}', '']
    for p in spec['projects']:
        out.append(row(title(p['name']), '', esc(p['meta']), link(p.get('link', ''), p.get('url', ''))))
        out += bullets(p['bullets']) + ['']
    return out

def experience():
    out = [r'\section{Experience}']
    for x in spec['experience']:
        out.append(row(esc(x['org']), esc(x['loc']), esc(x['title']), esc(x['date'])))
        out += bullets(x['bullets'])
    return out + ['']

L += summary() + education() + skills()
L += (experience() + projects()) if spec.get('experience_first') else (projects() + experience())
L += [r'\end{document}', '']
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', sys.argv[2])
