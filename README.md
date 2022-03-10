# Pururin
[![Testing](https://github.com/sinkaroid/pururin/actions/workflows/test.yml/badge.svg)](https://github.com/sinkaroid/pururin/actions/workflows/test.yml)   
Pururin unofficial API wrapper  
The official pururin is not providing any API and uses javascript, scrape strategy is not really helps

## Features

- Covers the most paths
- Fully documented and tested.
- Fancy featureful

## Installation

`pip install pururin`

## Documentation
The documentation can be found [https://sinkaroid.github.io/pururin](https://sinkaroid.github.io/pururin)

- ### get_book(options)
    - Gets the specific book by providing the Id

- ### get_random()
    - Gets random doujin on pururin

- ### get_random_with_query(options)
    - Gets random doujin on pururin by query

- ### search_by_highest_rated(options)
    - Returns list of doujinshi based on highest rated

- ### search_by_most_popular(options)
    - Returns list of doujinshi based on most popular

- ### search_by_most_viewed(options)
    - Returns list of doujinshi based on most viewed

- ### search_by_newest(options)
    - Returns list of doujinshi based on newest

- ### search_by_random(options)
    - Returns list of doujinshi based on random

- ### search_by_title(options)
    - Returns list of doujinshi based on title sort

## Quick example

```py
import asyncio
import pururin

async def search():
    doujin = pururin.Client()
    data = doujin.get_book(61119)
    print(data)

async def get():
    await asyncio.gather(search())

asyncio.run(get())
```

## Results
`get` method will represent as **Book Object**

```js
{
    "id": "61119",
    "images": [
        "https://cdn.pururin.to/assets/images/data/61119/1.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/2.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/3.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/4.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/5.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/6.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/7.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/8.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/9.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/10.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/11.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/12.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/13.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/14.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/15.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/16.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/17.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/18.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/19.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/20.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/21.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/22.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/23.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/24.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/25.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/26.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/27.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/28.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/29.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/30.jpg",
        "https://cdn.pururin.to/assets/images/data/61119/31.jpg"
    ],
    "tags": "Blue Gk Flock Blue Fate Fate Grand Order Collar Garter Belt Gloves Leash Lingerie Long Gloves Stockings Doujinshi Gudao Jeanne Alter English xinsu C94 ",
    "title": "Reiju mo Nashi ni Jeanne Alter ga Hatsujou Suru Wake ga Nai",
    "total": "31",
    "type": ".jpg"
}
```
`search` method will represent as **List Object**
```js
[
    {
        "id": "1228",
        "lang_and_total": "English, 15 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Dack Hokkai No Kotou Chira Chira - Twitching Pixies"
    },
    {
        "id": "33904",
        "lang_and_total": "English, 23 pages",
        "sort_by": "most-popular",
        "title": "-Chijoku no Majo Jeanne Alter- Fukujuu Maryoku Kyoukyuu  --"
    },
    {
        "id": "36328",
        "lang_and_total": "English, 34 pages",
        "sort_by": "most-popular",
        "title": "Lily or Jeanne, Who Is the Ace?"
    },
    {
        "id": "33873",
        "lang_and_total": "English, 26 pages",
        "sort_by": "most-popular",
        "title": "Okusuri Kyouiku Jeanne - Kyousei Maryoku Kyoukyuu"
    },
    {
        "id": "36434",
        "lang_and_total": "English, 26 pages",
        "sort_by": "most-popular",
        "title": "Ichaicha Jeanne-san"
    },
    {
        "id": "54509",
        "lang_and_total": "English, 7 pages",
        "sort_by": "most-popular",
        "title": "I Own a Voluptuous Pregnant Jeanne"
    },
    {
        "id": "54290",
        "lang_and_total": "English, 5 pages",
        "sort_by": "most-popular",
        "title": "Jeanne to Issho ni Training"
    },
    {
        "id": "57520",
        "lang_and_total": "English, 29 pages",
        "sort_by": "most-popular",
        "title": "DOSUKEBE. FGO!! Vol. 02 Mizugi Jeanne Hen  DOSUKEBE. FGO!! Vol.02"
    },
    {
        "id": "49974",
        "lang_and_total": "English, 149 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Mama"
    },
    {
        "id": "38429",
        "lang_and_total": "English, 31 pages",
        "sort_by": "most-popular",
        "title": "C9-37 Jeanne Alter-chan to Yuru Fuwa SM  SM"
    },
    {
        "id": "38866",
        "lang_and_total": "English, 30 pages",
        "sort_by": "most-popular",
        "title": "Sapohame Jeanne -Netori no Shou-  --"
    },
    {
        "id": "38865",
        "lang_and_total": "English, 28 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Alter-chan no Deisui Seihai"
    },
    {
        "id": "37367",
        "lang_and_total": "English, 28 pages",
        "sort_by": "most-popular",
        "title": "C9-32 Jeanne Alter-chan to Hatsujou  C9-32"
    },
    {
        "id": "39541",
        "lang_and_total": "English, 73 pages",
        "sort_by": "most-popular",
        "title": "Shounen Jeanne"
    },
    {
        "id": "51205",
        "lang_and_total": "English, 8 pages",
        "sort_by": "most-popular",
        "title": "Sex with Jeanne"
    },
    {
        "id": "55219",
        "lang_and_total": "English, 22 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Alter&#039;s Secret Intentions"
    },
    {
        "id": "55373",
        "lang_and_total": "English, 44 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Alter to Futari no Astolfo  2"
    },
    {
        "id": "39565",
        "lang_and_total": "English, 26 pages",
        "sort_by": "most-popular",
        "title": "Serva Fes no Jeanne no Sodatekata"
    },
    {
        "id": "47226",
        "lang_and_total": "English, 20 pages",
        "sort_by": "most-popular",
        "title": "Jeanne Alter Wants to Transfer Mana!?  !?"
    },
    {
        "id": "54599",
        "lang_and_total": "English, 27 pages",
        "sort_by": "most-popular",
        "title": "Mating earnestly with cat ears Jalter"
    }
]
```

## Legal

This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel like this tool deserves an attribution, mention it.