# FourTriesDekker
FourTriesDekker

Versiones previas al algortimo más eficiente de Dekker

- Versión 1: *Alternancia estricta*. Garantiza la exclusión mutua, pero su desventaja es que acopla los procesos fuertemente, esto significa que los procesos lentos atrasan a los procesos rápidos.
- Versión 2: *Problema interbloqueo*. No existe la alternancia, aunque ambos procesos caen a un mismo estado y nunca salen de ahí.
- Versión 3: Colisión región crítica *no garantiza la exclusión mutua*. Este algoritmo no evita que dos procesos puedan acceder al mismo tiempo a la región crítica.
- Versión 4: *Postergación indefinida*. Aunque los procesos no están en interbloqueo, un proceso o varios se quedan esperando a que suceda un evento que tal vez nunca suceda *Livelock*.


