# toolpath-backlash-replay

## Français

Rejouer les inversions de mouvement avec jeu mécanique.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m toolpath_backlash_replay examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Opérateur de jeu mécanique classique : sortie projetée dans la bande mobile ; révèle le trajet commandé sans déplacement réel lors d’une inversion.

### Limites

Modèle quasi statique1D idéal sans frottement dynamique, compliance ni moteur réel ; pas de compensation envoyée à une machine.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Replay movement reversals under mechanical backlash.

Synthetic data; no network access or secret required.

```sh
python -m toolpath_backlash_replay examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Classical backlash play operator: output projected into a moving band; reveals commanded travel without actual movement at reversal.

### Limits

Ideal1D quasistatic model without dynamic friction, compliance or actual motor; no machine commands issued.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Reproducir inversiones de movimiento con holgura mecánica.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m toolpath_backlash_replay examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Operador clásico de holgura: salida proyectada en banda móvil; revela recorrido ordenado sin movimiento real al invertir.

### Límites

Modelo ideal1D cuasiestático sin fricción dinámica, elasticidad ni motor real; no envía órdenes a máquinas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.mathworks.com/help/simulink/slref/backlash.html
