CREATE DATABASE Aroma_Recipes;
USE Aroma_Recipes;
SET SQL_SAFE_UPDATES = 0;

CREATE TABLE Recipes (
	recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_name VARCHAR(255) NOT NULL,
    ingredients TEXT,
    instructions TEXT,
    cuisine VARCHAR(100),
    category VARCHAR(100),
    seasonal VARCHAR(50)
    );
    
INSERT INTO Recipes(recipe_name, ingredients, instructions, cuisine, category, seasonal)
VALUES ('Garlic Parmesan Pasta', '2 tbsps Unsalted Butter, 4 cloves Minced Garlic, 2 cups Chicken Broth, 1 cup Milk, 
8 oz Fettuccine Noodles, Salt, Pepper, 1/4 cup Grated Parmesan Cheese, 2 tbsp Chopped Fresh Parsley', 'Step 1 - Heat unsalted butter in a
large skillet over medium high heat. Add garlic and cook, stirring frequently, until fragrant, about 1-2 minutes. Step 2 - Add in the 
chicken broth, milk, and noodles, season with salt and pepper. Step 3 - Bring the pot to a boil, then reduce heat and simmer, stirring occasionally,
until the pasta is cooked through, about 18-20 minutes. Step 4 - Stir in Parmesan, if it is too thick, add more milk as needed. Step 5 - Serve and top with Parsley.', 'Italian', 'Chicken, Pasta', NULL);


UPDATE Recipes
SET 
    instructions = 'Step 1 - Heat unsalted butter in a large skillet over medium high heat, add garlic and cook, stirring frequently, until fragrant, about 1-2 minutes. Step 2 - Add in the chicken broth, milk, and noodles, season with salt and pepper. Step 3 - Bring the pot to a boil, then reduce heat and simmer, stirring occasionally, until the pasta is cooked through, about 18-20 minutes. Step 4 - Stir in Parmesan, if it is too thick, add more milk as needed. Step 5 - Serve and top with Parsley!'

WHERE recipe_name = 'Garlic Parmesan Pasta';

INSERT INTO Recipes(recipe_name, ingredients, instructions, cuisine, category, seasonal)
VALUES ('Chicken Pot Pie Soup', '1 tbsp Olive Oil, 1 Diced Yellow Onion, 4 stalks Diced Celery, 6 Diced Carrots, 1 Clove Garlic, 3 tbsp Unsalted Butter, 1/4 cup All-Purpose Flour, 2 cups Chicken Stock, 2 cups Half-and-Half, 1 tsp Pepper, 1 tsp Thyme, 1 pinch Ground Nutmeg, 1 cup Frozen Corn, 1 cup Frozen Peas, 1 whole Rotisserie Chicken, Small Baked Rounds of Pie Crust', 'Step 1 - Heat the olive oil in a large pot over medium-high heat, add the onion, celery, carrots, and garlic and cook until onions are translucent, about 5 minutes. Step 2 - Stir in the butter until melted, then add the flour and cook until the flour coats the veggies and browns slightly. Step 3 - Add the chicken stock and half-and-half and stir to combine, season with the black pepper, thyme, and nutmeg, then allow to come to a boil. Step 4 - Reduce the heat to medium-low and add the corn, peas, and chicken, season with salt, cook until warmed through. Step 5 - Ladle the soup into bowls and if desired garnish with small rounds of baked pie crust!', 'English', 'Chicken, Soup, Vegetables,', 'Winter'); 

INSERT INTO Recipes(recipe_name, ingredients, instructions, cuisine, category, seasonal)
VALUES ('Chocolate Strawberry Crepes', '2 cups All Purpose Flour, 3 Eggs, 1/4 cup Melted Butter, 3 tbsp Granulated Sugar, 3 cups Milk, 1/2 cup Hazelnut Spread, 10 Sliced Strawberries, Powdered Sugar', 'Step 1 - In a large bowl, combine flour, eggs, butter, and sugar, stirring until ingredients are slightly mixed. Step 2 - Add the milk 1/2 cup at a time, stirring vigorously, making sure the milk is completely incoporated into the batter and that the batter is smooth before adding more milk. Step 3 - Repeat with the rest of the milk, the batter should be very liquidy and have no lumps. Step 4 - In a pan over medium heat, pour 1/3 cup of the batter in the center and swirl the batter around the edges of the pan until set. Step 5 - To know when the crepe is ready to flip, lift up one of the edges about 1/3 of the way, the bottom should be golden brown, now flip it. Step 6 - Cook until the edges are starting to slightly crisp. Step 7 - Remove from heat and cover with a paper towel to make sure the crepes stay moist. Step 8 - Spread half of the chocolate hazelnut spread on half of the crepe. Step 9 - Lay half of the strawberries on the spread. Step 10 - Fold the other half of the crepe on top of the strawberries, then fold the crepe in half. Step 11 - Repeat with the other crepe and Enjoy!', 'French', 'Chocolate, Strawberry, Dessert', 'Spring, Summer, Fall, Winter' ); 

SELECT * FROM RECIPES;


