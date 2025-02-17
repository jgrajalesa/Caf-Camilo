import streamlit as st

# Título de la aplicación
st.title("☕ Calculadora de Precio Real de Café")

# Imagen decorativa (puedes agregar una imagen relacionada con el café)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Coffee_Beans.jpg/800px-Coffee_Beans.jpg", use_column_width=True)

# Sección para calcular el porcentaje de pérdida de peso automáticamente
st.subheader("🔄 Calculadora de Porcentaje de Pérdida de Peso")

# Ingreso del peso inicial y final del café
peso_inicial = st.number_input("Peso inicial del café (en gramos):", min_value=1, value=1000)
peso_final = st.number_input("Peso final del café (después de la pérdida de peso) (en gramos):", min_value=1, value=750)

# Cálculo automático del porcentaje de pérdida de peso
porcentaje_perdida_calculado = (1 - peso_final / peso_inicial) * 100
st.write(f"Porcentaje de pérdida de peso calculado: {porcentaje_perdida_calculado:.2f}%")

# Opción de calcular el porcentaje manualmente
usar_calculo_automatico = st.checkbox("Usar cálculo automático del porcentaje de pérdida de peso", value=True)

# Bloqueamos el input de porcentaje de pérdida de peso si se usa el cálculo automático
if usar_calculo_automatico:
    porcentaje_perdida = porcentaje_perdida_calculado
    st.write(f"El porcentaje de pérdida de peso utilizado será: {porcentaje_perdida:.2f}%")
else:
    # Ingreso manual del porcentaje de pérdida
    porcentaje_perdida = st.number_input(
        "Ingresa el porcentaje de pérdida de peso (%):", 
        min_value=0.0, 
        max_value=100.0, 
        value=10.0, 
        step=0.1
    )

# Reordenando el flujo de entrada de datos:

# 1. Ingreso del peso del café
peso_cafe = st.number_input("Ingresa el peso del café en gramos:", min_value=1, value=1000)

# 2. Ingreso del precio del café total
precio_cafe = st.number_input("Ingresa el precio del café total (en tu moneda):", min_value=0.0, value=10.0)

# 3. Ingreso del precio del tostado por gramo
precio_tostado_por_gramo = st.number_input("Ingresa el precio del tostado por gramo (en tu moneda):", min_value=0.0, value=0.005)

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
### ☕ Código por Juan Grajales para Berraquita Café.
""")
