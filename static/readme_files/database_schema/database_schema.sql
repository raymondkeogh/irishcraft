CREATE TABLE `Product`(
    `SKU` VARCHAR(255) NOT NULL,
    `Name` VARCHAR(255) NOT NULL,
    `Price` DECIMAL(8, 2) NOT NULL,
    `Description` VARCHAR(255) NOT NULL,
    `Category` VARCHAR(255) NOT NULL,
    `Image_url` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Product` ADD PRIMARY KEY `product_sku_primary`(`SKU`);
CREATE TABLE `Category`(
    `name` VARCHAR(255) NOT NULL,
    `friendly_name` VARCHAR(255) NULL
);
ALTER TABLE
    `Category` ADD PRIMARY KEY `category_name_primary`(`name`);
CREATE TABLE `Order`(
    `Order_number` CHAR(255) NOT NULL,
    `Full_name` CHAR(255) NOT NULL,
    `Email` VARCHAR(255) NOT NULL,
    `Phone_number` VARCHAR(255) NOT NULL,
    `Country` CHAR(255) NOT NULL,
    `Postcode` VARCHAR(255) NULL,
    `Town_or_city` CHAR(255) NULL,
    `Street_address_1` CHAR(255) NOT NULL,
    `Street_address_2` CHAR(255) NULL,
    `County` CHAR(255) NULL,
    `Postcode` VARCHAR(255) NULL,
    `Country` VARCHAR(255) NOT NULL,
    `Date` DATETIME NOT NULL,
    `Delivery_cost` DECIMAL(8, 2) NOT NULL,
    `Order_total` DECIMAL(8, 2) NOT NULL,
    `Grand_total` DECIMAL(8, 2) NOT NULL,
    `customer_account` INT NOT NULL
);
ALTER TABLE
    `Order` ADD PRIMARY KEY `order_order_number_primary`(`Order_number`);
CREATE TABLE `OrderLineItem`(
    `Order` CHAR(255) NOT NULL,
    `Product` VARCHAR(255) NOT NULL,
    `Quantity` INT NOT NULL,
    `Lineitem_total` DECIMAL(8, 2) NOT NULL,
    `Product_size` CHAR(255) NULL
);
ALTER TABLE
    `OrderLineItem` ADD PRIMARY KEY `orderlineitem_order_primary`(`Order`);
CREATE TABLE `Customer`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Full_name` VARCHAR(255) NOT NULL,
    `Email` VARCHAR(255) NOT NULL,
    `Phone_number` VARCHAR(255) NULL,
    `Town_or_city` VARCHAR(255) NULL,
    `Street_address_1` VARCHAR(255) NULL,
    `Street_address_2` VARCHAR(255) NOT NULL,
    `County` VARCHAR(255) NULL,
    `Postcode` VARCHAR(255) NULL,
    `Country` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Customer` ADD PRIMARY KEY `customer_id_primary`(`id`);
CREATE TABLE `Review`(
    `title` CHAR(255) NOT NULL,
    `body` TEXT NOT NULL,
    `product` VARCHAR(255) NOT NULL,
    `user` VARCHAR(255) NOT NULL,
    `created` DATETIME NOT NULL,
    `ratings` INT NOT NULL,
    `updated` DATETIME NOT NULL
);
ALTER TABLE
    `Review` ADD PRIMARY KEY `review_title_primary`(`title`);
CREATE TABLE `ProductActivity`(
    `name` VARCHAR(255) NOT NULL,
    `view_count` INT NOT NULL,
    `view_on` DATETIME NOT NULL
);
ALTER TABLE
    `ProductActivity` ADD PRIMARY KEY `productactivity_name_primary`(`name`);
ALTER TABLE
    `OrderLineItem` ADD CONSTRAINT `orderlineitem_product_foreign` FOREIGN KEY(`Product`) REFERENCES `Product`(`SKU`);
ALTER TABLE
    `Product` ADD CONSTRAINT `product_category_foreign` FOREIGN KEY(`Category`) REFERENCES `Category`(`name`);
ALTER TABLE
    `Order` ADD CONSTRAINT `order_customer_account_foreign` FOREIGN KEY(`customer_account`) REFERENCES `Customer`(`id`);
ALTER TABLE
    `Review` ADD CONSTRAINT `review_product_foreign` FOREIGN KEY(`product`) REFERENCES `Product`(`SKU`);
ALTER TABLE
    `Review` ADD CONSTRAINT `review_user_foreign` FOREIGN KEY(`user`) REFERENCES `Customer`(`id`);