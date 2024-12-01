This is a final project for my COSC 2610 Operating Systems course. Professor: Sokhibjamol Boeva
This project is a "University timetable" application built using Flask and deployed on AWS EC2 with a PostgreSQL database hosted on RDS.
The application allows users to select a level (Undergraduate or Graduate) and view a dynamically generated timetable for courses specific to that level.
It showcases integration of a web framework with a cloud-hosted database, emphasizing full-stack development and cloud deployment principles.

Steps of creation (run all commands on terminal):
1. Signing in to AWS services. Setting up an account.
2. Setting up EC2 Instance, configuring the security groups.
3. Setting up RDS PostgreSQl, ensuring the public access
4. Establishing the connection between personal desktop and the EC2 instance using the terminal command:
ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>
5. Update EC2 and installing all needed dependencies:
sudo apt update
sudo apt install python3 python3-pip postgresql-client -y
6. Connecting to RDS PostgreSQL:
psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>
7. Creating and populating Database Table:
- Creating the "timetable" table:
CREATE TABLE timetable (
    id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    level VARCHAR(20),
    day VARCHAR(20),
    time VARCHAR(20)
);
- Inserting sample course data:
INSERT INTO timetable (course_name, level, day, time)
VALUES
    ('Computer Programming', 'Undergraduate', 'Monday', '4:00 PM'),
    ('College Algebra', 'Undergraduate', 'Wednesday', '2:00 PM'),
    ('Database Concepts', 'Graduate', 'Tuesday', '11:30 PM'),
    ('Network Principles', 'Undergraduate', 'Thursday', '4:20 PM'),
    ('Operating Systems', 'Undergraduate', 'Tuesday', '2:00 PM');
8. Creating project directory and Flask application:
mkdir my_project
cd my_project
touch app.py
Editing app.py and implementing the Flask application with PostgreSQL connection.
9. Creating "templates" folder with index.html and timetable.html files in it and implementing the html code.
10. Setting up python virtual environment:
python3 -m venv venv # to create the virtual environment
source venv/bin/activate # to activate it
11. InstallingpPython dependencies:
- Installing the necessary libraries:
pip3 install --upgrade pip
pip3 install flask psycopg2-binary
12. Running the Flask app:
python app.py
13. Accessing the application:
Opening the browser and accessing the web application on EC2 instance at http://<EC2_Public_IP>:8000.
