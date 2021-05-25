# mutual_inf
2文章間の相互情報量計算用ライブラリ. This lib compute on Mutual Information from 2dox relation.
For Report of Information Searching System Class from UT.

## Usage
- Lib import 'import mutual_inf'
- Argument stlucture is here↓
'''
mutual_inf(base, freqA, freqB, freqAB, total, significan)
'''

## Description Args
### Log Setting
- base : Base of 'log' / preset is '10' / type is 'int'

### Words Freqs
- freqA : Word appered freq of doc1 / preset is '1' / type is 'int'
- freqB : Word appered freq of doc2 / preset is '1' / type is 'int'
- freqAB : Words appered freqs of dox1&2 / preset is '1' / type is 'int'
- total : total of dox / preset is '1' / type is 'int'

### Roundding Setting
- significan : 1 ~ 0.1 ~0.00...1 .. Rounding number of digits / preset is '1' / type is 'float'
