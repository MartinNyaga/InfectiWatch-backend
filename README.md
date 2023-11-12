# README for the InfectiWatch backend

# Table of contents:
 
 1. [Description](#description)
 2. [Access](#access)
 3. [Requirements](#requirements)
 4. [Technologies used](#technologies-used)
 5. [MVP features](#mvp-features)
 6. [Admin Features](#admin-features)
 7. [Acknowledgments](#acknowledgments)
 8. [Contribution](#contribution) 
 9. [License](#license)
 10.[Challenges aced](#challenges-faced)


 # Description:
  This Project is based on Non-communicable disease charity. Our project displays the non-communicable diagnostic analysis, based within the country, and shows the analysis of the statistics within the country.

  Based on the current world trend, we had a look at the common challenges people encounter such as, 
  * Limited access to technology
  * Inadequate health literacy and digital literacy
  * Data privacy and security concerns
  * Lack of interoperability and standardization
  * Cost and resource constraints

Our code aims to address these challenges through the following approaches:
  * Providing users with easily accessible information on various diseases, removing any barriers to access.
  * Educating users on different preventive measures to protect themselves from diseases featured on our website.
  * Facilitating fundraising efforts to support the treatment of less fortunate individuals.
  * Engaging users directly by encouraging them to share their feedback through reviews, allowing for hands-on involvement in improving our project.
   

# Access;
    In order to access the project, kindly click on the link below;
    https://infecti-watch.onrender.com/
# Requirements
- A well functioning laptop, tablet or smarthphone.
- Constant Power Supply.
- A well and stable Internet connection.

# Technologies Used:
- Backend: Django/Flask Python 
- Database: PostgreSQL
- Wireframes: Figma (Should be mobile friendly)
- Testing Framework: ​Jest & Minitests
- Frontend: ReactJs &Redux Toolkit(state management)

  # MVP features
    - Users can create an account and log in. 
    - Users can view a listing of the most prevalent communicable diseases.
    - Users can view areas where the communicable diseases have affected the most
    - Users can view more details about a specific communicable disease
    - Users can view more details about a specific affected area
    - Users can give their reviews of how they’d like to help eradicate the disease in a specific area
    - Users can view a map showing the analysis of communicabke diseases affecting a specifuc area
    - Users can offer donations areas affected by the diseases.

# Admin Features
    - An Admin can create users and add existing users (Change their roles)
    - Perform CRUD operations on communicable diseases.
    - Perform CRUD operations on areas affected by communicable diseases.

# Acknowledgments
    - I want to acknowledge Adam Obare and I Martin Nyaga for the creation of the backend.
    - I also want to acknowledge the following resource for the creation of the backend 
    - Python:

              Django: A high-level Python web framework.
              Flask: A micro web framework for Python.
              SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) for Python.
              FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.10.

# Contribution 
   -Anyone viewing this project is welcomed to contribute to our project to further better our website.Here are some of the guidelines to follow inorder to contribute to our project :
### Getting Started

   1. Fork the repository to your own GitHub account.

   2. Clone the forked repository to your local machine:

   ```bash
   git clone https://github.com/MartinNyaga/InfectiWatch-backend/tree/Development.git 

   Create a new branch for your feature or bug fix:

   git checkout -b feature-name
   
   Make your changes in the codebase.
   Test your changes thorougly to ensure they as expected.
   Commit your changes with a descriptive commit message:
           git commit -m "Add feature or fix bug"
    push your changes to your forked repository:
           git push origin feature-name 
    
    Go to the original repository.

    Create a Pull Request (PR) from your forked repository to the original repository.

    Provide a clear and descriptive title for your PR.

    In the PR description, explain the purpose of your changes and any considerations for the reviewers.

    Wait for feedback from maintainers and make necessary changes if requested.

    Your code will undergo a review process. Make sure to address any comments or concerns raised by the maintainers
   
    Thank you for contributing to our project! Your efforts are greatly appreciated

# License

    MIT License

    Copyright (c) 2023 [InfectiWatch]

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

# Challenges Faced
    * Creating authentication for users so that can access the data and prevent unauthorized users from accessing the data.
    *Designing effective database schemes that are able to handle querying of the data and ensure data is consistent
    *Implementing effective error handling and logging mechanisms is vital for debugging and monitoring. 
    *Thoroughly testing the backend, including unit testing, integration testing, and end-to-end testing, is challenging but crucial for ensuring the reliability of the application.
    *Designing a backend that can handle a growing number of users and increasing data volume is crucial. Scalability challenges may arise when the application experiences a sudden surge in traffic.


    