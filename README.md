# NewScrap: Your Chilean News Scraper API 🌐
[![stability-wip](https://img.shields.io/badge/stability-wip-lightgrey.svg)](https://github.com/mkenney/software-guides/blob/master/STABILITY-BADGES.md#work-in-progress)

NewScrap is a Work-In-Progress (WIP) web scraping project, adept at extracting valuable information from a specific Chilean news website efficiently. This project, aimed as a showcase for my portfolio, is built with Django, Django Rest Framework (DRF), Selenium, and housed in a PostgreSQL container via Docker. NewScrap stands as a reliable, showcasing solution for your news data extraction needs. In its current version, the scraper is tailored to a base newspaper, with plans to extend its capabilities to multiple news platforms.


## 🚀 Features

- **🤖 Dynamic Web Scraping**: Leverage Selenium to navigate, interact, and scrape dynamic web content from the base news platform.
- **🗃 Reliable Data Storage**: PostgreSQL container ensures your data is stored securely and efficiently.
- **🛠 RESTful API**: Access or manage your scraped data programmatically through a DRF powered API.
- **🐳 Docker-Compose Ready**: A single command to spin up your PostgreSQL container and PGAdmin for database management, making setup a breeze.

## 🛠 Getting Started

### Prerequisites

Ensure you have the following installed on your local machine:
- Docker Desktop (macOs/Windows)
- Docker and Docker Compose (Linux)
- Python 3.8+

### Installation

1. **Clone the Repository**:
```bash
git clone https://github.com/javiev/django-selenium-scraper.git
cd django-selenium-scraper
```

2. **Build and Start the PostgreSQL Container and PGAdmin**:
```bash
docker-compose up --build -d
```

Your PostgreSQL database is now running at `127.0.0.1:5432`, and PGAdmin is available at `http://127.0.0.1:80` for database management. Your scraped data is ready to be stored and managed.

### 🔧 Configuration

1. **Update Database Credentials**:
```python
# settings.py
DATABASES = {
    "default": {
        ...
        "USER": "your-username",
        "PASSWORD": "your-password",
        ...
    }
}
```

2. **Customize Docker-Compose Configuration**:
```yaml
# docker-compose.yml
...
      - POSTGRES_USER=your-username
      - POSTGRES_PASSWORD=your-password
...
```

### 🖥 Usage

Utilize the API endpoints to access or manage your data:

- List all scraped data: `http://127.0.0.1:8000/api/scraped-data/`
- Detail of a scraped data item: `http://127.0.0.1:8000/api/scraped-data/<id>/`

### 📖 Documentation

For more detailed documentation, refer to:
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [DRF Documentation](https://www.django-rest-framework.org/)
- [Selenium Documentation](https://www.selenium.dev/documentation/en/)

### 👤 Author

Javier Gómez C