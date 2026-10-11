# strategy-war-game
Описание: agent-based симулятор конкурентной борьбы. Компании-агенты, эволюция стратегий, сценарии, веб-визуализация.  Стек: Python, Mesa, FastAPI, Streamlit, Plotly, Docker.

# strategy-war-game

Agent-based симулятор конкурентной борьбы между компаниями.

## Возможности
- 4 стратегии: cost_leader, differentiator, aggressive, balanced
- Готовые сценарии: baseline, crisis, boom, price_war
- Кастомные параметры рынка
- REST API + Streamlit-дашборд
- Экспорт истории

## Быстрый старт

docker-compose up --build

API: http://localhost:8000/docs
Dashboard: http://localhost:8501

## Тесты

pytest tests/ -v

## Лицензия
MIT
