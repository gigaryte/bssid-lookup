# Look up BSSIDs using Apple's Location API


#### Requirements

Requires Python3. 

Install Python dependencies:

```
pip install -r requirements.txt
```

#### Usage

Feed it a newline-delimited file of BSSIDs. Outputs a tab-separated,
newline-delimited file of `Unix Time, BSSID, Geolocation` tuples.
`-180.0,-180.0` indicates that a BSSID was not found in the database

```
./geolocate-bssids.py input_file -o output_file
```
