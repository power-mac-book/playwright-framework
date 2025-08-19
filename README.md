# Playwright AI Test Automation Framework

🚀 An **AI-powered test automation framework** built with **Playwright, FastAPI, and React**.
This framework enables intelligent test case creation, healing, and management with a modern UI and backend integration.

---

## ✨ Features

* **Playwright POM (Page Object Model)** for clean, maintainable tests
* **AI-assisted test generation** via Monaco-based test studio
* **AI healing logic** for flaky selectors
* **Suite management** and reusable test libraries
* **Visual test run history** (screenshots + logs)
* **Admin panel** for managing tests and suites
* **FastAPI backend** with PostgreSQL for persistent storage
* **Dockerized setup** for easy deployment

---

## 🛠 Tech Stack

* **Frontend**: React + Tailwind + Monaco Editor
* **Backend**: FastAPI + PostgreSQL
* **Testing**: Playwright (TypeScript)
* **AI**: Selector suggestion + healing logic
* **Deployment**: Docker + Docker Compose

---

## 📂 Project Structure

```
.
├── backend/                # FastAPI backend
│   ├── api/                # API routes
│   ├── models/             # DB models (SQLAlchemy)
│   ├── services/           # AI logic & business logic
│   ├── tests/              # API unit tests
│   └── main.py             # FastAPI entrypoint
│
├── frontend/               # React test studio (Monaco-based)
│   ├── src/components/     # UI components
│   ├── src/pages/          # Pages (Dashboard, Test Designer, History)
│   └── src/App.jsx
│
├── playwright-tests/       # Playwright POM tests
│   ├── pages/              # Page objects
│   ├── specs/              # Test specs
│   └── utils/              # Helpers (AI selector healing, logging)
│
├── docker-compose.yml      # Multi-service setup
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo

```sh
git clone https://github.com/your-username/playwright-ai-framework.git
cd playwright-ai-framework
```

### 2. Run with Docker

```sh
docker-compose up --build
```

* Backend: [http://localhost:8000](http://localhost:8000)
* Frontend: [http://localhost:5173](http://localhost:5173)
* PostgreSQL: `localhost:5432`

### 3. Run Playwright tests

```sh
cd playwright-tests
npx playwright test
```

---

## 🧑‍💻 Usage

* Open **Frontend UI** → Create/edit test cases
* Add **steps & selectors** (AI suggestions available)
* Save test → Stored in PostgreSQL via FastAPI
* Run test → Captures screenshots + logs → View results in history

---

## 🧪 Example Test (Login Flow)

```ts
import { test } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('User can login', async ({ page }) => {
  const login = new LoginPage(page);
  await login.goto();
  await login.enterUsername('testuser');
  await login.enterPassword('password123');
  await login.submit();
  await login.expectLoginSuccess();
});
```

---

## 📊 Roadmap

* [ ] CI/CD integration (GitHub Actions)
* [ ] More AI-based test template generation
* [ ] Parallel test execution dashboard
* [ ] Cross-browser visual regression

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](../../issues).

---

## 📜 License

MIT License © 2025


