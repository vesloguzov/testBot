import numpy
import pysrt

subs = pysrt.open('subs/1.srt')
subs.shift(seconds=2.1)
subs.save('subs/1_+2.1.srt', encoding='utf-8')

print(subs)