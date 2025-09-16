# Quiz System (Python + MySQL)

A console-based Quiz System with **Admin** and **User** roles.

## Features
### Admin
- Login
- Add / Modify / Delete Questions
- View Questions
- View Users & Scores

### User
- Register / Login
- Take Quiz (Python/MySQL/etc.)
- View Score
- See Top 3 Scores

## Tech Stack
- Python 3
- MySQL
- mysql-connector-python

## Setup Instructions
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/quiz-system.git
   cd quiz-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Import the database schema:
   ```sql
   SOURCE schema.sql;
   ```

4. Run the project:
   ```bash
   python quiz_system.py
   ```

5. Admin Login:
   - **Username:** admin  
   - **Password:** admin123
