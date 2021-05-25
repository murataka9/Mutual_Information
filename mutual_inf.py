###### header begin ========================================
## Lib: mutual_inf :: 英意:相互情報量
## ver: 1.0(beta)
## ---------------------------------------------------------
## Auther: Takahito Murakami (kami)
## Auther email: takahito@digitalnature.slis.tsukuba.ac.jp
## twttr: @murataka9 / @takahito_mura
## ---------------------------------------------------------
###### ========================================== header end

import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


def mutual_inf(base=10, freqA:int=1, freqB:int=1, freqAB:int=1, total:int=1, significan:float=1):
  Pab = freqAB / total
  Pa = freqA / total
  Pb = freqB / total

  x = Pab/(Pa * Pb)

  if x == Pab:
    return 0
  else:
    mutual = math.log(x, base)
    return Decimal(str(mutual)).quantize(Decimal(str(significan)), rounding=ROUND_HALF_UP)

# developer memoß
# 四捨五入 quantize() from decimal
# math.log() > e基底
###