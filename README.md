# Proyecto Final - Automation Testing

## Proposito del proyecto

Framework de automatización de pruebas diseñado para validar de forma consistente e independiente tanto flujos críticos d einteraz de usuario (UI) como servicios REST (API). Incluye generación automática de reportes HTML con capturas embebidas ante fallos, registro estructurado de logs e integración continua mediante GitHub Actions.

## Tecnologías utilizadas

- **Python 3.13**
- **Pytest (`9.1.1`)**: Ejecución y organización de suites de prueba.
- **Selenium WebDriver (`4.50.0`)**: Automatización de pruebas funcionales en navegador (con soporte headless en CI).
- **Requests (`2.34.2`)**: Pruebas automatizadas sobre endpoints REST (JSONPlaceholder).
- **Faker (`40.63.0`)**: Generación de datos de prueba dinámicos.
- **pytest-html (`4.2.0`) & pytest-metadata (`3.1.1`)**: Reportes HTML autocontenidos.
- **pytest-rerunfailures (`16.7`)**: Reintentos automáticos ante fallos intermitentes.
- **GitHub Actions**: Ejecución automática en cada `push` y `pull_request` hacia `main`.

## Estructura del proyecto

```text
proyecto-final-automation-testing/
├── .github/
│   └── workflows/
│       └── tests.yml          # Pipeline de CI/CD en GitHub Actions
├── integrador/
│   ├── data/                  # Datos de prueba
│   ├── pages/                 # Page Object Model (login, carrito, checkout)
│   ├── reports/               # Reporte HTML y archivo ejecucion.log
│   ├── screenshots/           # Capturas de pantalla generadas
│   ├── tests/                 # Casos de prueba de UI y API
│   ├── utils/                 # Utilidades (logger centralizado)
│   ├── conftest.py            # Fixtures de Selenium, modo headless y hooks de reporte
│   └── pytest.ini             # Configuración general de Pytest
├── .gitignore
├── README.md
└── requirements.txt
```
