# HiredIn - Job Searching Board

Welcome to **HiredIn**, a comprehensive job search platform designed to connect job seekers and employers seamlessly. Developed by **Oikos**, we aim to create a user-centric experience that empowers job seekers to find their ideal positions and companies to discover top talent efficiently.

## Project Overview

**HiredIn** is a platform for job seekers to explore job opportunities, create standout resumes, schedule interviews, and stay informed on market trends. Our team at Oikos handles the entire development process from UI/UX design to frontend and backend implementation.

## Features

### User Types
- **Client (Job Seekers)**: Access to profile setup and personalized job feeds.
- **Company (Employers)**: Profile creation with company information and job postings.
- **Admin**: Dashboard to monitor user activity, manage content, and maintain the platform.

### Core Pages
- **Login Page**: Secure authentication, including Google Auth.
- **Application Page**: Streamlined job application experience with one-click apply functionality.

### Platform Features
- **Google Authentication**: Simplified login with Google.
- **Portfolio Check**: Verification of user portfolios for credibility.
- **Advanced Search and Filtering**: Refine job searches by location, industry, role, and more.
- **One-Click Apply**: Easy application process for job seekers.
- **Resume Templates**: Built-in tool to create, customize, and download professional resumes.
- **Interview Scheduler**: Schedule interviews directly on the platform, with calendar integration.
- **Job Alerts and Notifications**: Personalized alerts based on user preferences.
- **Job Matching Algorithm**: AI-powered matching to recommend suitable jobs to users.
- **Company and Job Reviews**: User-submitted reviews and ratings for better job selection.
- **Saved Jobs and Applications**: Track favorite job listings and application progress.
- **Salary and Market Trends**: Insights into salary ranges, market trends, and in-demand skills.
- **Job Insights and Analytics**: Stats on job views, application progress, and profile engagement.

## Tech Stack

- **Frontend**: React, Redux, Tailwind CSS
- **Backend**: Python with Django
- **Database**: MySQL
- **UI/UX Design**: Figma (for wireframing and prototyping)
- **Version Control**: Git & GitHub
- **Additional Skills and Tools**:
  - **JWT** for authentication and session management
  - **REST API** development with Django REST Framework
  - **Testing**: Jest (frontend) and Pytest (backend) for test coverage and quality assurance
  - **Deployment**: Docker for containerization and deployment readiness

## Getting Started

### Prerequisites
- Node.js (for frontend development)
- Python 3.x (for backend development)
- MySQL (for database)
- Docker (for containerized deployment)

### Installation
1. Clone the repository.
   git clone https://github.com/oikos/hiredin.git
2. Install frontend dependencies
   cd frontend
   npm install
3. Set up backend environment and install dependencies.
   cd backend
   pip install -r requirements.txt
4. Configure the MySQL database and update environment variables in the .env file.
5. Run migrations and start the development servers.
### Running the Project
- **Frontend:** Run npm start in the frontend folder.
- **Backend:** Run python manage.py runserver in the backend folder.
### Running with Docker
For a Docker-based setup, use:
docker-compose up --build

## Contributing
We welcome contributions from anyone interested in enhancing HiredIn. Feel free to fork this repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.
