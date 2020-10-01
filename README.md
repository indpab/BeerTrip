# BeerTrip #



* To solve the Beer Travel Challenge, I used the Travelling Salesperson Problem (TSP) approach. Used minimisation of the distance between two breweries with several additional criterias.



### To start the Beer Journey: ###
```
python main.py -lat 0.0 lon -0.0
```

### Required python libraries: ###
- numpy
- pandas
- os
- random
- argparse
- sys
- getopt
- time
- math
- itertools
- csv


### Calculation example ###
```
python main.py -lat 51.742503 -lon 19.432956
Latitude:  51.742503
Longitude: 19.432956
Updating distance matrix...
Matrix update lasted: 3.31 sec
Planning route:
Total distance travelled 214.24 km
Total distance travelled 321.87 km
Total distance travelled 515.83 km
Total distance travelled 626.34 km
Total distance travelled 714.64 km
Total distance travelled 800.11 km
Total distance travelled 842.06 km
Total distance travelled 995.39 km
Total distance travelled 1023.49 km
Total distance travelled 1099.27 km
Total distance travelled 1111.36 km
Total distance travelled 1148.78 km
Total distance travelled 1210.51 km
Total distance travelled 1230.50 km
Total distance travelled 1252.16 km
Total distance travelled 1260.59 km
Total distance travelled 1262.17 km
Total distance travelled 1263.76 km
Total distance travelled 1288.56 km
Route planned. Collecting beer...
Found 21 breweries:
   0 HOME                                                    :  51.742503 ,  19.432956,    0 km
 307 Browar Okocim                                           :  49.962200 ,  20.600300,  214 km
 309 Browar Zywiec                                           :  49.662201 ,  19.174200,  107 km
 995 Pivovar Starobrno                                       :  49.191101 ,  16.591801,  193 km
 958 Ottakringer Brauerei AG                                 :  48.213299 ,  16.322901,  110 km
 224 Brauerei Wieselburg                                     :  48.130600 ,  15.138600,   88 km
 211 Brauerei Gss                                            :  47.362499 ,  15.094700,   85 km
 234 Brausttte der Steirerbrau Aktiengesellschaft            :  47.067902 ,  15.441700,   41 km
1115 Schloss Eggenberg                                       :  47.990398 ,  13.923800,  153 km
 210 Brauerei Grieskirchen AG                                :  48.235100 ,  13.829200,   28 km
1202 Stieglbrauerei zu Salzburg GmbH                         :  47.800499 ,  13.044400,   75 km
 663 Hofbru Kaltenhausen Salzachtal                          :  47.694199 ,  13.078400,   12 km
 664 Hofbruhaus Traunstein                                   :  47.869099 ,  12.650500,   37 km
1347 Weissbierbrauerei Hopf                                  :  47.793999 ,  11.831100,   61 km
 205 Brauerei Aying Franz Inselkammer KG                     :  47.970600 ,  11.780800,   19 km
1053 Restaurant Isarbru                                      :  48.070801 ,  11.531100,   21 km
 621 Hacker-Pschorr Bru                                      :  48.139099 ,  11.580200,    8 km
1311 Unionsbru Haidhausen                                    :  48.135502 ,  11.600900,    1 km
 972 Paulaner                                                :  48.139099 ,  11.580200,    1 km
 748 Knig Ludwig Schlobrauerei Kaltenberg                    :  48.182598 ,  11.252200,   24 km
   0 HOME                                                    :  51.742503 ,  19.432956,  705 km
Total distance travelled: 1994.397040775653 km
Collected 52 types of beer:
 0: 1634 Urtyp Hell
 1: Alt Munich Dark
 2: Altbairisch Dunkel
 3: BrÃ¤u-Weisse
 4: Celebrator
 5: Columbus Bock
 6: Columbus Pils
 7: Czech Premium Lager
 8: Dark Beer / StiftsbrÃ¤u
 9: Doppelbock Dunkel
10: Edelweiss Dunkel Weissbier
11: Edelweiss HefetrÃ¼b
12: Export-Hell
13: GÃ¶sser
14: Hacker-Pschorr Dunkel Weisse
15: Hacker-Pschorr Hubertus Bock
16: Hacker-Pschorr Original Oktoberfest
17: Hacker-Pschorr Weisse
18: Hacker-Pschorr Weisse Bock
19: Hefe-WeiÃŸbier
20: Hefeweizen
21: Hell
22: Helles Naturtrub
23: Jahrhundert-Bier
24: JÃ¶rger WeiÃŸe Hell
25: Krakus
26: KÃ¶nig Ludwig Dunkel
27: KÃ¶nig Ludwig Weissbier Dunkel
28: KÃ¶nig Ludwig Weissbier Hell
29: O.K. Beer
30: Okocim Porter
31: Oktober Fest - MÃ¤rzen
32: Original Munich Premium Lager
33: Original Oktoberfest
34: Ottakringer Helles
35: Paracelsus Zwickl
36: Paulaner Oktoberfest
37: Porter
38: Salvator
39: Samichlaus Bier 2003
40: Samichlaus Bier 2005
41: Samichlaus Bier 2006
42: Stationsweizen
43: Stiegl GoldbrÃ¤u
44: Stiegl Leicht
45: Unimator
46: Ur-Weisse
47: Urbock 23Â°
48: Weisse
49: Weizengold Dunkel
50: Weizengold Hefefein
51: WeiÃŸe Export / Helle WeÃŸe
Solution time: 14.55 sec
Total time: 17.86 sec

```

By Indrė Pabijonavičiūtė