* Project ECO 351 Do File *
* As a note, the data was added manually from the file data.xls *
* Since the data is saved locally it might not be able to be opened through code *
* Data file is title data.dat*

* The regressions are repeated twice to get the adjusted R^2 from the first reg *

clear
use "/Users/al-baraael-hag/Downloads/Korea/data.dta"

* Model 1 *
reg gini lgdp lgdp2
reg gini lgdp lgdp2, r
outreg, se
outreg2 merge


* Model 2 *
reg gini lgdp lgdp2 cpi old unemp
reg gini lgdp lgdp2 cpi old unemp, r
outreg, se merge
outreg2 merge

* Model 3 *
reg gini lgdp lgdp2 cpi old empf
reg gini lgdp lgdp2 cpi old empf, r
outreg, se merge
outreg2 merge

* Model 4 *
reg gini lgdp lgdp2 cpi old unemp lfdi xmy iy gy
reg gini lgdp lgdp2 cpi old unemp lfdi xmy iy gy, r
outreg, se merge
outreg2 merge


* Model 5 *
reg gini lgdp lgdp2 cpi old empf lfdi xmy iy gy
reg gini lgdp lgdp2 cpi old empf lfdi xmy iy gy, r
outreg, se merge
outreg2 merge

* Model 6 *
reg gini lgdp lgdp2 cpi old unemp lfdi iy gy my
reg gini lgdp lgdp2 cpi old unemp lfdi iy gy my, r
outreg, se merge
outreg2 merge

* Model 7 *
reg gini lgdp lgdp2 cpi old empf lfdi iy gy my
reg gini lgdp lgdp2 cpi old empf lfdi iy gy my, r
outreg, se merge
outreg2 merge





