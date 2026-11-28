# Contexto Científico de Referencia — Study Tracker

Síntesis estructurada de la evidencia teórica para diseñar los indicadores, preguntas de sesión, visualizaciones y futuras mecánicas de gamificación.

---

## 1. Arquitectura Cognitiva y Dificultad Deseable
- **Aprendizaje vs. Rendimiento (Soderstrom & Bjork, 2015):** El desempeño inmediato durante la sesión es un mal predictor de retención a largo plazo. La fluidez rápida genera *ilusión de competencia* (Benjamin, Bjork & Schwartz, 1998) y lleva a malinterpretar el esfuerzo productivo como fracaso (*misinterpreted-effort hypothesis*; Kirk-Johnson, Galla & Fraundorf, 2019).
- **Nueva Teoría del Desuso (Bjork & Bjork, 1992, 2011):** La memoria tiene dos fuerzas independientes: *Fuerza de Almacenamiento* ($S$, durabilidad) y *Fuerza de Recuperación* ($R$, accesibilidad momentánea). La ganancia de aprendizaje es inversamente proporcional a qué tan fácil fue recordar: $\Delta S \propto f(1/R)$.
- **Teoría de Carga Cognitiva (Sweller, 1988):**
  - *Intrínseca:* complejidad propia del tema según conocimiento previo.
  - *Extraña (dificultad indeseable):* ruido, malas instrucciones o fricción inútil; satura la memoria de trabajo.
  - *Germana (dificultad deseable):* esfuerzo dirigido a construir esquemas y discriminar conceptos.
- **Efecto de Inversión de la Pericia (Chen, Kalyuga & Sweller):** Novatos requieren andamiaje y ejemplos resueltos; conforme crece el dominio, deben transicionar a recuperación activa y entrelazado.
- **Estrategias validadas:**
  - *Recuperación activa / Testing Effect:* supera ampliamente la relectura ($g = 0.50\text{–}0.61$; Rowland, 2014; Adesope et al., 2017; Roediger & Karpicke, 2006). Más potente en formato generativo (respuesta abierta) con feedback diferido.
  - *Entrelazado (Interleaving):* efectivo globalmente ($g = 0.42$; Brunmair & Richter, 2019), especialmente en categorización visual ($g = 0.67$) y matemáticas/problemas ($g = 0.34$, hasta $d = 0.83$ diferido). El bloqueo sigue siendo mejor en pares aislados o listas de palabras ($g = -0.39$).
  - *Ranking de utilidad (Dunlosky et al., 2013):* Alta (práctica de recuperación, práctica distribuida); Moderada (interrogación elaborativa, autoexplicación, entrelazado); Baja (relectura, subrayado, resúmenes literales).

## 2. Memoria Temporal y Repetición Espaciada
- **Curva del Olvido y Sueño (Ebbinghaus, 1885; Murre & Dros, 2015):** El olvido cae exponencialmente en las primeras horas, pero existe un repunte a las **24 horas** por consolidación durante el sueño. El primer repaso activo conviene situarlo tras un ciclo completo de sueño.
- **Cresta Temporal Óptima (Cepeda et al., 2006, 2008):** El intervalo óptimo entre sesiones ($ISI$) escala según el plazo hasta la evaluación ($RI$): ~20–30% para 1 semana, ~10–15% para 1 mes, ~5–8% para 1 año.
- **Modelo DSR y FSRS (Woźniak; Jarrett Ye):** Modela *Dificultad* ($D$), *Estabilidad* ($S$, días para caer de 100% a 90% de recuerdo) y *Accesibilidad* ($R(t) = e^{-t/S}$). Repasar cerca de $R \approx 85\text{–}90\%$ maximiza el salto de estabilidad. FSRS reduce la carga de repaso un 20–30% frente a SM-2 con igual retención.

## 3. Generación Propia, Delegación y Deuda Cognitiva por IA
- **Efecto de Generación (Slamecka & Graf, 1978):** Producir la respuesta propia mejora el recuerdo un 25–40% frente a leerla pasivamente (requiere conocimiento base previo y corrección de errores).
- **Delegación Cognitiva (Risko & Gilbert, 2016):** Depende de juicios metacognitivos (a menudo mal calibrados) y distorsiona la percepción de conocimiento propio. Delegar habilidades en desarrollo causa atrofia funcional (ej. pérdida de memoria espacial por uso habitual de GPS; Dahmani & Bohbot, 2020).
- **Deuda Cognitiva con LLMs:**
  - *Kosmyna et al. (2025, MIT Media Lab):* Registros EEG mostraron menor conectividad alfa/beta, menor recuerdo y pérdida de autoría en usuarios que redactaron con LLM desde el inicio; al quitarles la IA mantuvieron bajo desempeño. **Regla de diseño:** primero generación autónoma (*brain-first*), después verificación/asistencia con IA.
  - *Bastani et al. (2025, PNAS):* GPT sin restricciones subió el rendimiento en práctica (+48%) pero lo desplomó en examen sin IA (-17%). GPT Tutor con pistas socráticas subió la práctica (+127%) sin pérdida en examen autónomo.
  - *Gerlich (2025) y Lee et al. (2025, CHI):* Fuerte correlación negativa entre delegación en IA y pensamiento crítico ($r = -0.75$); mayor confianza en la IA reduce el esfuerzo analítico propio.

## 4. Arquitectura Motivacional (Base para Fase 2: Gamificación)
- **Teoría de la Autodeterminación — SDT (Deci & Ryan, 1985, 2000):** La motivación sostenible requiere satisfacer tres necesidades: **autonomía, competencia y relación**. Las mecánicas basadas en culpa o presión (regulación externa/introyectada, ej. rachas punitivas) generan adherencia frágil.
- **Efecto de Sobrejustificación (Deci, 1971; Deci, Koestner & Ryan, 1999):** Recompensas tangibles, esperadas y controladoras socavan la motivación intrínseca. El feedback informativo que valida competencia la protege o aumenta.
- **Proceso vs. Resultado y Feedback Sabio:**
  - Premiar esfuerzo/estrategia fomenta resiliencia ante el error frente a premiar resultado/talento (Mueller & Dweck, 1998). En estudiantes mayores, los eslóganes genéricos tienen impacto mínimo ($d = 0.08$; Sisk et al., 2018; Glerum et al., 2019): importa el **feedback técnico específico**.
  - *Wise Feedback (Yeager et al., 2014):* Combinar estándares altos con confianza explícita en la capacidad aumenta la revisión voluntaria.
- **Lineamiento de Gamificación (Chou, Octalysis + SDT):** Priorizar *White Hat* (progreso real de dominio, árboles de habilidades, logros por lucha productiva) sobre *Black Hat* (rachas de login o miedo a perder puntos).

## 5. Principios de Visualización de Datos (Munzner, 2014)
- **Marco What–Why–How:** Definir primero el tipo de dato (*What*) y la pregunta analítica (*Why*: tendencia, correlación, distribución, anomalía) antes de elegir el gráfico (*How*).
- **Derivación activa de atributos:** No limitarse a graficar horas estudiadas; derivar métricas compuestas (ej. índice de calibración metacognitiva, ratio *brain-first* vs. *AI-first*, estabilidad estimada vs. olvido).
- **Jerarquía de canales visuales:** Usar posición en escala común para magnitudes críticas (líneas, dispersión, barras alineadas), tono de color solo para categorías y luminancia/saturación para intensidad ordenada (mapas de calor). Usar *small multiples* para comparar múltiples variables sin saturar una sola vista.