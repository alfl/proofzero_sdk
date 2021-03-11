# proofzero_sdk
> A parsing-hasher client to the Proof Zero matching system.


This file will become your README and also the index of your documentation.

## Install

Within your python environment:

```bash
tar -xvf proofzero_sdk.tar.bz2
pip install ./proofzero_sdk
```

## How to use

Import the code into your `.py` file or Jupyter notebook:

```python
import proofzero_sdk.core as pz
```

### Load your data

```python
dir(proofzero)
```




    ['__all__',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'load',
     'pd']



```python
data = pz.load('./data.csv')
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>acct_num</th>
      <th>name</th>
      <th>address</th>
      <th>phone</th>
      <th>SIN</th>
      <th>DOB</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PXCG66212484637575</td>
      <td>Kristin Sanchez MD</td>
      <td>31417 Gina Lodge, Bradleytown, MB P7G 4N5</td>
      <td>1 (598) 742-6794</td>
      <td>203 268 552</td>
      <td>1943-04-15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>XDFZ47399319158654</td>
      <td>Robert Evans</td>
      <td>7156 Tracy Points Suite 587, Perezville, AB M7...</td>
      <td>609 900 6570</td>
      <td>123 827 644</td>
      <td>1991-10-29</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TVNH52405149187504</td>
      <td>Dr. Amy Franklin</td>
      <td>89141 Lopez Lodge Suite 418, Mooremouth, NT M2...</td>
      <td>409-152-0210</td>
      <td>813 208 170</td>
      <td>1962-10-11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WSIK91106311396186</td>
      <td>Donald Sullivan DDS</td>
      <td>05620 Patton Drives, West Susan, NT J1C8S7</td>
      <td>868.610.7617</td>
      <td>335 441 184</td>
      <td>1979-07-09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KTCA56850140109485</td>
      <td>Amanda Rivers</td>
      <td>04050 Johnny Road, East Margaret, PE G4P7H5</td>
      <td>337-707-2813 x982</td>
      <td>238 840 375</td>
      <td>1916-08-23</td>
    </tr>
    <tr>
      <th>5</th>
      <td>JBAQ16782361144059</td>
      <td>John Bush</td>
      <td>764 White Springs Apt. 124, Brandonfurt, YT T6...</td>
      <td>641 411 5627</td>
      <td>815 346 754</td>
      <td>1924-01-23</td>
    </tr>
    <tr>
      <th>6</th>
      <td>SISI84961587433955</td>
      <td>Thierry Hebert</td>
      <td>75, rue Alves, 19169 Moulin</td>
      <td>1 (671) 051-7137</td>
      <td>580 532 836</td>
      <td>1981-02-03</td>
    </tr>
    <tr>
      <th>7</th>
      <td>TBAJ20314253884167</td>
      <td>Mrs. Tracey Collins</td>
      <td>981 Blake Viaduct, Port Courtney, SK A9A 3E7</td>
      <td>+1 (834) 463-5846</td>
      <td>170 346 886</td>
      <td>1913-07-29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>QTRR43030016643496</td>
      <td>Donna Richardson</td>
      <td>854 Lori Villages Apt. 622, North Amandaburgh,...</td>
      <td>356 068 3191</td>
      <td>623 725 041</td>
      <td>1939-10-24</td>
    </tr>
    <tr>
      <th>9</th>
      <td>HJED76191056412385</td>
      <td>Mark Pratt</td>
      <td>15719 Colton Fort, Petermouth, NL A8H 5X3</td>
      <td>106 835 1688</td>
      <td>023 855 612</td>
      <td>1978-08-16</td>
    </tr>
    <tr>
      <th>10</th>
      <td>IUDQ22069678815357</td>
      <td>Philip Chapman</td>
      <td>583 Craig Summit Suite 417, New Aaronchester, ...</td>
      <td>(345) 961-6247 x019</td>
      <td>382 460 129</td>
      <td>2011-07-11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>TAAC54944274450150</td>
      <td>Diane Cohen</td>
      <td>92, boulevard Morel, 64798 LedouxVille</td>
      <td>1-210-341-8687</td>
      <td>540 332 715</td>
      <td>1973-12-17</td>
    </tr>
    <tr>
      <th>12</th>
      <td>CDIE39326969399627</td>
      <td>Mr. Richard Herrera MD</td>
      <td>66183 Duffy Manor, South Eric, BC G5Y 2P2</td>
      <td>264-066-9799</td>
      <td>823 051 735</td>
      <td>1961-03-17</td>
    </tr>
    <tr>
      <th>13</th>
      <td>GGXQ96615961784947</td>
      <td>Michele Shaw</td>
      <td>590 Lane Drives, Lake Susan, NL C9V 5X8</td>
      <td>790-500-3928</td>
      <td>067 551 838</td>
      <td>1923-04-14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>LTEJ93384790637066</td>
      <td>Crystal Camacho</td>
      <td>43533 Joanna Burg Apt. 031, Dianaside, QC A5B4X7</td>
      <td>1 987 643 2231 x431</td>
      <td>825 308 315</td>
      <td>1968-02-03</td>
    </tr>
    <tr>
      <th>15</th>
      <td>QJGU15199846045025</td>
      <td>Denise Hammond</td>
      <td>630 Gina Ports, North Robert, NT K1H5S7</td>
      <td>(560) 922-6004</td>
      <td>673 225 744</td>
      <td>1971-02-17</td>
    </tr>
    <tr>
      <th>16</th>
      <td>EDRT42856525044653</td>
      <td>de Alice Regnier</td>
      <td>6, rue Joseph, 05317 Huet-la-For√™t</td>
      <td>782-176-2155 x263</td>
      <td>126 730 241</td>
      <td>1911-09-17</td>
    </tr>
    <tr>
      <th>17</th>
      <td>YKWB29981978484030</td>
      <td>Teresa Hunt</td>
      <td>627 Andres Isle, Stephenburgh, NU K9B 7H5</td>
      <td>129 967 7011</td>
      <td>384 024 139</td>
      <td>1940-05-01</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PIBF31897897356585</td>
      <td>de Victor Riviere</td>
      <td>chemin Guyot, 82268 Lombard</td>
      <td>1 (722) 081-0754</td>
      <td>653 401 778</td>
      <td>1984-05-29</td>
    </tr>
    <tr>
      <th>19</th>
      <td>UDXE27240828693671</td>
      <td>Emmanuel Imbert</td>
      <td>6, chemin de Torres, 37433 Saint Alice</td>
      <td>+1 (270) 634-2119</td>
      <td>834 607 186</td>
      <td>1979-03-31</td>
    </tr>
    <tr>
      <th>20</th>
      <td>KZYA43304007028308</td>
      <td>Jessica Andrews</td>
      <td>374 Scott Ports, East Ericfurt, PE X8C 6K3</td>
      <td>412.089.5870</td>
      <td>438 710 386</td>
      <td>1937-03-11</td>
    </tr>
    <tr>
      <th>21</th>
      <td>GTZB18751561090354</td>
      <td>Nicholas Saunders</td>
      <td>247 Joshua Ports Apt. 799, Greenshire, NB A2R 5E3</td>
      <td>1 (320) 195-7249</td>
      <td>455 823 864</td>
      <td>1984-03-08</td>
    </tr>
    <tr>
      <th>22</th>
      <td>XIZL94040281781914</td>
      <td>Tiffany Hernandez MD</td>
      <td>1578 Jasmine Heights Suite 588, Gavinton, AB A...</td>
      <td>(563) 162-6738</td>
      <td>306 117 482</td>
      <td>1924-12-21</td>
    </tr>
    <tr>
      <th>23</th>
      <td>LBRO56881851494609</td>
      <td>Matthew Li</td>
      <td>912 Susan Overpass, Lopezbury, NS K5K6P1</td>
      <td>+1 (764) 751-1850</td>
      <td>446 617 086</td>
      <td>1979-11-11</td>
    </tr>
    <tr>
      <th>24</th>
      <td>FSBS28577897962621</td>
      <td>Tracy Dixon</td>
      <td>70198 Ashley Divide, New Brandonstad, NB N8R 6L4</td>
      <td>1 (927) 587 8970 x099</td>
      <td>706 651 445</td>
      <td>1937-01-08</td>
    </tr>
    <tr>
      <th>25</th>
      <td>ZMKN77019320751728</td>
      <td>Robert Greene PhD</td>
      <td>470 Fletcher Centers Suite 352, Lake Christine...</td>
      <td>(423) 724-2131</td>
      <td>076 625 821</td>
      <td>1927-11-18</td>
    </tr>
    <tr>
      <th>26</th>
      <td>BZFX52387922919553</td>
      <td>Miss Molly Moore</td>
      <td>6098 Ford Light, Masonbury, AB M3N8M7</td>
      <td>494-677-4977</td>
      <td>068 722 651</td>
      <td>1936-05-02</td>
    </tr>
    <tr>
      <th>27</th>
      <td>ZIGW09414072902822</td>
      <td>Katrina Vasquez</td>
      <td>414 Dylan View, East Michelle, YT L7V 1S5</td>
      <td>1-130-453-6406 x317</td>
      <td>683 417 406</td>
      <td>1931-01-04</td>
    </tr>
    <tr>
      <th>28</th>
      <td>BGDW87222409297476</td>
      <td>Sandy Miranda</td>
      <td>367 Emily Common Suite 118, West Nathanburgh, ...</td>
      <td>+1 (818) 429-7782</td>
      <td>540 833 225</td>
      <td>1997-10-15</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PGCR37044498095498</td>
      <td>Dr. Sabrina Lewis</td>
      <td>9075 Leach Points Apt. 260, Melindahaven, PE L...</td>
      <td>897-522-4512</td>
      <td>671 188 407</td>
      <td>1943-08-14</td>
    </tr>
    <tr>
      <th>30</th>
      <td>ZFHB41898897817927</td>
      <td>Brandi Matthews</td>
      <td>77667 Melissa Ferry, Jonathanmouth, NB R8C 7X1</td>
      <td>(490) 041-3451</td>
      <td>257 386 078</td>
      <td>1990-12-28</td>
    </tr>
    <tr>
      <th>31</th>
      <td>JMQV76750346118474</td>
      <td>Zachary Carlson</td>
      <td>41264 Garrett Cliff Apt. 584, Thomasside, NS N...</td>
      <td>(508) 681-5345 x766</td>
      <td>762 302 172</td>
      <td>2010-04-18</td>
    </tr>
    <tr>
      <th>32</th>
      <td>MYJW84337436208261</td>
      <td>Rachel Randall</td>
      <td>39550 Melvin Lights, East Charles, MB A6K6V4</td>
      <td>1-349-398-3262</td>
      <td>711 256 644</td>
      <td>2008-12-27</td>
    </tr>
    <tr>
      <th>33</th>
      <td>DCZF81670025464977</td>
      <td>Alexandria Roussel</td>
      <td>83, chemin de Lombard, 45191 Gerard</td>
      <td>(889) 239-0876</td>
      <td>254 768 062</td>
      <td>2009-01-27</td>
    </tr>
    <tr>
      <th>34</th>
      <td>TMLQ40147565532095</td>
      <td>Mr. Timothy Marquez DDS</td>
      <td>831 Amanda Parks Apt. 011, North Madison, BC C...</td>
      <td>702-468-5751</td>
      <td>374 571 040</td>
      <td>1948-05-26</td>
    </tr>
    <tr>
      <th>35</th>
      <td>GRZR41263080377942</td>
      <td>Lorraine Cantu</td>
      <td>7321 Reed Turnpike Suite 076, New Karenport, Y...</td>
      <td>(265) 874-0011</td>
      <td>627 107 162</td>
      <td>1988-10-12</td>
    </tr>
    <tr>
      <th>36</th>
      <td>RGEG96021133730919</td>
      <td>Jason Williams IV</td>
      <td>7271 Tiffany Trafficway Apt. 683, Port Gregory...</td>
      <td>224-647-9524</td>
      <td>852 230 689</td>
      <td>1973-01-10</td>
    </tr>
    <tr>
      <th>37</th>
      <td>TWWO87965954322791</td>
      <td>Craig Young</td>
      <td>646 Wright Summit, Port Scott, NB X4T8P5</td>
      <td>264.014.7743</td>
      <td>652 048 562</td>
      <td>2006-08-07</td>
    </tr>
    <tr>
      <th>38</th>
      <td>TBGD22590615280672</td>
      <td>Mr. Dylan Stephens</td>
      <td>32776 Jose Crest, West Annetteville, NB P5Y 2V7</td>
      <td>1 (329) 969-0227</td>
      <td>882 540 339</td>
      <td>1999-04-01</td>
    </tr>
    <tr>
      <th>39</th>
      <td>HJLW61870218484993</td>
      <td>Gabrielle Wagner</td>
      <td>37, avenue Mallet, 99045 Saint Susannenec</td>
      <td>(114) 528-2190</td>
      <td>526 680 251</td>
      <td>1927-04-01</td>
    </tr>
    <tr>
      <th>40</th>
      <td>DXMN07741514275063</td>
      <td>Megan Martinez</td>
      <td>4311 Brenda Highway Suite 337, New Alyssafort,...</td>
      <td>1956980144</td>
      <td>037 132 172</td>
      <td>1930-12-18</td>
    </tr>
    <tr>
      <th>41</th>
      <td>BKML77357017308394</td>
      <td>Samantha Reed MD</td>
      <td>63200 Jeremy Shoals Suite 770, East Nicole, NB...</td>
      <td>(727) 533 3586 x418</td>
      <td>455 338 806</td>
      <td>1935-09-03</td>
    </tr>
    <tr>
      <th>42</th>
      <td>NNXG67753872628099</td>
      <td>Dr. Jacqueline Marquez</td>
      <td>044 David Hills, Danielsmouth, NS K2M 7K7</td>
      <td>1 (776) 658 3800</td>
      <td>271 076 648</td>
      <td>1949-12-25</td>
    </tr>
    <tr>
      <th>43</th>
      <td>GWQP56763667507927</td>
      <td>de Joseph Roux</td>
      <td>97, avenue Peltier, 28596 Valettenec</td>
      <td>+1 (900) 309-9145</td>
      <td>076 172 162</td>
      <td>1991-03-19</td>
    </tr>
    <tr>
      <th>44</th>
      <td>HWQV21823713722892</td>
      <td>Dr. Gregory Ward</td>
      <td>2279 Adam Rue, Jillmouth, ON V2T8P4</td>
      <td>1 (277) 535-2223</td>
      <td>271 043 747</td>
      <td>1912-05-27</td>
    </tr>
    <tr>
      <th>45</th>
      <td>PEPH75283267953132</td>
      <td>Dr. Cheryl Garcia</td>
      <td>097 Peter Row, Lake Elizabeth, AB B7A8J1</td>
      <td>352.442.6398</td>
      <td>582 605 820</td>
      <td>1931-10-06</td>
    </tr>
    <tr>
      <th>46</th>
      <td>OOCM33770952445286</td>
      <td>Bradley Cox</td>
      <td>70255 Osborne Junction, Francostad, QC G8R9K2</td>
      <td>(992) 455-7811</td>
      <td>042 347 765</td>
      <td>1962-10-10</td>
    </tr>
    <tr>
      <th>47</th>
      <td>LQSB24060947991286</td>
      <td>Janice Schwartz MD</td>
      <td>22494 Moreno Village, West Ashleyberg, PE L9Y4L6</td>
      <td>(332) 602-5142</td>
      <td>130 428 329</td>
      <td>1969-08-07</td>
    </tr>
    <tr>
      <th>48</th>
      <td>JHWS10927634586978</td>
      <td>Stacy Tucker</td>
      <td>8514 Horn Trace Apt. 626, Lake Susanberg, ON M...</td>
      <td>1-174-939-0907</td>
      <td>486 706 815</td>
      <td>1987-03-17</td>
    </tr>
  </tbody>
</table>
</div>


