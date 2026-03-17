# N-tier Architecture 
An N-tier architecture divides an application into logical layers and physical tiers.  
The layers separate responsibilities and manage dependencies. Each layer has a specific  
responsibility. A higher layer can use services in a lower layer, but a lower layer can't   
use services from a higher layer. 

A traditional N-tier application has three layers: the presentation layer, a business tier and a database tier. The more complex the more tiers the application can have. 
The layers: 
* Presentation layer: This layer is responsible for the user interface and user experience. It handles user interactions and displays data to the user.
* Business layer: This layer contains the business logic and rules of the application. It processes data received from the presentation layer and interacts with the data layer to perform operations.
* Data layer: This layer is responsible for data storage and retrieval. It interacts with databases or other data sources to manage the application's data.

An N-tier application can have a closed layer architecture or an open layer architecture.  
* In a closed layer architecture, a layer can only call the next layer immediately down.  
* In a open layer architecture, a layer can call any lower layer.  

A closed layer architecture limits the dependencies between layers. It can create unnecessary  
network traffic if one layer only passes requests along to the next layer.   

## When to use an N-tier architecture
An N-tier architecture is considered a good choice in the following scenarios:  
* Support architectural requirements that are still evolving.  
* Migrate an on-premise application to the cloud. 
* Develop applications that span both on-premise and cloud environments. 

## Benefits    
* Portable across cloud and on-premises, and between cloud platforms
* Requires less learning curve for most developers
* Costs relatively little by not rearchitecting the solution
* Follows a natural evolution from the traditional application model
* Supports mixed environments that include Windows and Linux
* Secure
* Easy to manage
* Scalable 
## Challenges
* A middle tier might only perform basic create, read, update, delete (CRUD) operations, which adds latency and complexity without delivering meaningful value.
* Monolithic design prevents independent deployment of features.
* Large systems can make network security difficult to manage.
* User requests and data that move through multiple tiers make testing and monitoring more difficult.


### Examples
#### E-commerce Web Application
A common example of a 3-tier architecture is a modern online store:

* Presentation Tier: A web interface built with React or Angular where customers browse products and view their shopping cart.
* Business Tier: A backend service (using Node.js or Java) that validates credit card information, calculates shipping costs, and checks warehouse inventory levels.
* Data Tier: A relational database like PostgreSQL that stores the product catalog, customer profiles, and transaction history.

#### Banking System
Another classic implementation found in financial services:

* Presentation Tier: A mobile banking app or an ATM interface used by the customer.
* Business Tier: The core banking logic that handles interest calculations, fraud detection, and authorization of transfers.
* Data Tier: A secure mainframe or database cluster that records all account balances and historical ledger entries.

```code
banking-system/
│
├── README.md
├── docs/
│   ├── architecture.md
│   └── diagrams/
│
├── presentation/
│   ├── web-app/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── main.js
│   │
│   └── mobile-app/
│       ├── screens/
│       ├── services/
│       └── app.js
│
├── business/
│   ├── services/
│   │   ├── account_service.py
│   │   ├── transfer_service.py
│   │   ├── authentication_service.py
│   │   └── fraud_detection_service.py
│   │
│   ├── models/
│   │   ├── account.py
│   │   ├── transaction.py
│   │   └── customer.py
│   │
│   └── validators/
│       ├── account_validator.py
│       └── transaction_validator.py
│
├── data/
│   ├── repositories/
│   │   ├── account_repository.py
│   │   ├── transaction_repository.py
│   │   └── customer_repository.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── migrations/
│   │
│   └── schemas/
│       ├── account_schema.sql
│       ├── transaction_schema.sql
│       └── customer_schema.sql
│
├── api/
│   ├── controllers/
│   │   ├── account_controller.py
│   │   ├── transfer_controller.py
│   │   └── auth_controller.py
│   │
│   └── routes.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── infrastructure/
│   ├── docker/
│   ├── kubernetes/
│   └── terraform/
│
└── config/
    ├── settings.py
    └── logging.py
```