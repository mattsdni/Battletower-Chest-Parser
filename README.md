# Intro
This python script parses a .CSV file into a config file for AtomicStryker's Battle Towers mod for minecraft. It's curently designed to work with 1.7.10.


## How to Use

1. Download the python file
2. Create a spreadsheet in [this format](https://docs.google.com/spreadsheets/d/13hXSt2acGLkbz7bva5P-jugv8-TPoXV73KUTWiHxyj8/edit?usp=sharing). Cells can be commented out with the # symbol.
3. When you are done with your config, download it as a .CSV file
4. Rename it to input.csv and put it in the same directory as the python script
5. Run the script and you should get a config.txt file.
6. Open the file and copy the text over to your BattleTowers.cfg

If you are having trouble getting the right item names/meta numbers, make sure you have Not Enough Items installed. Then run the game and open your inventory. Make sure nothing is typed in the search box at the bottom then click on Options in the bottom left. Then go to Tools, Data Dumps. Next to Item Panel, select CSV and click Dump. That will give you a spreadsheet for all the items and their meta in AppData\Roaming\\.minecraft\dumps.
