# Data Overview
## Data Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 654 entries, 0 to 653
Data columns (total 24 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   Index      654 non-null    int64  
 1   Name       654 non-null    object 
 2   V          654 non-null    bool   
 3   Fe         654 non-null    bool   
 4   Co         654 non-null    bool   
 5   Ni         654 non-null    bool   
 6   Mo         654 non-null    bool   
 7   Sn         654 non-null    bool   
 8   W          654 non-null    bool   
 9   CP         654 non-null    bool   
 10  CM_type    654 non-null    object 
 11  CM_morph   654 non-null    object 
 12  MS2_morph  654 non-null    object 
 13  CP_morph   654 non-null    object 
 14  SSA        654 non-null    float64
 15  C          654 non-null    float64
 16  Cation     654 non-null    object 
 17  Anion      654 non-null    object 
 18  P_low      654 non-null    float64
 19  P_high     654 non-null    float64
 20  CD         654 non-null    float64
 21  Cs         654 non-null    float64
 22  Ref        654 non-null    object 
 23  Ref_index  654 non-null    int64  
dtypes: bool(8), float64(6), int64(2), object(8)
memory usage: 87.0+ KB


## Descriptive Statistics for Numerical Columns:
            Index         SSA           C       P_low      P_high          CD  \
count  654.000000  654.000000  654.000000  654.000000  654.000000  654.000000   
mean   395.304281   70.720651    2.853211   -0.213303    0.390076    5.591896   
std    242.715402  112.527745    1.900233    0.358797    0.249293    6.219731   
min      4.000000    1.750000    1.000000   -1.200000   -0.300000    0.100000   
25%    167.250000   16.640000    2.000000   -0.200000    0.400000    1.000000   
50%    370.500000   39.800000    2.000000    0.000000    0.450000    3.000000   
75%    618.750000   78.385000    3.500000    0.000000    0.500000    8.000000   
max    782.000000  918.000000    6.000000    0.000000    1.000000   50.000000   

                Cs   Ref_index  
count   654.000000  654.000000  
mean    465.193646   41.533639  
std     437.863531   23.548678  
min      14.800000    2.000000  
25%     140.250000   19.000000  
50%     321.350000   42.500000  
75%     665.250000   61.750000  
max    3051.111111   80.000000  

## Frequency Distribution for CM_type:
CM_type
0                       343
derived carbon-based    141
G-based                 105
CNF                      37
CNT                      28
Name: count, dtype: int64

## Frequency Distribution for CM_morph:
CM_morph
0             343
3D porous     114
2D             81
3D special     53
1D fibers      42
1D tubes       15
0D QDs          6
Name: count, dtype: int64

## Frequency Distribution for MS2_morph:
MS2_morph
irregular nanoparticles    236
flower-like clusters       152
nanoparticles              117
nanosheets                  76
hollow morph                49
bulk                        24
Name: count, dtype: int64

## Frequency Distribution for CP_morph:
CP_morph
0                  343
supported          156
interconnection     73
embedded            47
coated              35
Name: count, dtype: int64

## Frequency Distribution for Cation:
Cation
K     536
Na     84
H      20
Li     14
Name: count, dtype: int64

## Frequency Distribution for Anion:
Anion
OH     568
SO4     75
SO3      6
Cl       5
Name: count, dtype: int64
