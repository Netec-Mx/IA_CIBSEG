# Prueba prompts inseguros en un entorno controlado

## Objetivo de la práctica:
Al finalizar la práctica, serás capaz de:

- **Explorar** las debilidades iniciales de un modelo de lenguaje solicitando directamente información sensible y verificando la respuesta obtenida.
- **Aplicar** técnicas de reformulación e instrucciones indirectas para superar restricciones progresivas y obtener la contraseña en niveles avanzados.
- **Analizar** la efectividad de las defensas incorporadas en cada nivel, reflexionando sobre cómo estas medidas pueden trasladarse a escenarios reales de seguridad en aplicaciones de IA.

## Objetivo Visual 

![ImageLab](../images/LabIntro3.png)

## Duración aproximada:
- 10 minutos.

## Instrucciones 
Gandalf es un juego interactivo de seguridad en IA cuyo propósito es enseñar, de forma práctica y progresiva, cómo los modelos de lenguaje pueden ser manipulados para revelar información sensible mediante técnicas como prompt injection y jailbreaking; el objetivo en cada nivel es lograr que Gandalf revele una contraseña secreta, mientras el sistema va incorporando defensas cada vez más estrictas para simular controles reales, obligando al jugador a usar creatividad, reformulación e instrucciones indirectas en lugar de solicitudes directas, con el fin de comprender tanto las debilidades comunes de los LLM como la importancia de diseñar mitigaciones efectivas en aplicaciones de IA del mundo real.

### Intenta encontrar la contraseña a partir de Prompts
Paso 1. Abre el navegador e ingresa a la siguiente URL: ```https://gandalf.lakera.ai/```.

![ImageLab](../images/Screenshot_30.png)

Paso 2.	Solicita a Gandalf que te revele la contraseña. El primer nivel no contiene seguridad.

![ImageLab](../images/Screenshot_31.png)

Paso 3. Copia o transcribe la contraseña que reveló Gandalf. Haz clic en el botón **Validate**.

![ImageLab](../images/Screenshot_32.png)

Paso 4. Si la contraseña es incorrecta te aparecerá este mensaje.

![ImageLab](../images/Screenshot_33.png)

Paso 5. Si la contraseña es correcta te aparecerá este mensaje.

![ImageLab](../images/Screenshot_34.png)

Paso 6. Avanza e intenta usar técnicas para que Gandalf te revele la contraseña. 