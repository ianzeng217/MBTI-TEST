
# MBTI Personality Test Web Application  
*A Flask-based platform for MBTI assessment, insights, and community interaction*  

---

## Table of Contents  
1. [Features](#features)  
2. [Technical Stack](#technical-stack)  
3. [Installation Guide](#installation-guide)  
4. [Project Structure](#project-structure)  
5. [Configuration](#configuration)  
6. [Database Schema](#database-schema)  
7. [API & Data Sources](#api--data-sources)  
8. [Workflow & Development](#workflow--development)  
9. [Testing](#testing)  
10. [Deployment](#deployment)  
11. [Troubleshooting](#troubleshooting)  
12. [Contributing](#contributing)  
13. [License](#license)  

---

## Features  

### Core Functionality  
- **User Authentication**  
  - Secure registration/login with Flask-Login and password hashing.  
  - Session management with persistent user preferences.  

- **MBTI Assessment**  
  - Dynamic 60-question quiz with real-time progress tracking.  
  - Algorithm:  
    - Scoring based on [Myers-Briggs dichotomies](https://www.myersbriggs.org/).  
    - Result calculation using `(E-I, S-N, T-F, J-P)` axis comparisons.  

- **Personality Insights**  
  - **Type Details**: In-depth profiles for all 16 MBTI types (strengths, weaknesses, career matches).  
  - **Relationships**: Compatibility analysis between types (e.g., `ENFP x INTJ`).  
  - **Characters**: Anime/celebrity personas matching MBTI types (loaded from JSON).  
  - **Animals**: Spirit animals associated with types (e.g., `INFJ = Owl`).  

- **User Dashboard**  
  - Saved test history with timestamps.  
  - Favorite insights/characters bookmarking.  

### Advanced Features  
- **Dynamic UI Components**  
  - Interactive SVGs for MBTI dimension visualization.  
  - Swiper.js carousels for animal/character displays.  
  - Real-time compatibility percentage animations.  

- **Data Management**  
  - External JSON integration for character/animal data (hosted on GitHub).  
  - Caching mechanism for frequently accessed MBTI metadata.  

---

## Technical Stack  

### Backend  
- **Framework**: Flask 2.0+  
- **Database**: SQLite (Development), PostgreSQL (Production)  
- **ORM**: Flask-SQLAlchemy  
- **Authentication**: Flask-Login + Werkzeug Security  
- **API**: RESTful endpoints for data fetching  

### Frontend  
- **Templating**: Jinja2  
- **Styling**: CSS3 with CSS Variables + Mobile-First Design  
- **Interactivity**: Vanilla JavaScript + Swiper.js  
- **Animations**: Custom CSS keyframes + Intersection Observer API  

### DevOps  
- **Version Control**: Git + GitHub  
- **Dependency Management**: `requirements.txt`  
- **Deployment**: Docker + Gunicorn (Production)  

---

## Installation Guide  

### Prerequisites  
- Python 3.8+  
- Node.js (for optional Sass compilation)  

### Step-by-Step Setup  

```bash
# 1. Clone Repository  
git clone https://github.com/ianzeng217/MBTI-TEST.git  
cd mbti_checker  

# 2. Create Virtual Environment  
python -m venv venv  
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  

# 3. Install Dependencies  
pip install -r requirements.txt  

# 4. Database Initialization  
flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade  

# 5. Configure Environment Variables  
cp .env.example .env  
# Edit .env with your secrets (SECRET_KEY, DATABASE_URL, etc.)  

# 6. Run Development Server  
flask run --debug  
```

Access at: `http://localhost:5000`  

---

## Project Structure  

```plaintext
mbti_checker/  
├── app/  
│   ├── __init__.py          # Flask app factory  
│   ├── models.py            # SQLAlchemy models (User, Result)  
│   ├── routes.py            # All application routes  
│   ├── forms.py             # WTForms for registration/login  
│   └── utils/               # Helper functions  
│       ├── mbti_calculator.py  
│       └── data_loader.py  
│  
├── templates/               # Jinja2 templates  
│   ├── base.html            # Master template  
│   ├── index.html           # Landing page  
│   ├── quiz.html            # MBTI quiz interface  
│   ├── insights.html        # Type analysis (shown in user's question)  
│   ├── relationships.html   # Compatibility checker  
│   ├── characters.html      # Anime/celebrity MBTI matches  
│   └── animals.html         # Animal representations  
│  
├── static/  
│   ├── css/                 # Compiled CSS  
│   ├── js/                  # Custom scripts  
│   ├── mbti/                # MBTI type icons (INTJ.png, etc.)  
│   ├── Animals_MBTI/        # Animal images per type  
│   └── Anime_MBTI/          # Character images  
│  
├── migrations/              # Database migration scripts  
├── config.py                # Flask configuration  
├── requirements.txt         # Python dependencies  
└── README.md  
```

---

## Configuration  

### Key Environment Variables (`.env`)  
```ini
SECRET_KEY=your-secure-key-here  
DATABASE_URL=sqlite:///site.db  
DEBUG=True  # Set to False in production  
MBTI_DATA_URL=https://raw.githubusercontent.com/.../data.json  
```

### Flask Settings (`config.py`)  
- **Session Lifetime**: `PERMANENT_SESSION_LIFETIME = 7` (days)  
- **File Uploads**: `MAX_CONTENT_LENGTH = 16 * 1024 * 1024` (16MB)  

---

## Database Schema  

### `User` Model  
| Column          | Type        | Description                     |  
|-----------------|-------------|---------------------------------|  
| id              | Integer     | Primary key                     |  
| username        | String(20)  | Unique, not nullable            |  
| email           | String(120) | Unique, not nullable            |  
| password_hash   | String(128) | Hashed via Werkzeug             |  
| mbti_type       | String(4)   | Nullable, updated after quiz    |  

### `Result` Model  
| Column          | Type        | Description                     |  
|-----------------|-------------|---------------------------------|  
| id              | Integer     | Primary key                     |  
| mbti_result     | String(4)   | E.g., 'INFJ'                    |  
| timestamp       | DateTime    | Default=datetime.utcnow         |  
| user_id         | Integer     | ForeignKey('user.id')           |  

---

## API & Data Sources  

### External Data Integration  
- **Characters**: Fetched from [`charecter.json`](https://github.com/.../charecter.json)  
  ```json
  {
    "purpleHouse": {
      "types": {
        "INTJ": {
          "characters": [
            {"name": "Lelouch Lamperouge", "anime": "Code Geass", "traits": {...}}
          ]
        }
      }
    }
  }
  ```
- **Animals**: Loaded from [`animals.json`](https://github.com/.../animals.json)  

---

## Workflow & Development  

### Feature Branch Workflow  
1. Create a new branch:  
   ```bash
   git checkout -b feature/new-insights-page
   ```
2. Develop locally and test:  
   ```bash
   flask run --debug
   ```
3. Commit changes:  
   ```bash
   git add .  
   git commit -m "Add new insights page with interactive charts"
   ```
4. Push to GitHub and create PR.  

### Code Style  
- Follow **PEP 8** for Python.  
- Use **BEM naming convention** for CSS.  
- JavaScript: ES6+ with modular patterns.  

---

## Testing  

### Manual Testing Checklist  
1. User registration/login flow  
2. MBTI quiz result accuracy  
3. Data persistence across sessions  
4. Mobile responsiveness  

### Automated Tests (Example)  
```python
# tests/test_auth.py  
def test_user_registration(client):  
    response = client.post('/register', data={  
        'username': 'testuser',  
        'email': 'test@example.com',  
        'password': 'securepassword123'  
    })  
    assert response.status_code == 302  # Redirect on success  
```

Run tests:  
```bash
python -m pytest tests/
```

---

## Deployment  

### Production Setup with Docker  
```Dockerfile
FROM python:3.9-slim  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY . .  
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]  
```

Build and run:  
```bash
docker build -t mbti-app .  
docker run -d -p 5000:5000 --env-file .env mbti-app  
```

---

## Troubleshooting  

### Common Issues  
| Symptom                  | Solution                          |  
|--------------------------|-----------------------------------|  
| "Database locked" error  | Delete `instance/site.db` + rerun migrations |  
| Missing static files     | Check `static/` directory permissions |  
| JSON fetch errors        | Verify CORS headers on GitHub data files |  

---

## Contributing  

1. Fork the repository.  
2. Add tests for new features.  
3. Update documentation in `/docs`.  
4. Submit PR with detailed description.  

---

## License  
MIT License - See [LICENSE](LICENSE) for details.  
