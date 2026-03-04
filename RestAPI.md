 let’s look at **REST** as the "philosophy" behind the code.

**REST** stands for **Representational State Transfer**. It is a set of rules that allows two computers to talk to each other over the internet using the same language (HTTP).

---

## 1. The Core Concept: Resources

In a REST API, everything is a **Resource**. A resource could be a user, a photo, or a bank transaction. Each resource is identified by a **URL**.

* **Bad URL:** `/get_user_info?id=10` (Focuses on the action)
* **RESTful URL:** `/users/10` (Focuses on the resource)

---

## 2. The 5 Standard Verbs (HTTP Methods)

Think of these as the "grammar" of your API. They tell the server what you want to do with a resource.

| Method | Action | Example |
| --- | --- | --- |
| **GET** | Read | `GET /items` (List all items) |
| **POST** | Create | `POST /items` (Add a new item) |
| **PUT** | Update (Full) | `PUT /items/1` (Replace item #1 entirely) |
| **PATCH** | Update (Partial) | `PATCH /items/1` (Change only the price of item #1) |
| **DELETE** | Delete | `DELETE /items/1` (Remove item #1) |

---

## 3. The 3 Main Rules of REST

### A. Statelessness

This is the most important rule. The server does **not** remember who you are between requests. Every single request must contain everything the server needs to know (like an API token or a User ID). It’s like a waiter who forgets your face every time they walk to the kitchen—you have to show your table number every time you order a drink.

### B. Uniform Interface

No matter what resource you are hitting, the "style" remains the same. You always use JSON, and the way you structure your URLs remains consistent. This makes it easy for other developers to use your API without reading a 500-page manual.

### C. Client-Server Separation

The code for your mobile app (Client) and the code for your database (Server) are totally independent. You could rewrite your entire backend in **FastAPI** after using **Java**, and as long as the URLs and JSON stay the same, the mobile app will never know the difference.

---

## 4. Anatomy of a REST Request

When you make a call to a REST API, you are sending a package that looks like this:

1. **The Endpoint (URL):** `https://api.example.com/v1/users`
2. **The Method:** `POST`
3. **The Headers:** Meta-information (e.g., `Content-Type: application/json`)
4. **The Body:** The actual data (e.g., `{"name": "Sneh", "role": "Engineer"}`)

---

## 5. Standard Status Codes

A REST API uses specific numbers to tell the client what happened:

* **200 OK:** Everything worked.
* **201 Created:** Success! (Usually follows a **POST**).
* **400 Bad Request:** You sent something wrong (the client's fault).
* **401 Unauthorized:** You forgot your "ID card" (API Key).
* **404 Not Found:** That resource doesn't exist.
* **500 Internal Server Error:** The server crashed (the developer's fault).

---

**Would you like to try building a full "CRUD" (Create, Read, Update, Delete) application in FastAPI to see how these REST principles look in a real project?**
