import base64
f=lambda n: base64.b64encode(open(f'/home/claude/build/fonts/{n}.woff2','rb').read()).decode()
css=(f'@font-face{{font-family:"CMU Serif";font-style:normal;font-weight:400;src:url(data:font/woff2;base64,{f("cmu-serif-500-roman")}) format("woff2")}}'
     f'@font-face{{font-family:"CMU Serif";font-style:italic;font-weight:400;src:url(data:font/woff2;base64,{f("cmu-serif-500-italic")}) format("woff2")}}'
     f'@font-face{{font-family:"CMU Serif";font-style:normal;font-weight:700;src:url(data:font/woff2;base64,{f("cmu-serif-700-roman")}) format("woff2")}}')
open('/home/claude/build/site2/index.html','w').write(open('/home/claude/build/template.html').read().replace('/*FONTS*/',css))
