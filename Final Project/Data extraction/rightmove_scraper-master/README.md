# Rightmove property data scraper

Install the requirements in requirements.txt

To use, simply run scrape.py, passing in some command line arguments:

`-l` for input location, such as Twickenham (if searching a place name) or TW1 (the first part of a postcode)    
`-p` to indicate if the input location is a postcode (true, false)  
`-r` for search radius in miles (only works if not a postcode). Defaults to 1.0.  
`-s` to indicate if you wish to return properties for sale or for rent (sale, rent). Defaults to sale.  

## Example usage

To get all properties within 2.0 miles of Twickenham station:  

```bash
python scrape.py -l "Twickenham station" -p false -s sale -r 2.0
```

Note : I wrapped "Twickenham station" in quotes because there is a space in the string and argparser 
thinks it's a list of 2 strings without the quotes. If it's just a single word string, then you can omit them.  

To get all properties for rent in N1  

```bash
python scrape.py -l N1 -p true -s rent
```


## Output data

The retrieved properties will be saved in to the output directory as JSON files.  

