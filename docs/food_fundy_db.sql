-- Create Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_username VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_phone VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_address VARCHAR(255) NOT NULL,
    user_type ENUM('user', 'admin', 'chief') NOT NULL,
    user_notes TEXT,
    user_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Categories table
CREATE TABLE Tags (
    tag_id INT PRIMARY KEY AUTO_INCREMENT,
    tag_name VARCHAR(255) NOT NULL,
    tag_notes TEXT,
    tag_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Categories table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    category_type ENUM('Main', 'Secondary') NOT NULL,
    category_image VARCHAR(255),
    category_notes TEXT,
    category_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Meals table
CREATE TABLE Meals (
    meal_id INT PRIMARY KEY AUTO_INCREMENT,
    meal_name VARCHAR(255) NOT NULL,
    meal_category INT,
    meal_tag INT,
    meal_notes TEXT,
    meal_image VARCHAR(255),
    meal_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Create Ingredients table
CREATE TABLE Ingredients (
    ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
    ingredient_category INT,
    ingredient_name VARCHAR(255) NOT NULL,
    ingredient_type ENUM('Main', 'Secondary') NOT NULL,
    ingredient_notes TEXT,
    ingredient_date DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Create Devices table
CREATE TABLE Devices (
    device_id INT PRIMARY KEY AUTO_INCREMENT,
    device_name VARCHAR(255) NOT NULL,
    device_notes TEXT,
    device_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create MealsIngredients table to represent the many-to-many relationship between Meals and Ingredients
CREATE TABLE MealsIngredients (
    mi_id INT PRIMARY KEY AUTO_INCREMENT, 
    mi_meal_id INT, 
    mi_ingredient_id INT,
    mi_device_id INT,
    FOREIGN KEY (mi_meal_id) REFERENCES Meals(meal_id),
    FOREIGN KEY (mi_ingredient_id) REFERENCES Ingredients(ingredient_id),
    FOREIGN KEY (mi_device_id) REFERENCES Devices(device_id)
);

-- Create UserMeals table to represent the relationship between Users and Meals
CREATE TABLE UserMeals (
    um_id INT PRIMARY KEY AUTO_INCREMENT,
    um_user_id INT,
    um_meal_id INT,
    FOREIGN KEY (um_user_id) REFERENCES Users(user_id),
    FOREIGN KEY (um_meal_id) REFERENCES Meals(meal_id),
    PRIMARY KEY (um_user_id, meal_id)
);
