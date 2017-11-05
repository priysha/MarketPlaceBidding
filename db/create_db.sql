CREATE TABLE `bid` (
  `bid_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Bid ID',
  `project_id` int(11) NOT NULL COMMENT 'Project ID of the project for which this bid is put',
  `bid_amount` float NOT NULL COMMENT 'Bidding amount, can be hourly or fixed ',
  `buyer_id` varchar(45) NOT NULL COMMENT 'User ID of the buyer who put this bid',
  `creation_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'The time when this bid was made',
  `bid_type` varchar(45) NOT NULL COMMENT 'Type of bid, can be hourly or fixed',
  `bid_hours` int(11) DEFAULT NULL COMMENT 'If bid type is hourly, this is needed to calculate bid amount',
  PRIMARY KEY (`bid_id`,`buyer_id`,`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

CREATE TABLE `buyer` (
  `buyer_id` varchar(45) NOT NULL COMMENT 'Buyer ID',
  `first_name` varchar(45) DEFAULT NULL COMMENT 'First name of the buyer',
  `last_name` varchar(45) DEFAULT NULL COMMENT 'Last name of the buyer',
  `location` varchar(45) DEFAULT NULL COMMENT 'Location of the buyer',
  `skills` varchar(45) DEFAULT NULL COMMENT 'Skills of the buyer',
  `creation_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Datetime when the buyer was created',
  PRIMARY KEY (`buyer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `seller` (
  `seller_id` varchar(45) NOT NULL COMMENT 'Seller ID',
  `first_name` varchar(45) NOT NULL COMMENT 'First name of the seller',
  `last_name` varchar(45) DEFAULT NULL COMMENT 'Last name of the seller',
  `location` varchar(45) DEFAULT NULL COMMENT 'Location of the seller',
  `job_title` varchar(100) DEFAULT NULL COMMENT 'Job title of the seller',
  `company` varchar(45) DEFAULT NULL COMMENT 'Company of the seller',
  `creation_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Datetime when the seller is created',
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Project ID',
  `project_name` varchar(45) NOT NULL COMMENT 'Name of the project',
  `location` varchar(45) DEFAULT NULL COMMENT 'Location specified for the project',
  `bid_end_time` datetime NOT NULL COMMENT 'The time when bidding for this project ends',
  `seller_id` varchar(45) NOT NULL COMMENT 'User ID of the seller who posted this project',
  `buyer_id` varchar(45) DEFAULT NULL COMMENT 'User ID of the buyer who finally got the project.',
  `description` varchar(255) DEFAULT NULL COMMENT 'Description of the project',
  `creation_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT 'Date when the project is first posted',
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
