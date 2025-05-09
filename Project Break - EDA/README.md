# 🃏 Pokémon TCG Pocket — Exploratory Data Analysis (EDA)

## 📌 Descripción del Proyecto

Este proyecto realiza un pequeño análisis de los últimos torneos de **Pokémon TCG Pocket** para poder ver como se va desenvolviendo el metagame con la salida del nuevo sobre Celestial Guardians. El análisis tiene en cuenta solo datos de top 16.

**Nota: Disculpad si la información no se entiende mucho, enfoqué el proyecto de forma que fuera a hacer una presentación a alguien que tuviera interés previo en recibir los datos, por lo que se asume cierto conocimiento sobre el contexto. La información creo que está suficientemente clara por lo que se debería entender de que va y lo que pretende conseguir igualmente.**

Información sacada de [aquí](https://play.limitlesstcg.com/tournaments/completed?game=POCKET&format=all&platform=all&type=online&time=7days&page=1)

---

## 🧾 Descripción del Dataset

- **Deck**: Nombre de cada deck
- **Placement**: Posicionamiento final dentro del torneo
- **Tournament**: Nombre del torneo
- **Players**: Cantidad de participantes
- **Tier**: Clasificación de torneo basada en el número de jugadores:
  - Tier 1: +128
  - Tier 2: +64
  - Tier 3: 64 o menos

---

## 🔍 Objetivos del Análisis

- Identificar los **mazos más jugados**.
- Comparar la **representación** y **desempeño promedio** de los mazos.
- Ver cuántos **torneos ha ganado cada mazo**.
- Analizar los **5 mazos más populares** en profundidad.
- Explorar la **evolución del rendimiento** por fecha.
- Visualizar relaciones clave mediante **gráficos y heatmaps**.

---

## 📁 Datos

El dataset empleado se ubica en:

```
SRC/data/df_pocket_clean.csv
```

aunque también está disponible el código para sacar los datos. Tener en cuenta la limitación de las peticiones de la propia web.
