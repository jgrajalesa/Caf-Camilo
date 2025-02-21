import streamlit as st

# Título de la aplicación
st.title("☕ Calculadora de Precio Real de Café")

# Instrucciones iniciales
st.markdown("""
### Bienvenido a la calculadora de café ☕
Aquí podrás calcular el precio real de tu café antes y después del tostado, teniendo en cuenta la pérdida de peso durante el proceso.

**Por favor sigue los siguientes pasos:**
1. Ingresa el precio total del café que pagaste.
2. Establece el costo por gramo del tostado.
3. Si deseas, puedes calcular automáticamente el porcentaje de pérdida de peso ingresando el peso inicial y final de tu café, o si prefieres, puedes ingresar el porcentaje manualmente.
""")

# Sección para calcular el porcentaje de pérdida de peso automáticamente
st.subheader("🔄 Calculadora de Porcentaje de Pérdida de Peso")

# Opción de calcular el porcentaje automáticamente o ingresarlo manualmente
usar_calculo_automatico = st.radio(
    "¿Cómo deseas calcular el porcentaje de pérdida de peso?",
    ("Calcular automáticamente", "Ingresar porcentaje manualmente")
)

if usar_calculo_automatico == "Calcular automáticamente":
    # Si el usuario opta por calcular automáticamente el porcentaje, pedimos los pesos inicial y final
    st.write("Para calcular automáticamente, ingresa el peso inicial y final del café.")
    
    # Ingreso del peso inicial y final del café
    peso_inicial = st.number_input("Peso inicial del café (en gramos):", min_value=1.000, value=1000.000, help="Peso del café antes de perder parte de su masa.")
    peso_final = st.number_input("Peso final del café (en gramos, después de la pérdida):", min_value=1.000, value=750.000, help="Peso del café después de la pérdida de masa.")

    # Cálculo automático del porcentaje de pérdida de peso
    porcentaje_perdida_calculado = (1 - peso_final / peso_inicial) * 100
    st.write(f"Porcentaje de pérdida de peso calculado: {porcentaje_perdida_calculado:.2f}%")

    porcentaje_perdida = porcentaje_perdida_calculado  # Utilizamos el porcentaje calculado automáticamente

else:
    # Si el usuario decide ingresar el porcentaje manualmente
    st.write("Ingresa el porcentaje de pérdida de peso según tu experiencia o estimación.")
    # Ingreso manual del porcentaje de pérdida
    porcentaje_perdida = st.number_input(
        "Ingresa el porcentaje de pérdida de peso (%):", 
        min_value=0.000, 
        max_value=100.000, 
        value=10.000, 
        step=0.1,
        help="Porcentaje de pérdida de peso durante el tostado."
    )

# Reordenando el flujo de entrada de datos:

# 1. Ingreso del peso del café
peso_cafe = st.number_input("Ingresa el peso del café en gramos:", min_value=1.000, value=1000.000, help="Peso total del café que compraste en su estado original.")

# 2. Ingreso del precio del café total
precio_cafe = st.number_input("Ingresa el precio total del café (en tu moneda):", min_value=0.000, value=10.000, help="Precio que pagaste por el café sin tostar.")

# 3. Ingreso del precio del tostado por gramo
precio_tostado_por_gramo = st.number_input("Ingresa el precio del tostado por gramo (en tu moneda):", min_value=0.000, value=0.005, help="Costo del proceso de tostado por gramo de café.")

# 4. El porcentaje de pérdida de peso ya está calculado o ingresado

# Cálculo del peso real después de la pérdida de peso
peso_real = peso_cafe * (1 - porcentaje_perdida / 100)

# Cálculo del precio de tostado total (por gramo)
precio_tostado_total = peso_real * precio_tostado_por_gramo

# Cálculo del precio total del café (café + tostado)
precio_total = precio_cafe + precio_tostado_total

# Cálculo del precio real por gramo de café después de la pérdida de peso
precio_real_por_gramo = precio_total / peso_real

# Mostrar resultados
st.subheader("🎯 Resultados:")
st.write(f"Peso real del café después de la pérdida de peso: {peso_real:.2f} gramos")
st.write(f"Precio total del café (café + tostado): {precio_total:.2f} {st.session_state.get('moneda', 'unidades monetarias')}")
st.write(f"Precio real por gramo de café después de la pérdida de peso: {precio_real_por_gramo:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")

# Mostrar resultados antes y después del pago del tostado
st.subheader("🔍 Comparación antes y después del pago del tostado:")
st.write(f"Precio por gramo antes del tostado: {precio_cafe / peso_cafe:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")
st.write(f"Precio por gramo después del tostado: {precio_real_por_gramo:.4f} {st.session_state.get('moneda', 'unidades monetarias')} por gramo")

# Decoración con texto adicional para hacerlo más atractivo
st.markdown("""
---
### ☕ Código por Juan Grajales para Berraquita Café
""")
