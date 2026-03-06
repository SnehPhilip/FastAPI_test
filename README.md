# FastAPI_test- FILES to execute
      1.FastAPI_Test.ipynb
      2.main.py

# Why API?
### 1. Separation of Concerns (Frontend vs. Backend)
     
    * In the old days, the server handled everything—the data, the logic, and the HTML design.
    * Because we use an API, you can use the same FastAPI backend to power a website, an iPhone app, and an Android app     simultaneously.

### 2. Security and Data Integrity

    * You never want a user's browser to talk directly to your database. That's like giving a customer the keys to your warehouse.
    * The API is the Clerk:Only if Validation,Authorisation is perfect does the API talk to the database.
      
### 3. Machine-to-Machine Communication

    * APIs aren't just for humans using apps.They allow different services to "talk" to each other automatically.
    * Example: When you buy something on a website, the website's API sends a POST request to
      Stripe’s API to process the credit card. Stripe sends a response back, and the website updates your order status.

### 4. Scalability and Efficiency

    *  If your website gets millions of hits, you can "scale" just the API.
    *  You can have 10 servers running your FastAPI code and 1 database * server. Because the API uses standard JSON,
    *  it is incredibly lightweight and fast to transmit over the internet compared to sending entire web pages.
