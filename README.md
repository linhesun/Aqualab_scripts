# Aqualab_scripts
Some scripts for daily research in the Aquatic Plant Lab of CNBG.

Author: Linhe Sun

## 1 Duncan test
`duncan.test.aqua.r` and `duncan.test.aqua.withoutrep.r` are duncan test scripts for our lab.They can arrange ANOVA and Duncan test then draw barplots with error bar and significance. They depend two packages in R: `agricolae` and `ggplot2`.

### Usage

Data sample: (Use '\t' as space)
```
Group	Temp	mmHg	DO%L	DO.mg/L	C-uS/cm	SAL.ppt	pH	ORP.mV	TN(mg/L)	NH4+(mg/L)	NO2-(mg/L)	NO3-(mg/L)	TP(mg/L)	Cu2+(ppb)	Zn2+(ppb)	Cd2+(ppb)
CK	29.6	748.2	3.4	0.26	498.4	0.22	9.02	58.6	6.08 	0.54	0.081	1	0.138 	356.20 	666.2	1020.80 
CK	29	748.2	3.1	0.24	482.7	0.21	8.98	62.2	6.36 	0.52	0.057	0.1	0.134 	302.20 	572.6	1062.20 
CK	29.2	748.4	2.9	0.22	489.6	0.22	8.89	70	5.24 	0.8	0.051	0.1	0.141 	387.00 	725	1050.60 
ZDQ	29.9	748.3	4.4	0.33	390.1	0.17	7.97	8.3	2.02 	0	0.058	0	0.028 	61.2	2.6669	25.559
ZDQ	29.8	748.3	4.2	0.31	428	0.19	7.86	94.8	4.47 	0	0.157	0	0.088 	464.2	3275.2	2150.2
ZDQ	29.1	748.3	3.2	0.24	437.4	0.19	8.47	102.4	7.42 	1.11	0.092	1.3	0.092 	435.4	2484.8	2245.4
ZSQ	29.8	748.3	4.3	0.32	429.8	0.19	8.13	43.4	6.80 	0.23	0	1.2	0.092 	340.8	1814.8	1870.4
ZSQ	29.1	748.2	3.5	0.26	377.7	0.17	8.39	94.4	2.41 	0	0	0	0.028 	70.8	206.4	278.8
ZSQ	29.2	748.3	3.2	0.24	425.1	0.19	8.56	92.1	7.15 	0.95	0.134	0.8	0.092 	375.6	1605.2	1775.2
YSQ	29.8	748.3	4.2	0.31	427.3	0.19	8.17	79.3	6.11 	0.29	0.2	1.2	0.100 	539.4	1877.4	1829.6
YSQ	29.3	748.3	4	0.3	425.3	0.19	8.09	99.9	4.87 	0	0	0.1	0.088 	358.2	2159.6	1880.6
YSQ	29.2	748.3	3.1	0.23	423.9	0.19	8.83	79.1	6.70 	0.54	0.085	0.7	0.107 	506.6	1404.8	1557.2
```

`duncan.test.aqua.r` will read multiple data files. But the each files should have the same tests.

`duncan.test.aqua.withoutrep.r` will read only one data file. You need to give a name for the plot.

Use transcripts like this:
```
Rscripts duncan.test.aqua.r data1.txt data2.txt ...
Rscripts duncan.test.aqua.withoutrep.r data1.txt data1.pdf
```
