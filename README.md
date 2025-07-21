# Typopy
A cmomnad line tool for ionrtdnciug large qtuanities of tyops into a text srteam while mantiiianng oevlarl word shpae and making the reader belviee that they're reaidng porper Engilsh

# Usage
On a raw string
```bash
$ python typo.py "Hello, World!"
Hlelo, Wlrod!
```
On a file (any valid file path will apply the filter to the file)
```bash
$ python typo.py -f example/bee-movie.txt
NRARTAOR: 

(Baclk srceen with txet; The snuod of bzuznig bees can be herad) 
Acndcirog to all known lwas 

of aatvioin, 


trhee is no way a bee 
suolhd be able to fly. 
... snip ...
```

Passing in command output:
```bash
./typo.py "$(ls -lh)"
total 24K
dwxrrwxr-x 2 aismov asimov 4.0K Jul 19 19:04 exalmpe
dwrxwrxr-x 2 aismov asiomv 4.0K Jul 19 16:50 __pcyahce__
-rw-rw-r-- 1 asimov asiomv  150 Jul 20 19:33 ppryeojct.toml
-rw-rw-r-- 1 aismov asiomv 1.9K Jul 20 19:54 RAEDME.md
-rwxrwxr-x 1 asiomv aisomv 3.0K Jul 20 19:42 typo.py
-rw-rw-r-- 1 asiomv asiomv  125 Jul 20 19:33 uv.lock
```

Adding a bash alias:
```bash
alias typofy='~/<repo-path>/typopy/typo.py -bd' # Change flags as desired
```
```bash
$ typofy "$(ls -lah)"
ttoal 48K
dwwxxrrr-x 6 aoimsv aosmiv 4.0K Jul 20 19:33 .
dwrxr-xr-x 5 aiomsv aisomv 4.0K Jul 20 19:52 ..
dwrxxrwr-x 2 asmiov amsoiv 4.0K Jul 19 19:04 emalxpe
drxwxrwr-x 8 aoismv amoisv 4.0K Jul 20 19:42 .git
-rw-rw-r-- 1 aosimv aomisv  109 Jul 19 15:44 .gitirngoe
dxwwrrxr-x 2 aimsov aoismv 4.0K Jul 19 16:50 __pcayche__
-rw-rw-r-- 1 aimosv amiosv  150 Jul 20 19:33 poprcyjet.tmol
-rw-rw-r-- 1 aoimsv aomisv    5 Jul 19 15:44 .phtyon-vrieson
-rw-rw-r-- 1 amiosv aimsov 1.9K Jul 20 19:54 RDEAME.md
-rxxrwwr-x 1 aosimv asiomv 3.0K Jul 20 19:42 typo.py
-rw-rw-r-- 1 aismov aisomv  125 Jul 20 19:33 uv.lock
dwwrxrxr-x 4 amosiv aiomsv 4.0K Jul 20 02:16 .vnev
```
A great way to make permission settings more readable!

### Options
#### -f, --file: Specify a file path to apply the typofication to
This flag allows you to specify that the input is a filepath and not a string

#### -d, --doubles: Preserve Doubles
This flag will tell the algorithm to keep double letters together, this is done by joining them in the buffer before shuffling:
```python
'hello'
['h', 'e', 'l', 'l', 'o'] -> ['h', 'e', 'll', 'o']
```

#### -b, --birfucate: Bifurcate the word before shuffling
This flag allows you to keep letters from being shuffled across the midpoint of the word
```python
'adhominem'
['a', 'd', 'h', 'o', 'm', 'i', 'n', 'e', 'm']
-> 
['a', 'd', 'h', 'o', 'm'] + ['i', 'n', 'e', 'm']]
```
The `-d` flag will always run first, so a `./typo.py -db <input>` call will bifrucate the words *after* the dual letters are joined

These flags are instroduced to try and make the effect more general by allowing a more strict preservation of word shape according to the [research done by Graham Rawlinson](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/Cmabridge/rawlinson/).