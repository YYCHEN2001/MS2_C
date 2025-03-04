# Data Overview
## Data Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 794 entries, 0 to 793
Data columns (total 24 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Name       794 non-null    object 
 1   Ti         794 non-null    bool   
 2   V          794 non-null    bool   
 3   Mn         794 non-null    bool   
 4   Fe         794 non-null    bool   
 5   Co         794 non-null    bool   
 6   Ni         794 non-null    bool   
 7   Zr         794 non-null    bool   
 8   Mo         794 non-null    bool   
 9   Sn         794 non-null    bool   
 10  W          794 non-null    bool   
 11  CP         794 non-null    bool   
 12  CM_type    794 non-null    object 
 13  CM_morph   794 non-null    object 
 14  MS2_morph  794 non-null    object 
 15  CP_morph   794 non-null    object 
 16  SSA        794 non-null    float64
 17  C          794 non-null    float64
 18  Cation     794 non-null    object 
 19  Anion      794 non-null    object 
 20  P_low      794 non-null    float64
 21  P_high     794 non-null    float64
 22  CD         794 non-null    float64
 23  Cs         794 non-null    float64
dtypes: bool(11), float64(6), object(7)
memory usage: 89.3+ KB


## Descriptive Statistics for Numerical Columns:
              SSA           C       P_low      P_high          CD           Cs
count  794.000000  794.000000  794.000000  794.000000  794.000000   794.000000
mean    80.228184    3.034005   -0.181360    0.407758    5.675063   642.334388
std    117.581538    1.981020    0.334999    0.233775    6.151714   645.671965
min      1.750000    1.000000   -1.200000   -0.300000    0.100000    14.800000
25%     17.370000    2.000000   -0.100000    0.400000    1.125000   160.000000
50%     39.890000    2.000000    0.000000    0.450000    4.000000   422.500000
75%    100.200000    6.000000    0.000000    0.500000    8.000000   892.050000
max    918.000000    6.000000    0.000000    1.000000   50.000000  4474.100000

## Frequency Distribution for CM_type:
CM_type
0                       395
derived carbon-based    206
G-based                 122
CNF                      43
CNT                      28
Name: count, dtype: int64

## Frequency Distribution for CM_morph:
CM_morph
0             395
3D porous     184
2D             93
3D special     53
1D fibers      48
1D tubes       15
0D QDs          6
Name: count, dtype: int64

## Frequency Distribution for MS2_morph:
MS2_morph
irregular nanoparticles    316
flower-like clusters       164
nanoparticles              152
nanosheets                  76
hollow morph                55
bulk                        31
Name: count, dtype: int64

## Frequency Distribution for CP_morph:
CP_morph
0                  395
supported          238
interconnection     73
embedded            47
coated              41
Name: count, dtype: int64

## Frequency Distribution for Cation:
Cation
K     664
Na     84
H      32
Li     14
Name: count, dtype: int64

## Frequency Distribution for Anion:
Anion
OH     696
SO4     87
SO3      6
Cl       5
Name: count, dtype: int64
