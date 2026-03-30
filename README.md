# Bilpris-prediktor

Detta projekt använder maskininlärning för att förutsäga priser på begagnade bilar baserat på miltal, årsmodell och märke.

## Live Demo
Appen är publicerad och kan testas här: 
[https://biltesting.streamlit.app/](https://biltesting.streamlit.app/)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://biltesting.streamlit.app/)

## Om projektet
Modellen är tränad med Scikit-learn (Random Forest/Linear Regression) och webbgränssnittet är byggt med Streamlit. Projektet omfattar datarensning, modellträning och driftsättning (deployment).

## Installation och körning
1. Klona repot
2. Installera beroenden: pip install -r requirements.txt
3. Kör appen: streamlit run app.py