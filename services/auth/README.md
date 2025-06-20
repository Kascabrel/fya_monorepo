auth-service/
├── api/                  ← Abstract network interfaces (REST/gRPC)
│   ├── rest/             ← Implementation REST (FastAPI/Flask)
│   │   └── controllers/
│   ├── grpc/             ← (à venir) Implémentation gRPC (gRPC stubs, etc.)
│   └── interfaces.py     ← Abstractions des "use cases" exposés
│
├── core/                 ← Domaine métier (indépendant de REST/gRPC)
│   ├── models/           ← Pydantic ou dataclasses
│   ├── services/         ← Logique métier (ex: AuthService, JWTManager, etc.)
│   └── ports/            ← Interfaces vers infrastructure (DB, cache, etc.)
│
├── infrastructure/       ← Implémentations concrètes (SQLAlchemy, Redis, etc.)
│   ├── repositories/
│   └── adapters/         ← Ex: JWTAdapter, EmailSender
│
├── tests/
│
├── main.py               ← Point d’entrée REST (ou gRPC ensuite)
├── requirements.txt
└── pyproject.toml