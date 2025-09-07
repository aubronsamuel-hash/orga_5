# Backend

## Authentification de developpement

### Login
`POST /auth/login` avec le corps suivant :

```
{ "role": "admin" }
```

Retour :

```
{ "token": "admin" }
```

Utiliser l'en-tete `Authorization: Bearer admin` pour acceder aux routes protegees.

### Roles
- admin
- planner
- tech

## Changelog
- 2025-09-07 : ajout de l'authentification de developpement et des roles.
