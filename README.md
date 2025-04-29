**House_Web_Scrapper_Setup**

**description**: Setup instructions for the House Web Scrapper project.

**database**: Your Database Name

**name**: Houses_Scrapper

**table**: Houses_List

**columns**:

address: Address of the house

house_id: Unique ID for the house

price: Price of the house

web_url: URL of the listing

**env_variables**:

DB_HOST: your_host

DB_USER: your_username

DB_PASSWORD: your_password

DB_DATABASE: your_database_name

⚡ Create a .env file in the project root folder and add the above environment variables with your MySQL server details.

**dependencies**:

mysql-connector-python
python-dotenv
requests
bs4

Install all the required dependencies using:

bash: pip install -r requirements.txt

**instructions**:

Create a MySQL database named Houses_Scrapper.

Create a table Houses_List with the columns listed above.

Create a .env file and add your MySQL credentials.

Install required Python libraries with pip install -r requirements.txt.

Run the Python script to start scraping and saving data.

**notes**:

Always use a Python virtual environment (.venv) for dependency management.

Make sure the MySQL server is running and accessible.

Never upload or share your .env file publicly for security reasons.

