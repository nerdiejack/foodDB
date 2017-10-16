import pymongo
import datetime
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.fooddb
collection = db.recipes

recipe = {"recipe": {
     "name": "Gemuese-Nudel-Lachs-Salat",
     "ingredients":[
	   {
          "name": "Nudeln",
          "amount": "150",
          "measure_unit": "g",
       },
       {
          "name": "Tomaten",
          "amount": "500",
          "measure_unit": "g",
       },
       {
          "name": "Bohnen",
          "amount": "200",
          "measure_unit": "g",
       },
       {
          "name": "Aubergine",
          "amount": "1",
          "measure_unit": "",
       },
       {
          "name": "Zucchini",
          "amount": "1",
          "measure_unit": "",
       },
       {
          "name": "Olivenoel",
          "amount": "4",
          "measure_unit": "EL",
       },
       {
          "name": "trockener Vermouth",
          "amount": "100",
          "measure_unit": "ml",
        },
        {
          "name": "Butter",
          "amount": "2",
          "measure_unit": "EL",
        },
        {
          "name": "Lachsfilet",
          "amount": "300",
          "measure_unit": "g",
        },
        {
          "name": "Chiliflocken",
          "amount": "0.5",
          "measure_unit": "TL",
        },
        {
          "name": "Petersilie",
          "amount": "4",
          "measure_unit": "Stiele",
        },
        {
          "name": "Oliven",
          "amount": "60",
          "measure_unit": "g",
        },
        {
          "name": "Zitronensaft",
          "amount": "6",
          "measure_unit": "EL",
        },
        {
          "name": "Salz",
          "amount": "1",
          "measure_unit": "Prise",
        },
        {
          "name": "Pfeffer",
          "amount": "1",
          "measure_unit": "Prise",
        }
      ]
     }}

recipes = db.recipes
recipe_id = recipes.insert_one(recipe).inserted_id

pprint.pprint(recipes.find_one({"recipe.name": "Couscous-Gemuese-Salat"}))
